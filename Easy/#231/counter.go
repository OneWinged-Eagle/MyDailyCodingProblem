package main

type counter map[rune]int

func newCounter(str string) (c counter) {
	c = make(map[rune]int)

	for _, char := range str {
		c[char] = c.get(char) + 1
	}

	return c
}

func (c counter) has(char rune) bool {
	_, ok := c[char]
	return ok
}

func (c counter) get(char rune) int {
	if c.has(char) {
		return c[char]
	}

	return 0
}

func (c *counter) sub(char rune) {
	if c.has(char) {
		(*c)[char]--
		if (*c)[char] == 0 {
			delete(*c, char)
		}
	}
}
