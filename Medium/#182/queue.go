package main

type queue []int

func (q *queue) enqueue(v int) {
	*q = append(*q, v)
}

func (q *queue) dequeue() int {
	res := (*q)[0]
	*q = (*q)[1:]
	return res
}
