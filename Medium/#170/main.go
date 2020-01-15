package main

/*
Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat.
*/

import "fmt"

type queue []string

func (q *queue) enqueue(v string) {
	*q = append(*q, v)
}

func (q *queue) dequeue() string {
	res := (*q)[0]
	*q = (*q)[1:]
	return res
}

type void struct{}
type set map[string]void

func newSet(strings []string) (s set) {
	s = make(set, len(strings))
	for _, str := range strings {
		s.add(str)
	}

	return
}

func (s set) has(str string) bool {
	_, ok := s[str]
	return ok
}

func (s *set) add(str string) {
	if !s.has(str) {
		(*s)[str] = void{}
	}
}

func (s *set) del(str string) {
	if s.has(str) {
		delete(*s, str)
	}
}

func oneStep(str1, str2 string) (match bool) {
	if len(str1) != len(str2) {
		return
	}

	for i := 0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			if match {
				return false
			}
			match = true
		}
	}

	return
}

type graph map[string]set

func newGraph(dictionary set) (g graph) {
	g = make(map[string]set, len(dictionary))

	for w1 := range dictionary {
		var words []string

		for w2 := range dictionary {
			if w1 == w2 {
				continue
			}

			if oneStep(w1, w2) {
				words = append(words, w2)
			}
		}

		if len(words) > 0 {
			g[w1] = newSet(words)
		}
	}
	return
}

func (g graph) has(key string) bool {
	_, ok := g[key]
	return ok
}

func (g graph) keys() []string {
	k := make([]string, len(g))

	i := 0
	for key := range g {
		k[i] = key
		i++
	}

	return k
}

func (g graph) shortest(start, end string) (path []string) {
	if !g.has(start) || !g.has(end) {
		return nil
	}

	nextToStart, todo := make(map[string]string, len(g)), newSet(g.keys())
	var q queue
	q.enqueue(start)
	todo.del(start)

	for len(q) > 0 {
		curr := q.dequeue()

		for word := range todo {
			if g[curr].has(word) {
				nextToStart[word] = curr
				todo.del(word)
				q.enqueue(word)
			}
		}
	}

	curr := end
	for curr != start {
		if next, ok := nextToStart[curr]; ok {
			path = append([]string{curr}, path...)
			curr = next
		} else {
			return nil
		}
	}

	return append([]string{curr}, path...)
}

func transformation(start, end string, dictionary set) []string {
	if !dictionary.has(end) {
		return nil
	}
	dictionary.add(start)

	g := newGraph(dictionary)

	return g.shortest(start, end)
}

func main() {
	fmt.Println("transformation(dog, cat, {dot, dop, dat, cat}) =", transformation("dog", "cat", newSet([]string{"dot", "dop", "dat", "cat"})))
	fmt.Println("transformation(dog, cat, {dot, tod, dat, dar}) =", transformation("dog", "cat", newSet([]string{"dot", "tod", "dat", "dar"})))
	fmt.Println("transformation(TOON, PLEA, {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}) =", transformation("TOON", "PLEA", newSet([]string{"POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"})))
}
