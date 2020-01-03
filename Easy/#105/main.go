package main

/*
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.
*/

import (
	"fmt"
	"time"
)

func print() {
	fmt.Println("Finally!")
}

func debounced(f func(), n int) func() {
	var timer *time.Timer
	duration := time.Duration(n) * time.Millisecond

	return func() {
		if timer == nil {
			timer = time.NewTimer(duration)

			go func() {
				<-timer.C
				timer.Stop()
				timer = nil
				f()
			}()
		} else {
			timer.Reset(duration)
		}
	}
}

func main() {
	fmt.Printf("Current Unix Time: %v\n", time.Now().Unix())

	debouncer := debounced(print, 1000)

	debouncer()
	time.Sleep(time.Duration(500) * time.Millisecond)
	debouncer()
	time.Sleep(time.Duration(500) * time.Millisecond)
	debouncer()

	time.Sleep(time.Duration(1001) * time.Millisecond)

	fmt.Printf("Current Unix Time: %v\n", time.Now().Unix())
}
