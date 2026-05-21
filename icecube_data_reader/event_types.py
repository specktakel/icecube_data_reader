"""
Organise different event types
"""

from dataclasses import dataclass

# TODO replace by hnu dataclasses
IC40 = "IC40"
IC59 = "IC59"
IC79 = "IC79"
IC86 = "IC86"
IC86_I = "IC86_I"
IC86_II = "IC86_II"


# And what have they ever given us in return...
suffixes = [
    "_I", "_II", "_III", "_IV", "_V", "_VI", "_VII", "_VIII", "_IX", "_X", "_XI"
]

@dataclass
class DR2:
    available_irfs = [IC40, IC59, IC79, IC86]


@dataclass
class DR1:
    available_irfs = [IC40, IC59, IC79, IC86_I, IC86_II]