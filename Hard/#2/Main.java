
/*
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
*/

import java.util.Arrays;

public class Main {
	static int[] products(int[] numbers) {
		int[] products = new int[numbers.length];
		int prod = 1;
		int zeroIndex = -1;

		for (int i = 0; i < numbers.length; i++) {
			if (numbers[i] == 0) {
				if (zeroIndex != -1) {
					return products;
				}
				zeroIndex = i;
			} else {
				prod *= numbers[i];
			}
		}

		if (zeroIndex != -1) {
			products[zeroIndex] = prod;
		} else {
			for (int i = 0; i < numbers.length; i++) {
				products[i] = (int) (prod * Math.pow(numbers[i], -1));
			}
		}

		return products;
	}

	public static void main(String[] args) {
		System.out.printf("products([1, 2, 3, 4, 5]) = %s%n", Arrays.toString(products(new int[] { 1, 2, 3, 4, 5 })));

		System.out.printf("products([3, -2, 1]) = %s%n", Arrays.toString(products(new int[] { 3, -2, 1 })));

		System.out.printf("products([1, 2, 0, 4, 5]) = %s%n", Arrays.toString(products(new int[] { 1, 2, 0, 4, 5 })));

		System.out.printf("products([1, 0, 3, 0, 5]) = %s%n", Arrays.toString(products(new int[] { 1, 0, 3, 0, 5 })));
	}
}
