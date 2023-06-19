# You would like to run for city council, and you would like to collect vote from people in one neighborhood in person.
# You would like to meet with everyone in that neighborhood by making as few trips as possible.
# For simplicity, once you arrive at neighborhood, you instantly receive peoples' votes that are in the neighborhood at that time.
# You have people's schedule:
# A sequence of segments [ [L1, R1], ..., [Ln, Rn] ] is the schedule for each individual presence in that neighborhood.
# You would like to find a set of minimum points in time such that if you visit the neighborhood during those time instances,
# you are able to meet with all people and collect their votes.
#
# For example:
#
# Input:  [Segment(1, 3), Segment(2, 5), Segment(3, 6)]
# Output: [3] (length of time points: 1)
#
# Input:  [Segment(1, 3), Segment(2, 5), Segment(6, 7)]
# Output: [3, 6] (length of time points: 2)

# Solve a larger test case:

# Dionysi Ntreou Solution:


# The Segment class has been introduced based on the assumptions made when reading the exercise description,
# specifically the provided dataset. The Segment class encapsulates the start and end fields
class Segment:
    def __init__(self, start: int, end: int):
        if start > end:
            raise ValueError("Invalid segment: start cannot be greater than end.")
        self.start = start
        self.end = end


# The Scheduler class allows for breaking down responsibilities while following an OOP approach.
# It helps keep our functions that concern our segments together and encapsulates their logic.
class Scheduler:
    def __init__(self, segments: list[Segment]):
        self.segments = segments

    def find_minimum_points(self) -> list[int]:
        """Find the minimum points needed to cover all segments."""

        # Ensuring that if segments do not contain any elements,
        # we handle it instead of allowing our program to run and throw an error when trying to access a field
        # of a non-existing element in the list. Of course, we can always wrap it in a try-catch block
        if not self.segments:
            return []

        # Firstly, we will begin by sorting our list of segments by the 'From' time.
        # Having our array sorted will help us easily identify the optimal time.
        # I have chosen to implement a merge sort instead of using the built-in .sort() method to showcase
        # how I would implement a sorting algorithm like merge sort, which has a time complexity of O(n log n).
        sorted_segments = self.sort_segments(self.segments)
        points = []

        # Since our points list is not populated, we insert the 'END' field of our first segment and set it as our
        # current end. Another approach for this would be to incorporate this logic below the if statement that
        # checks if our points array is empty. If it is, we insert the first item, and instead of setting the current
        # end as we have, we could also use 'points[-1].end'
        current_end = sorted_segments[0].end
        points.append(current_end)

        # The approach followed here is to check if the 'START' field of the segment we are pulling from our sorted
        # list is greater than the end time already present in our points list. This way, we can be certain that,
        # by having a sorted list of segments, the segments that overlap, even from the start of one to the end of
        # another, are 'grouped' i.e. have 1 common point.
        for segment in sorted_segments:
            if segment.start > current_end:
                current_end = segment.end
                points.append(current_end)
            else:
                current_end = min(current_end, segment.end)

        return points

    def sort_segments(self, segments: list[Segment]) -> list[Segment]:
        """Sort the segments using merge sort algorithm."""
        if len(segments) <= 1:
            return segments

        # We split the list in the middle using the // operator to perform floor division.
        # This is done because when you have arrays that, when divided by 2,
        # result in a numeric value followed by a decimal point. and there is no index 2.5 haha :)
        mid = len(segments) // 2

        # Recursively sorting both halves (left and right).
        left = self.sort_segments(segments[:mid])
        right = self.sort_segments(segments[mid:])

        return self.merge(left, right)

    def merge(self, left: list[Segment], right: list[Segment]) -> list[Segment]:
        """Merge two sorted lists of segments into one sorted list."""

        # Here, we are going to initialize our "indexers" that will help us avoid going out of bounds and keep track
        # of the index we are on in each list (left or right) of our ordered list.
        i, j = 0, 0
        ordered = []

        # We will loop until we reach both bounds of the provided lists (left and right) and appropriately insert
        # the item with the lesser value first. Then we will progressively increase the index of the value that has
        # been visited and added to the ordered list.
        while i < len(left) and j < len(right):
            if left[i].start < right[j].start:
                ordered.append(left[i])
                i += 1
            else:
                ordered.append(right[j])
                j += 1

        ordered.extend(left[i:])
        ordered.extend(right[j:])

        return ordered


if __name__ == "__main__":
    input_segments = [Segment(41, 42),
                      Segment(52, 52),
                      Segment(63, 63),
                      Segment(80, 82),
                      Segment(78, 79),
                      Segment(35, 35),
                      Segment(22, 23),
                      Segment(31, 32),
                      Segment(44, 45),
                      Segment(81, 82),
                      Segment(36, 38),
                      Segment(10, 12),
                      Segment(1, 1),
                      Segment(23, 23),
                      Segment(32, 33),
                      Segment(87, 88),
                      Segment(55, 56),
                      Segment(69, 71),
                      Segment(89, 91),
                      Segment(93, 93),
                      Segment(38, 40),
                      Segment(33, 34),
                      Segment(14, 16),
                      Segment(57, 59),
                      Segment(70, 72),
                      Segment(36, 36),
                      Segment(29, 29),
                      Segment(73, 74),
                      Segment(66, 68),
                      Segment(36, 38),
                      Segment(1, 3),
                      Segment(49, 50),
                      Segment(68, 70),
                      Segment(26, 28),
                      Segment(30, 30),
                      Segment(1, 2),
                      Segment(64, 65),
                      Segment(57, 58),
                      Segment(58, 58),
                      Segment(51, 53),
                      Segment(41, 41),
                      Segment(17, 18),
                      Segment(45, 46),
                      Segment(4, 4),
                      Segment(0, 1),
                      Segment(65, 67),
                      Segment(92, 93),
                      Segment(84, 85),
                      Segment(75, 77),
                      Segment(39, 41),
                      Segment(15, 15),
                      Segment(29, 31),
                      Segment(83, 84),
                      Segment(12, 14),
                      Segment(91, 93),
                      Segment(83, 84),
                      Segment(81, 81),
                      Segment(3, 4),
                      Segment(66, 67),
                      Segment(8, 8),
                      Segment(17, 19),
                      Segment(86, 87),
                      Segment(44, 44),
                      Segment(34, 34),
                      Segment(74, 74),
                      Segment(94, 95),
                      Segment(79, 81),
                      Segment(29, 29),
                      Segment(60, 61),
                      Segment(58, 59),
                      Segment(62, 62),
                      Segment(54, 56),
                      Segment(58, 58),
                      Segment(79, 79),
                      Segment(89, 91),
                      Segment(40, 42),
                      Segment(2, 4),
                      Segment(12, 14),
                      Segment(5, 5),
                      Segment(28, 28),
                      Segment(35, 36),
                      Segment(7, 8),
                      Segment(82, 84),
                      Segment(49, 51),
                      Segment(2, 4),
                      Segment(57, 59),
                      Segment(25, 27),
                      Segment(52, 53),
                      Segment(48, 49),
                      Segment(9, 9),
                      Segment(10, 10),
                      Segment(78, 78),
                      Segment(26, 26),
                      Segment(83, 84),
                      Segment(22, 24),
                      Segment(86, 87),
                      Segment(52, 54),
                      Segment(49, 51),
                      Segment(63, 64),
                      Segment(54, 54)]
    scheduler = Scheduler(input_segments)
    minimum_points = scheduler.find_minimum_points()

    print(f"Minimum points: {minimum_points} (length of time points: {len(minimum_points)})")

    # for item in sorted_segment:
    #     print(item.start, item.end, ", ")
    # find_optimal_visit_times(sorted_segment)
