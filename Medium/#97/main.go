package main

/*
Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
*/

import (
	"fmt"
	"sort"
)

func floorSearch(array []int, elem int) int {
	if len(array) == 0 {
		return -1
	}

	tmp := array
	for half := len(tmp) / 2; half > 0; half = len(tmp) / 2 {
		if elem == tmp[half] {
			return tmp[half]
		} else if elem < tmp[half] {
			tmp = tmp[:half]
		} else {
			tmp = tmp[half:]
		}
	}

	if len(tmp) == 0 || tmp[0] > elem {
		return -1
	}

	return tmp[0]
}

type flooredMap struct {
	m    map[int]int
	keys []int
}

func newFlooredMap(key, value int) *flooredMap {
	return &flooredMap{map[int]int{key: value}, []int{key}}
}

func (fm *flooredMap) set(key, value int) {
	i := sort.SearchInts(fm.keys, key)

	if i == len(fm.keys) || fm.keys[i] != key {
		fm.keys = append(fm.keys, 0)
		copy(fm.keys[i+1:], fm.keys[i:])
		fm.keys[i] = key
	}
	fm.m[key] = value
}

func (fm flooredMap) get(key int) int {
	k := floorSearch(fm.keys, key)

	if k == -1 {
		return -1
	}

	return fm.m[k]
}

type dateMap struct {
	m map[int]*flooredMap
}

func (dm *dateMap) set(key, value, time int) {
	if fm, ok := dm.m[key]; ok {
		fm.set(time, value)
	} else {
		dm.m[key] = newFlooredMap(time, value)
	}
}

func (dm *dateMap) get(key, time int) int {
	if fm, ok := dm.m[key]; ok {
		return fm.get(time)
	}

	return -1
}

func main() {
	dm := &dateMap{make(map[int]*flooredMap)}

	dm.set(1, 1, 1)
	dm.set(1, 2, 3)
	fmt.Printf("dm.get(1, 1) = %d (should be 1)\n", dm.get(1, 1))
	fmt.Printf("dm.get(1, 4) = %d (should be 2)\n", dm.get(1, 4))

	dm.set(1, 1, 5)
	fmt.Printf("dm.get(1, 0) = %d (should be -1)\n", dm.get(1, 0))
	fmt.Printf("dm.get(1, 10) = %d (should be 1)\n", dm.get(1, 10))

	dm.set(1, 1, 0)
	dm.set(1, 2, 0)
	fmt.Printf("dm.get(1, 0) = %d (should be 2)\n", dm.get(1, 0))
}
