<?php
/* Multiples of 3 and 5
 * Problem 1
 * 
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.// Multiples of 3 and 5
 * Problem 1
 * 
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
$sum = 0;
for ($j = 0; $j < 1000; $j++) {
    if (!($j % 3) || !($j % 5)) {
        $sum += $j;
    }
}
echo $sum;
?>
