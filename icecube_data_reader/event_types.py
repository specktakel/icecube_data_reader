"""
Organise different event types
"""

from dataclasses import dataclass


class Meta(type):
    # Construct to add str(EventType)
    def __repr__(self):
        return self._str

    # Construct to add str(EventType())


class EventType:
    def __str__(self):
        return self._str


class IC40(EventType, metaclass=Meta):
    _str = "IC40"


class IC59(EventType, metaclass=Meta):
    _str = "IC59"


class IC79(EventType, metaclass=Meta):
    _str = "IC79"


class IC86(EventType, metaclass=Meta):
    _str = "IC86"


class IC86_I(EventType, metaclass=Meta):
    _str = "IC86_I"


class IC86_II(EventType, metaclass=Meta):
    _str = "IC86_II"


# And what have they ever given us in return...
suffixes = [
    "_I",
    "_II",
    "_III",
    "_IV",
    "_V",
    "_VI",
    "_VII",
    "_VIII",
    "_IX",
    "_X",
    "_XI",
]


@dataclass
class DR2:
    available_irfs = [IC40, IC59, IC79, IC86]


@dataclass
class DR1:
    available_irfs = [IC40, IC59, IC79, IC86_I, IC86_II]
