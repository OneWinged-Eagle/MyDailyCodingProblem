package main

/*
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
*/

import "fmt"

type SOE struct {
	primes    []int
	nextPrime int
}

func newSOE() *SOE {
	return &SOE{make([]int, 0), 2}
}

func (soe *SOE) next() (prime int) {
	prime = soe.nextPrime

	soe.primes = append(soe.primes, prime)

	for true {
		soe.nextPrime++

		divisible := false
		for _, p := range soe.primes {
			if soe.nextPrime%p == 0 {
				divisible = true
				break
			}
		}

		if !divisible {
			break
		}
	}

	return
}

func main() {
	sieveOfEratosthenes := newSOE()

	for i := 0; i <= 42; i++ {
		fmt.Println("sieveOfEratosthenes.next() = ", sieveOfEratosthenes.next())
	}
}
