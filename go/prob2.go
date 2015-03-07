// Even Fibonacci numbers
// Problem 2
//
// Each new term in the Fibonacci sequence is generated by adding the previous
// two terms. By starting with 1 and 2, the first 10 terms will be:
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
// By considering the terms in the Fibonacci sequence whose values do not exceed
// four million, find the sum of the even-valued terms.

package main

import "fmt"

func main() {
	a, b, j, i := 0, 1, 0, 0
	for {
		a = a + b
		b = b + a
		if j+i > 4000000 {
			fmt.Println(j + i)
			break
		} else if a%2 == 0 {
			i += a
		} else if b%2 == 0 {
			j += b
		}
	}
}
