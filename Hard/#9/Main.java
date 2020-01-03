/*
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
*/

public class Main {
	static int maxNonAdjSum(int[] numbers) {
		if (numbers.length == 0) {
			return 0;
		} else if (numbers.length == 1) {
			return numbers[0];
		}

		int sumWithPrev = numbers[1], sumWithoutPrev = numbers[0];

		for (int i = 2; i < numbers.length; i++) {
			int tmp = Math.max(sumWithPrev, sumWithoutPrev);
			sumWithPrev = sumWithoutPrev + numbers[i];
			sumWithoutPrev = tmp;
		}

		return Math.max(sumWithPrev, sumWithoutPrev);
	}

	public static void main(String[] args) {
		System.out.printf("maxNonAdjSum([2, 4, 6, 2, 5]) = %d%n", maxNonAdjSum(new int[] { 2, 4, 6, 2, 5 }));
		System.out.printf("maxNonAdjSum([-2, -4, -6, -2, -5]) = %d%n", maxNonAdjSum(new int[] { -2, -4, -6, -2, -5 }));
		System.out.printf("maxNonAdjSum([2, 4, -6, 2, 5]) = %d%n", maxNonAdjSum(new int[] { 2, 4, -6, 2, 5 }));
		System.out.printf("maxNonAdjSum([5, 1, 1, 5]) = %d%n", maxNonAdjSum(new int[] { 5, 1, 1, 5 }));
		System.out.printf("maxNonAdjSum([-5, -1, -1, -5]) = %d%n", maxNonAdjSum(new int[] { -5, -1, -1, -5 }));
		System.out.printf("maxNonAdjSum([-5, 1, -1, 5]) = %d%n", maxNonAdjSum(new int[] { -5, 1, -1, 5 }));
	}
}
