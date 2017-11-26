import unittest
from typing import List, Set, Dict, Iterator
from unittest import TestCase


class BloomFilter(object):
    """
    A bloom filter is a probabilistic data structure that trades space for accuracy.
    when determining if a value is in a set, it can tell you if a value was possibly added,
    or if it was definitely not added, but it can't tell you for certain that it was added
    """
    values: List[bool] = []
    size: int = -1

    def __init__(self, size: int):
        """Set up the BF whith the appropriate size"""
        self.values = [False] * size
        self.size = size

    def hash_value(self, value: object) -> int:
        """Has the value provided and scale it to fit the BF size"""
        return hash(value) % self.size

    def add_value(self, value: object):
        """Add a value to the BF"""
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self, value: object) -> bool:
        """check if the value might be in the BF"""
        h = self.hash_value(value)
        return self.values[h]

    def __str__(self):
        return "\t".join([str(v) for v in self.values])


def major_segments(s: str) -> Set[str]:
    """
    Perform major segmenting on a string. split the string by all of the major breaks.
    and return the set of everything found. The breaks in this implementation a single characters,
    but in splunk proper they can be multiple characters.
    A set is used because ordering doesn't matter, and duplicates are bad
    :param s:
    :return:
    """
    major_breaks: str = ' '
    last: int = -1
    results: Set[str] = set()

    for idx, ch in enumerate(s):
        if ch in major_breaks:
            segment: str = s[last + 1: idx]
            results.add(segment)
            last = idx

    # the last character may not be a break so always capture
    # the last segment (which may end up being "", but yolo)
    segment: str = s[last + 1:]
    results.add(segment)

    return results


def minor_segments(s: str) -> Set[str]:
    """
    Perform minor segmenting on a string, this is like major segmenting,
    :except it also captures from the start of the input to each break
    :param s:
    :return:
    """
    minor_break: str = '_.'
    last: int = -1
    results: Set[str] = set()

    for idx, ch in enumerate(s):
        if ch in minor_break:
            results.add(s[last + 1:idx])
            results.add(s[:idx])
            last = idx

    results.add(s[last + 1:])
    results.add(s)
    return results


def segments(event: str) -> Set[str]:
    results: Set[str] = set()
    for major in major_segments(event):
        for minor in minor_segments(major):
            results.add(minor)
    return results


class Splunk(object):
    bf: BloomFilter = BloomFilter(64)
    terms: Dict[str, Set[str]] = {}
    events: List[str] = []

    def __init__(self):
        pass

    def add_event(self, event: str):
        """Adds an event to this object"""
        # Generate a unique ID for the event, and save it
        event_id: int = len(self.events)
        self.events.append(event)

        # Add each term to the bloom filter, and track the event by each term
        for term in segments(event):
            self.bf.add_value(term)

            if term not in self.terms:
                self.terms[term] = set()
            self.terms[term].add(event_id)

    def search(self, term: str) -> Iterator[str]:
        """Search for a single term, and yield all the events that contain it"""
        # in Splunk this runs in o(1), and is likely to be in filesystem cache(memory)
        if not self.bf.might_contain(term):
            return

            # In Splunk this probably runs in O(logN) where N is the number of terms in the tsidx
        if term not in self.terms:
            return

        for event_id in sorted(self.terms[term]):
            yield self.events[event_id]

    def search_all(self, terms: List[str]) -> Iterator[str]:
        """Search for an AND of all terms"""
        # start with the universe of all events
        results: Set[str] = set(range(len(self.events)))

        for term in terms:
            # if a term is not present at all then we can stop looking
            if not self.bf.might_contain(term):
                return
            if term not in self.terms:
                return

            # Drop events that don't match from our results
            results = results.intersection(self.terms[term])

        for event_id in sorted(results):
            yield self.events[event_id]

    def search_any(self, terms: List[str]) -> Iterator[str]:
        """Search for an OR of all terms"""
        results: Set[str] = set()
        for term in terms:
            # if a term is not present, we skip it, but don't stop
            if not self.bf.might_contain(term):
                continue
            if term not in self.terms:
                continue

            # Add these events to our results
            results = results.union(self.terms[term])
        for event_id in sorted(results):
            yield self.events[event_id]


class Tests(TestCase):
    def test_bloom_filter(self):
        bf: BloomFilter = BloomFilter(10)
        bf.add_value("dog")
        bf.add_value("fish")
        bf.add_value("cat")
        bf.add_value("cat")
        print(bf)
        bf.add_value("bird")
        print(bf)

    def test_segment(self):
        for term in segments("src_ip = 1.2.3.4"):
            print(term)

    def test_splunk(self):
        s: Splunk = Splunk()
        s.add_event("src_ip = 1.2.3.4")
        s.add_event("src_ip = 5.6.7.8")
        s.add_event("dst_ip = 1.2.3.4")

        for event in s.search("1.2.3.4"):
            print(event)
        print("-" * 20)
        for event in s.search("src_ip"):
            print(event)
        print("-" * 20)
        for event in s.search("ip"):
            print(event)

        print(['src_ip', '5.6'])
        for event in s.search_all(['src_ip', '5.6']):
            print(event)
        print("-" * 20)

        print(['src_ip', 'dst_ip'])
        for event in s.search_any(['src_ip', 'dst_ip']):
            print(event)
        print("-" * 20)


if __name__ == '__main__':
    unittest.main()
