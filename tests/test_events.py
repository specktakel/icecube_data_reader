from icecube_data_reader.events import IceTrackDR2Events
from icecube_data_reader.event_types import IC40
from astropy import units as u
import numpy as np
from pathlib import Path

import pytest


def test_event_number():
    events = IceTrackDR2Events.from_event_files()
    assert events.N == 1643355

@pytest.fixture
def test_saving(output_directory):
    events = IceTrackDR2Events.from_event_files(IC40)
    path = events.to_file(Path(output_directory) / "ic40_events.h5")
    return (path, events)

def test_loading(test_saving):
    path, ic40 = test_saving
    loaded = IceTrackDR2Events.from_file(path)

    assert np.all(np.isclose(loaded.energy.to_value(u.GeV), ic40.energy.to_value(u.GeV)))

def test_selecting(test_saving):
    idx = 5
    _, events = test_saving
    N = events.N
    mask = np.zeros(N, dtype=bool)
    mask[idx] = True

    e = events.energy[idx].to_value(u.GeV)
    et = events.int_event_type[idx]
    events.select(mask)

    assert pytest.approx(events.energy[0].to_value(u.GeV)) == e
    assert et == events.int_event_type[0]