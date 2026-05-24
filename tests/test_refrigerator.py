from icecube_data_reader.event_types import (
    Refrigerator, DR2
)

import pytest

def test_int2dm():
    for int_, dm in enumerate(DR2.available_irfs, 1):
        assert Refrigerator.int2dm(int_) == dm

    with pytest.raises(ValueError, match="No detector 0 available."):
        Refrigerator.int2dm(0)

def test_str2int():
    for int_, dm in enumerate(DR2.available_irfs, 1):
        assert Refrigerator.str2int(str(dm)) == dm.S

def test_dm_equality():
    for dm in DR2.available_irfs:
        assert dm == dm
        assert dm == dm()