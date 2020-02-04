package main

/*
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
*/

import (
	"fmt"
	"strconv"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func myAtoi(s string) int {
	nb, err := strconv.Atoi(s)
	check(err)
	return nb
}

func helper(address, prefix string, nb int) (addresses []string) {
	if nb == 0 {
		return append(addresses, prefix[:len(prefix)-1])
	}

	if len(address) < nb || len(address) > nb*3 {
		return
	}
	nb--

	one := myAtoi(address[0:1])
	if len(address)-1 <= nb*3 && one >= 0 && one <= 9 {
		addresses = append(addresses, helper(address[1:], prefix+address[0:1]+".", nb)...)
	}

	if len(address) > 1 {
		two := myAtoi(address[0:2])
		if len(address)-2 >= nb && len(address)-2 <= nb*3 && two >= 10 && two <= 99 {
			addresses = append(addresses, helper(address[2:], prefix+address[0:2]+".", nb)...)
		}
	}

	if len(address) > 2 {
		three := myAtoi(address[0:3])
		if len(address)-3 >= nb && three >= 100 && three <= 255 {
			addresses = append(addresses, helper(address[3:], prefix+address[0:3]+".", nb)...)
		}
	}

	return
}

func ipAddresses(address string) []string {
	return helper(address, "", 4)
}

func main() {
	address := "2542540123"
	for len(address) > 0 {
		fmt.Printf("ipAddresses(%s) = %s\n", address, ipAddresses(address))
		address = address[0 : len(address)-1]
	}
}
