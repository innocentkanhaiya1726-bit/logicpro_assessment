# =============================================================================
#                         AI SOFTWARE ENGINEERING
#                    5th Semester - Training Assessment
#                   Time: 1 Hour | Maximum Marks: 50
# =============================================================================
# Questions and explanations are comments; Python answers are executable.
# SQL answers are multiline strings: run them in a database with the given tables.

# =============================================================================
# SECTION A - MCQs (10 x 1 = 10 Marks)
# =============================================================================

# 1. Which OOP concept allows a child class to reuse parent class features?
# A. Encapsulation B. Inheritance C. Polymorphism D. Abstraction
# Answer: B. Inheritance

# 2. Which file mode appends content?
# A. 'w' B. 'r' C. 'a' D. 'x'
# Answer: C. 'a'

# 3. Output of [x*x for x in range(1, 4)]?
# A. [1,2,3] B. [1,4,9] C. [2,4,6] D. [1,4,6]
# Answer: B. [1, 4, 9]

# 4. Which function applies a function to each iterable item?
# A. filter() B. reduce() C. map() D. zip()
# Answer: C. map()

# 5. Which keyword defines a CTE?
# A. VIEW B. WITH C. HAVING D. INDEX
# Answer: B. WITH

# 6. Which window function gives each row a unique sequential number?
# A. RANK() B. DENSE_RANK() C. ROW_NUMBER() D. AVG()
# Answer: C. ROW_NUMBER()

# 7. Which JOIN returns every possible row combination?
# A. INNER B. LEFT C. CROSS D. RIGHT
# Answer: C. CROSS

# 8. In a variable-size sliding window, what is commonly moved when its
# condition is violated?
# A. Left pointer B. Array size C. Middle element D. Recursion stack
# Answer: A. Left pointer

# 9. Which Python structure is commonly used for frequency counts?
# A. Tuple B. Dictionary C. String D. Float
# Answer: B. Dictionary

# 10. In two pointers on a sorted array, if sum is below target, generally move:
# A. Right pointer left B. Left pointer right C. Both left D. Neither
# Answer: B. Left pointer right
# Moving the left pointer right can increase the sum in ascending order.

# =============================================================================
# SECTION B - PYTHON PROGRAMMING (2 x 4 = 8 Marks)
# =============================================================================

# 11. Create a Student class with private name and marks, constructor,
# getter/setter methods, and a display method. Create and use an object.
# -----------------------------------------------------------------------------
# Answer:
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

student = Student("Aman", 85)
student.display()
student.set_name("Aman Kumar")
student.set_marks(92)
print("Name using getter:", student.get_name())
print("Marks using getter:", student.get_marks())
student.display()

# Output:
# Name: Aman
# Marks: 85
# Name using getter: Aman Kumar
# Marks using getter: 92
# Name: Aman Kumar
# Marks: 92
# Note: Double underscores use name mangling, not strict access enforcement.

# 12. Read students.txt, count lines and words, and handle a missing file
# using exception handling.
# -----------------------------------------------------------------------------
# Answer:
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("Total lines:", len(content.splitlines()))
    print("Total words:", len(content.split()))
except FileNotFoundError:
    print("Error: students.txt was not found.")

# Example file content (two lines):
# Aman 85
# Neha 90
# Expected output for this example:
# Total lines: 2
# Total words: 4

# =============================================================================
# SECTION C - SQL (3 x 4 = 12 Marks)
# =============================================================================
# Tables:
# students(student_id PK, student_name, city, course_id FK);
# courses(course_id PK, course_name, course_fee);
# results(result_id PK, student_id FK, subject, marks).

# 13. Multiple-table JOIN: Display student name, city, course name, subject
# and marks by joining all three tables. Include students who have not yet
# received a result, wherever applicable.
# -----------------------------------------------------------------------------
# Answer:
query_13 = """
SELECT s.student_name, s.city, c.course_name, r.subject, r.marks
FROM students AS s
LEFT JOIN courses AS c ON s.course_id = c.course_id
LEFT JOIN results AS r ON s.student_id = r.student_id;
"""

# LEFT JOIN preserves students without results; their result columns are NULL.

# 14. JOIN + Aggregates: Display course name, total students enrolled and
# average marks per course. Show only courses with average marks above 70.
# Use JOIN, COUNT(), AVG(), GROUP BY and HAVING.
# -----------------------------------------------------------------------------
# Answer:
query_14 = """
SELECT c.course_name,
       COUNT(DISTINCT s.student_id) AS total_students,
       AVG(r.marks) AS average_marks
FROM courses AS c
LEFT JOIN students AS s ON c.course_id = s.course_id
LEFT JOIN results AS r ON s.student_id = r.student_id
GROUP BY c.course_id, c.course_name
HAVING AVG(r.marks) > 70;
"""

# DISTINCT avoids counting a student once per subject result.
# LEFT JOIN counts enrolled students even if they have no results.
# AVG ignores NULL and averages available result marks for the course.

# 15. CTE + Window Function: Using a CTE, calculate each student's average
# marks across subjects. Display student name, average marks and rank within
# their course by average marks descending, using PARTITION BY.
# -----------------------------------------------------------------------------
# Answer:
query_15 = """
WITH StudentAverage AS (
    SELECT s.student_id, s.student_name, s.course_id,
           AVG(r.marks) AS average_marks
    FROM students AS s
    JOIN results AS r ON s.student_id = r.student_id
    GROUP BY s.student_id, s.student_name, s.course_id
    HAVING COUNT(r.marks) > 0
)
SELECT student_name, average_marks,
       RANK() OVER (
           PARTITION BY course_id
           ORDER BY average_marks DESC
       ) AS course_rank
FROM StudentAverage
ORDER BY course_id, course_rank, student_id;
"""

# Students with no available marks are excluded from the ranking.
# Equal averages receive the same rank; the following rank may have a gap.

# =============================================================================
# SECTION D - DSA / PROBLEM SOLVING (5 x 4 = 20 Marks)
# =============================================================================

# 16. Pattern Recognition: For [2, 4, 6, 8, 10, 12], identify the pattern and
# write a function checking whether a sequence has a constant difference.
# Return True or False.
# -----------------------------------------------------------------------------
# Answer: An arithmetic sequence with a constant difference of 2.
def has_constant_difference(sequence):
    if len(sequence) < 2:
        return True
    difference = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != difference:
            return False
    return True

print(has_constant_difference([2, 4, 6, 8, 10, 12]))
print(has_constant_difference([2, 4, 7]))

# Output:
# True
# False
# Time: O(n). Auxiliary space: O(1).

# 17. Sliding Window: For [2, 1, 5, 1, 3, 2], window size 3, find the maximum
# sum of a contiguous subarray. Show each window sum.
# -----------------------------------------------------------------------------
# Answer:
numbers = [2, 1, 5, 1, 3, 2]
k = 3
window_sum = sum(numbers[i] for i in range(k))
maximum = window_sum
print("Window 1 sum:", window_sum)
for right in range(k, len(numbers)):
    window_sum += numbers[right] - numbers[right - k]
    print(f"Window {right - k + 2} sum:", window_sum)
    maximum = max(maximum, window_sum)
print("Maximum sum:", maximum)

# Windows and sums:
# [2, 1, 5] -> 8
# [1, 5, 1] -> 7
# [5, 1, 3] -> 9
# [1, 3, 2] -> 6
# Maximum sum: 9
# Time: O(n). Auxiliary space: O(1).

# 18. Two Pointers + Hashing: For sorted array [1, 2, 4, 6, 8, 9] and target
# 10, find a pair using two pointers and state complexity. Briefly explain
# how a set/dictionary can solve pair-sum for an unsorted array.
# -----------------------------------------------------------------------------
# Answer:
def pair_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return numbers[left], numbers[right]
        if total < target:
            left += 1
        else:
            right -= 1
    return None

print(pair_sum_sorted([1, 2, 4, 6, 8, 9], 10))

# Output: (1, 9)
# Other valid pairs: (2, 8) and (4, 6).
# Two pointers: O(n) time and O(1) auxiliary space.
#
# For an unsorted array, store previously seen values in a set. For each
# number, check whether target - number was seen before adding the number.
# This ensures two different array positions are used.
def pair_sum_unsorted(numbers, target):
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return complement, number
        seen.add(number)
    return None

print(pair_sum_unsorted([4, 9, 2, 6, 1, 8], 10))

# Output: (4, 6)
# Hashing: O(n) expected time and O(n) auxiliary space.

# 19. Hashing - Frequency Count: For [4, 2, 4, 3, 2, 4, 1], write a Python
# function using a dictionary to count each number's frequency. Display the
# most frequent number and its frequency.
# -----------------------------------------------------------------------------
# Answer:
def count_frequencies(numbers):
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
    return frequencies

frequencies = count_frequencies([4, 2, 4, 3, 2, 4, 1])
print("Frequencies:", frequencies)
if frequencies:
    most_frequent = max(frequencies, key=frequencies.get)
    print("Most frequent number:", most_frequent)
    print("Frequency:", frequencies[most_frequent])
else:
    print("No numbers provided.")

# Output:
# Frequencies: {4: 3, 2: 2, 3: 1, 1: 1}
# Most frequent number: 4
# Frequency: 3
# Expected time: O(n). Auxiliary space: O(u), where u is unique values.

# 20. Sliding Window - Maximum Sum: For [3, 1, 4, 2, 5, 1, 6] and window
# size 3, find the maximum contiguous window sum using sliding window.
# State the time complexity.
# -----------------------------------------------------------------------------
# Answer:
def maximum_window_sum(numbers, k):
    if not 1 <= k <= len(numbers):
        raise ValueError("Window size must be between 1 and array length.")
    window_sum = sum(numbers[i] for i in range(k))
    maximum = window_sum
    for right in range(k, len(numbers)):
        window_sum += numbers[right] - numbers[right - k]
        maximum = max(maximum, window_sum)
    return maximum

print(maximum_window_sum([3, 1, 4, 2, 5, 1, 6], 3))

# Output: 12
# Windows and sums:
# [3, 1, 4] -> 8
# [1, 4, 2] -> 7
# [4, 2, 5] -> 11
# [2, 5, 1] -> 8
# [5, 1, 6] -> 12
# Maximum window: [5, 1, 6]. Maximum sum: 12.
# Time: O(n). Auxiliary space: O(1).

# =============================================================================
#                            END OF ASSESSMENT
# =============================================================================

