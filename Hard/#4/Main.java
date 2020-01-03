
/*
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/

public class Main {
	static int sort(int[] numbers) {
		int end = 0;
		for (int i = 0; i < numbers.length; i++) {
			if (numbers[i] > 0) {
				int temp = numbers[end];
				numbers[end++] = numbers[i];
				numbers[i] = temp;
			}
		}
		return end;
	}

	static int missingInteger(int[] numbers) {
		int end = sort(numbers);

		for (int i = 0; i < end; i++) {
			int abs = Math.abs(numbers[i]);
			if (abs <= end && numbers[abs - 1] > 0) {
				numbers[abs - 1] = -numbers[abs - 1];
			}
		}

		for (int i = 0; i < end; i++) {
			if (numbers[i] > 0) {
				return i + 1;
			}
		}

		return end + 1;
	}

	public static void main(String[] args) {
		System.out.printf("missingInteger([1, 2, 3, 4, 5]) = %d%n", missingInteger(new int[] { 1, 2, 3, 4, 5 }));
		System.out.printf("missingInteger([3, -2, 1]) = %d%n", missingInteger(new int[] { 3, -2, 1 }));
		System.out.printf("missingInteger([1, 2, 0, 4, 5]) = %d%n", missingInteger(new int[] { 1, 2, 0, 4, 5 }));
		System.out.printf("missingInteger([1, 0, 3, 0, 5]) = %d%n", missingInteger(new int[] { 1, 0, 3, 0, 5 }));
		System.out.printf("missingInteger([66, 420, 33, 1, 1337]) = %d%n",
				missingInteger(new int[] { 66, 420, 33, 1, 1337 }));
	}
}
