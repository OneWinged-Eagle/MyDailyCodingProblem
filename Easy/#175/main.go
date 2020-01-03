package main

/*
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
*/

import (
	"fmt"
	"math/rand"
)

type link struct {
	start rune
	end   rune
	p     float64
}

type probability struct {
	p   float64
	end rune
}

func next(probabilities []probability) rune {
	r := rand.Float64()

	for _, probability := range probabilities {
		if probability.p > r {
			return probability.end
		}
	}

	return -1
}

func getProbabilities(chain []link) (probabilities map[rune][]probability) {
	probabilities = make(map[rune][]probability)

	for _, l := range chain {
		lastP := 0.0

		if probs, ok := probabilities[l.start]; ok {
			lastP = probs[len(probs)-1].p
		}

		probabilities[l.start] = append(probabilities[l.start], probability{l.p + lastP, l.end})
	}

	return
}

func runChain(start rune, steps int, chain []link) (visits map[rune]int) {
	visits = make(map[rune]int)

	probabilities := getProbabilities(chain)

	curr := start
	for i := 0; i < steps; i++ {
		curr = next(probabilities[curr])
		visits[curr]++
	}

	return
}

func main() {
	chain := []link{
		link{'a', 'a', 0.9},
		link{'a', 'b', 0.075},
		link{'a', 'c', 0.025},

		link{'b', 'a', 0.15},
		link{'b', 'b', 0.8},
		link{'b', 'c', 0.05},

		link{'c', 'a', 0.25},
		link{'c', 'b', 0.25},
		link{'c', 'c', 0.5},
	}

	fmt.Println("chain =", chain)
	for i := 0; i < 10; i++ {
		fmt.Printf("runChain(chain) = %v\n", runChain('a', 5000, chain))
	}
}
