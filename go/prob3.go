// Largest prime factor
// Problem 3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?

package main

import "fmt"

func main() {
	var n int = 20
	var i int = 2
	for i*i <= n {
		if i*i == n {
			n := i
			break
		}
		for n%i == 0 {
			n := n / i
		}
		i += 1
		fmt.Println(n, i)
	}
	fmt.Println(n, i)
}
