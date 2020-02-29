package main

import "sort"

type SortedMap struct {
	m    map[int]int
	keys []int
}

func newSortedMap() *SortedMap {
	return &SortedMap{make(map[int]int), make([]int, 0)}
}

func (sm *SortedMap) set(key, val int) {
	if i := sort.SearchInts(sm.keys, key); i == len(sm.keys) || sm.keys[i] != key {
		sm.keys = append(sm.keys, 0)
		copy(sm.keys[i+1:], sm.keys[i:])
		sm.keys[i] = key
	}

	sm.m[key] = val
}

func (sm SortedMap) get(key, defaultVal int) int {
	if val, ok := sm.m[key]; ok {
		return val
	}

	return defaultVal
}
