package main

/*
Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
*/

import "fmt"

func copy(m map[string]int) (cp map[string]int) {
	cp = make(map[string]int)

	for k, v := range m {
		cp[k] = v
	}

	return
}

func helper(s string, words map[string]int, lenWord, nbWords int) bool {
	for i := 0; i < len(s); i += lenWord {
		word := s[i : i+lenWord]

		if nb, ok := words[word]; ok {
			if nb <= 0 {
				return false
			}

			words[word]--
			nbWords--
		} else {
			return false
		}
	}

	if nbWords == 0 {
		return true
	}

	return false
}

func getIndices(s string, words []string) (indices []int) {
	nbWords := len(words)
	if nbWords < 0 {
		return
	}

	lenWord := len(words[0])
	wordsMap := make(map[string]int)

	for _, word := range words {
		if len(word) != lenWord {
			return
		}

		if _, ok := wordsMap[word]; ok {
			wordsMap[word]++
		} else {
			wordsMap[word] = 1
		}
	}

	lenWords := nbWords * lenWord

	if lenWords > len(s) {
		return
	}

	for i := 0; i < len(s)-lenWords+1; i++ {
		if helper(s[i:i+lenWords], copy(wordsMap), lenWord, nbWords) {
			indices = append(indices, i)
		}
	}

	return
}

func main() {
	fmt.Printf("getIndices(\"dogcatcatcodecatdog\", [\"cat\", \"dog\"]) = %v\n", getIndices("dogcatcatcodecatdog", []string{"cat", "dog"}))
	fmt.Printf("getIndices(\"barfoobazbitbyte\", [\"dog\", \"cat\"]) = %v", getIndices("barfoobazbitbyte", []string{"dog", "cat"}))
}
