"""
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

from typing import Dict, List


# time O(n²), space O(n), delete every elements of coursesIds
def courses(coursesIds: Dict[str, List[str]]) -> List[str]:
	courses = []

	while len(coursesIds) > 0:
		found = [
		    courseId for courseId, courseIds in coursesIds.items()
		    if all(cId in courses for cId in courseIds)
		]

		if len(found) > 0:
			for courseId in found:
				del coursesIds[courseId]

			courses += found
		else:
			return None

	return courses


coursesIds = {
    "CSC300": ["CSC100", "CSC200"],
    "CSC200": ["CSC100"],
    "CSC100": []
}
print(f"courses({coursesIds}) = {courses(coursesIds)}")

coursesIds = {"first": [], "second": [], "third": []}
print(f"courses({coursesIds}) = {courses(coursesIds)}")

coursesIds = {
    "third": ["first", "second"],
    "fourth": ["second"],
    "second": ["first"],
    "first": []
}
print(f"courses({coursesIds}) = {courses(coursesIds)}")

coursesIds = {
    "third": ["first", "second"],
    "fourth": ["second"],
    "second": ["first"],
    "first": ["fourth"]
}
print(f"courses({coursesIds}) = {courses(coursesIds)}")

coursesIds = {
    "fourth": ["first", "second", "third"],
    "third": ["first", "second"],
    "second": ["first"],
    "first": []
}
print(f"courses({coursesIds}) = {courses(coursesIds)}")
