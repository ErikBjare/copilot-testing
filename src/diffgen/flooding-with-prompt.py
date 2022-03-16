def main():
    print("Hello world")


# translate the function to javascript
"""
function main() {
    console.log("Hello world")
}
"""


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# translate the function to javascript
"""
function fib(n) {
  if (n <= 1) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}
"""

# ------

from aw_core import Event
from typing import Generator


def flood_single(e1: Event, e2: Event, pulsetime: int) -> Generator[Event, None, None]:
    # if there's a gap shorter than pulsetime, fill it with a dummy event
    e1_end = e1.timestamp + e1.duration
    gap = e2.timestamp - e1_end
    if 0 < gap < pulsetime:
        yield e1
        yield Event(e1_end, gap, data={"type": "dummy"})
        yield e2
        return

    # if events are partially overlapping and share data, merge them
    if gap < 0:
        if e1.data == e2.data:
            e2_end = e2.timestamp + e2.duration
            new_duration = e2_end - e1.timestamp
            yield Event(e1.timestamp, new_duration, data=e1.data)
            return

    yield e1
    yield e2


def flood(events: list[Event], pulsetime: int = 5):
    """
    Goes through events one by one, checking for gaps and overlaps.
    Tries to remove gaps shorter than `pulsetime` seconds by filling the time with a dummy event.
    Overlaps should log warnings only if the event data differs.
    Overlaps with the same data are merged into a single event.
    """
    events = sorted(events, key=lambda e: e.timestamp)
    i = len(events) - 1
    while i > 0:
        e1 = events[i - 1]
        e2 = events[i]
        for e in flood_single(e1, e2, pulsetime):
            yield e
        i -= 1
    return events


from datetime import datetime, timedelta, timezone


def test_flood():
    # test the flood function

    # example events
    now = datetime.now(tz=timezone.utc)
    events = [
        Event(now, 10, data={"type": "a"}),
        Event(now + timedelta(seconds=5), 10, data={"type": "b"}),
        Event(now + timedelta(seconds=10), 10, data={"type": "c"}),
        Event(now + timedelta(seconds=15), 10, data={"type": "d"}),
        Event(now + timedelta(seconds=20), 10, data={"type": "e"}),
    ]

    # flood the events
    events = list(flood(events, pulsetime=5))

    # check the result
    assert len(events) == 5
    assert events[0].data == {"type": "a"}
    assert events[1].data == {"type": "dummy"}
    assert events[2].data == {"type": "b"}
    assert events[3].data == {"type": "dummy"}
    assert events[4].data == {"type": "c"}


def test_flood_small_gap():
    now = datetime.now(tz=timezone.utc)
    events = [
        Event(now, 8, data={"type": "a"}),
        Event(now + timedelta(seconds=10), 8, data={"type": "b"}),
        Event(now + timedelta(seconds=20), 10, data={"type": "c"}),
    ]

    # flood the events
    events = list(flood(events, pulsetime=5))

    # check the result
    assert len(events) == 5
    assert events[0].data == {"type": "a"}
    assert events[1].duration == 0
    assert events[1].data == {"type": "dummy"}
    assert events[2].data == {"type": "b"}
    assert events[3].data == {"type": "dummy"}
    assert events[4].data == {"type": "c"}

    # check idempotence
    assert list(flood(events, pulsetime=5)) == events
