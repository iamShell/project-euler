// Smallest multiple
// Problem 5
//
// 2520 is the smallest number that can be divided by each of the numbers
// from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all
// of the numbers from 1 to 20?

package main

import (
	"fmt"
)

func main() {
	//	var x int64 = 20
	//	divisible := false
	//	for ; !divisible; x += 20 {
	//		if (x%11 == 0) && (x%12 == 0) && (x%13 == 0) && (x%14 == 0) && (x%15 == 0) && (x%16 == 0) && (x%17 == 0) && (x%18 == 0) && (x%19 == 0) && (x%20 == 0) {
	//			fmt.Printf("%d\n", x)
	//			divisible = true
	//		}
	//	}
	x, count := 20, 0
	divisible := false
	for ; !divisible; x += 10 {
		count++
		//		if (x%1 == 0) && (x%2 == 0) && (x%3 == 0) && (x%4 == 0) && (x%5 == 0) && (x%6 == 0) && (x%7 == 0) && (x%8 == 0) && (x%9 == 0) && (x%10 == 0) {
		fmt.Println(count)
		if x%count == 0 {
			fmt.Println(x)
			if count == 2520 {
				divisible = true
			}
		}
	}

}
