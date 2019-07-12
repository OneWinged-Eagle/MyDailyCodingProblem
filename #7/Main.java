
/*
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
*/

import java.util.Hashtable;

public class Main {
	static Hashtable<String, Integer> cache = new Hashtable<String, Integer>();

	static int nb_ways(String encoded) {
		if (encoded.length() == 0) {
			return 1;
		} else if (encoded.charAt(0) == '0') {
			return 0;
		} else if (cache.containsKey(encoded)) {
			return cache.get(encoded);
		}

		int ways = nb_ways(encoded.substring(1));

		if (encoded.length() >= 2 && 10 <= Integer.parseInt(encoded.substring(0, 2))
				&& Integer.parseInt(encoded.substring(0, 2)) <= 26) {
			ways += nb_ways(encoded.substring(2));
		}

		cache.put(encoded, ways);
		return ways;
	}

	public static void main(String[] args) {
		System.out.printf("nb_ways('111') = %d%n", nb_ways("111"));
		System.out.printf("nb_ways('262026') = %d%n", nb_ways("262026"));
		System.out.printf("nb_ways('262126') = %d%n", nb_ways("262126"));
		System.out.printf("nb_ways('362136') = %d%n", nb_ways("362136"));
		System.out.printf("nb_ways('362136362136') = %d%n", nb_ways("362136362136"));
		System.out.printf("nb_ways('362136362136362136') = %d%n", nb_ways("362136362136362136"));
		System.out.printf("nb_ways('362936362936362936') = %d%n", nb_ways("362936362936362936"));
		System.out.printf("nb_ways('1111') = %d%n", nb_ways("1111"));
		System.out.printf("nb_ways('2222') = %d%n", nb_ways("2222"));
		System.out.printf("nb_ways('123450123541023541201') = %d%n", nb_ways("123450123541023541201"));
		System.out.printf("nb_ways('12345201235410235412010') = %d%n", nb_ways("12345201235410235412010"));
		System.out.printf("%s%n", cache);
	}
}
