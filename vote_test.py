import unittest

from vote import Segment, Scheduler


class SchedulerTests(unittest.TestCase):
    def test_find_minimum_points(self):
        segments = [Segment(1, 3), Segment(2, 4), Segment(3, 5), Segment(4, 6), Segment(5, 7)]
        scheduler = Scheduler(segments)
        minimum_points = scheduler.find_minimum_points()
        self.assertEqual(minimum_points, [3, 6])

    def test_find_minimum_points_non_overlapping_segments(self):
        segments = [Segment(1, 3), Segment(4, 6), Segment(7, 9)]
        scheduler = Scheduler(segments)
        minimum_points = scheduler.find_minimum_points()
        self.assertEqual(minimum_points, [3, 6, 9])

    def test_find_minimum_points_no_segments(self):
        scheduler = Scheduler(segments=[])
        minimum_points = scheduler.find_minimum_points()
        self.assertEqual(minimum_points, [])

    def test_find_minimum_points_single_segment(self):
        segments = [Segment(1, 3)]
        scheduler = Scheduler(segments)
        minimum_points = scheduler.find_minimum_points()
        self.assertEqual(minimum_points, [3])


class SegmentTestCase(unittest.TestCase):
    def test_segment_with_valid_input(self):
        segment = Segment(3, 6)
        self.assertEqual(segment.start, 3)
        self.assertEqual(segment.end, 6)

    def test_segment_with_invalid_input(self):
        with self.assertRaises(ValueError):
            segment = Segment(99, 2)


if __name__ == '__main__':
    unittest.main()

