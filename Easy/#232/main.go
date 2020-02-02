package main

/*
Implement a PrefixMapSum class with the following methods:

    insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
    sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
*/

import "fmt"

type PrefixMapSum struct {
	*Trie
}

func newPrefixMapSum() *PrefixMapSum {
	return &PrefixMapSum{newTrie()}
}

func (pms PrefixMapSum) sum(prefix string) int {
	return pms.getSum(prefix)
}

func main() {
	pms := newPrefixMapSum()

	pms.insert("columnar", 3)
	fmt.Println("pms.sum('col') =", pms.sum("col"))
	fmt.Println("pms.sum('colu') =", pms.sum("colu"))

	pms.insert("column", 2)
	fmt.Println("pms.sum('col') =", pms.sum("col"))
	fmt.Println("pms.sum('colu') =", pms.sum("colu"))

	pms.insert("col", 4)
	fmt.Println("pms.sum('col') =", pms.sum("col"))
	fmt.Println("pms.sum('colu') =", pms.sum("colu"))
}
