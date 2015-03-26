// Largest palindrome product
// Problem 4
//
// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 × 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

package main

import (
	"fmt"
	"strconv"
)

func main() {
	for j := 100; j <= 1000; j++ {
		for jj := 100; jj <= 1000; jj++ {
			var val string = strconv.Itoa(j * jj)
			if val == reverse(val) {
				fmt.Println(val)
			}
		}
	}
}

func reverse(s string) string {
	n := len(s)
	runes := make([]rune, n)
	for _, rune := range s {
		n--
		runes[n] = rune
	}
	return string(runes[n:])
}
