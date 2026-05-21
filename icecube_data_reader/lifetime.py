"""
Organise lifetime intervals during which IceCube is operational and taking data
"""

import numpy as np
import os
from abc import ABC
from astropy import units as u
from astropy.time import Time
from .downloader import data_directory, I3_10, I3_14, available_datasets, IceCubeData
from .event_types import IC40, IC59, IC79, IC86, IC86_I, IC86_II, suffixes

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LifeTime(ABC):

    @property
    def data(self):
        return self._data


    def lifetime_from_mjd(self, mjd_min: float, mjd_max: float) -> dict[str|u.quantity.Quantity[u.yr]]:
        """Compute lifetime from provided min and max mjd.

        :param mjd_min: Minimum mjd
        :type mjd_min: float
        :param mjd_max: Maximum mjd
        :type mjd_max: float
        :return: Dictionary with detector season: duration in astropy.units.yr
        :rtype: dict[str|u.quantity.Quantity[u.yr]]
        """
        pass

    def lifetime_from_season(self, *seasons) -> dict[str|u.quantity.Quantity[u.yr]]:
        """Compute lifetime of given seasons

        :param seasons: Seasons to calculate lifetimes of
        :return: Dictionary with detector season: duration in astropy.units.yr
        :rtype: dict[str|u.quantity.Quantity[u.yr]]
        """

        pass

class DR2LifeTime(LifeTime):

    def __init__(self):

        directory = available_datasets[I3_14]["dir"]
        sub_directory = available_datasets[I3_14]["subdir"]
        # Check if data exists, otherwise download it
        try:
            np.loadtxt(
                os.path.join(
                    data_directory,
                    directory,
                    sub_directory,
                    "uptime",
                    "IC40_exp.csv",
                )
            )
        except FileNotFoundError:
            data_interface = IceCubeData()
            dataset = data_interface.find(I3_14)
            data_interface.fetch(dataset)
        
        # Array of start and end times
        self._times = np.zeros((4, 2))
        self._data = {}
        for c, s in enumerate([IC40, IC59, IC79, IC86]):
            if s != IC86:
                self._data[s] = np.loadtxt(
                    os.path.join(
                        data_directory,
                        directory,
                        sub_directory,
                        "uptime",
                        f"{s}_exp.csv",
                    )
                )
            else:
                data = []
                for suffering in suffixes:
                    data.append(
                        np.loadtxt(
                            os.path.join(
                                data_directory,
                                directory,
                                sub_directory,
                                "uptime",
                                f"{s+suffering}_exp.csv",
                            )
                        )
                    )
                self._data[s] = np.concatenate(data)
            #self._times[c, 0] = self._data[s][0, 0]
            #self._times[c, 1] = self._data[s][-1, -1]
    pass
