from icecube_data_reader.event_types import DR2, DR1
from icecube_data_reader.events import IceTrackDR2Events

def test_event_number():
    events = IceTrackDR2Events.from_event_files()
    assert events.N == 1643355