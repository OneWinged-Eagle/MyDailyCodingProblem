/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/

import java.util.HashSet;

public class Main {
	static boolean addUpTo(int[] numbers, int K) {
		HashSet<Integer> hash = new HashSet<Integer>();

		for (int nb : numbers) {
			if (hash.contains(K - nb)) {
				return true;
			}
			hash.add(nb);
		}

		return false;
	}

	public static void main(String[] args) {
		System.out.printf("addUpTo([10, 15, 3, 7], 17) = %b%n", addUpTo(new int[] { 10, 15, 3, 7 }, 17));

		System.out.printf("addUpTo([10, 15, 3, 7], 16) = %b%n", addUpTo(new int[] { 10, 15, 3, 7 }, 16));

		System.out.printf("addUpTo([10, 15, 3, 7, 20, -3], 17) = %b%n", addUpTo(new int[] { 10, 15, 3, 7, 20, -3 }, 17));

		System.out.printf("addUpTo([10, 15, 3, 7, 20, -3], 20) = %b%n", addUpTo(new int[] { 10, 15, 3, 7, 20, -3 }, 20));
	}
}
