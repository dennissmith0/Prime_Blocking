# Prime Number Generation: A Primes Blocking Primes Approach

This project introduces a novel algorithm for generating prime numbers. Our approach provides an alternative to the traditional Sieve of Eratosthenes by exploiting properties of prime numbers and their multiples in an arithmetic sequence with respect to a recurring number structure, rather than the familiar number line.

## Theory

Our algorithm is based on the concept of "blocked primes", which refer to the positions where multiples of a certain prime number do appear on the left or the right of a multiple of 6. Since primes (besides 2 and 3) are only ever next to a multiple of a 6 (+ 1 or -1), we assume all these numbers "want" to be prime. They are not because previous primes occupy these positions (beginning at 25,35,49,...). 

We call these potential primes "blocked primes." Then, we can say a prime exists because a previous prime is not "blocking" that position. These blocking positions can be determined by a repeating pattern of sequence and index pairs, which allow us to eliminate multiples of prime numbers from the list of potential prime numbers up to a given limit n. We find the set of all primes up to n, and the amount of them, given the list of potential primes (all integers ± 1 a multiple of 6), minus the amount of "blocked primes" in the same range, + 2 - don't forget 2 and 3!.

We divide our investigation into two categories of primes: 

1. Primes that are one less than a multiple of six, referred to as 'LHS primes'.
2. Primes that are one more than a multiple of six, referred to as 'RHS primes'.

## Implementation

The algorithm consists of several functions that together generate a list of potential prime numbers up to a given limit.

- The `generate_blocking_positions` function generates the blocking positions for a given prime number.
- The `position_to_integer` function converts these positions back into integers.
- The algorithm ensures that the blocking positions for each prime number do not overlap with those of previous prime numbers.

The result is a list of all potential prime numbers up to a given limit, excluding multiples of the primes we have considered.

## Examples

Here is an example of running the code with the input `n = 1050`:

```python
Enter an integer (we will find all prime blocks up to this n): 1050
```

The code will produce the following output for the RHS:

```python
{7: [49, 77, 91, 119, 133, 161, 175, 203, 217, 245, 259, 287, 301, 329, 343, 371, 385, 413, 427, 455, 469, 497, 511, 539, 553, 581, 595, 623, 637, 665, 679, 707, 721, 749, 763, 791, 805, 833, 847, 875, 889, 917, 931, 959, 973, 1001, 1015, 1043, 1057], 
 13: [169, 221, 247, 299, 325, 377, 403, 455, 481, 533, 559, 611, 637, 689, 715, 767, 793, 845, 871, 923, 949, 1001, 1027], 
 19: [361, 437, 475, 551, 589, 665, 703, 779, 817, 893, 931, 1007, 1045]}
```
And the LHS:
```python
{5: [25, 35, 55, 65, 85, 95, 115, 125, 145, 155, 175, 185, 205, 215, 235, 245, 265, 275, 295, 305, 325, 335, 355, 365, 385, 395, 415, 425, 445, 455, 475, 485, 505, 515, 535, 545, 565, 575, 595, 605, 625, 635, 655, 665, 685, 695, 715, 725, 745, 755, 775, 785, 805, 815, 835, 845, 865, 875, 895, 905, 925, 935, 955, 965, 985, 995, 1015, 1025, 1045, 1055],
11: [121, 143, 187, 209, 253, 275, 319, 341, 385, 407, 451, 473, 517, 539, 583, 605, 649, 671, 715, 737, 781, 803, 847, 869, 913, 935, 979, 1001, 1045],
17: [289, 323, 391, 425, 493, 527, 595, 629, 697, 731, 799, 833, 901, 935, 1003, 1037],
23: [529, 575, 667, 713, 805, 851, 943, 989],
29: [841, 899, 1015]}
```

Each key represents a prime number that originates on the RHS (+ 1 a multiple of 6) and the LHS (-1 a multiple of 6), respectively. Each value associated with each key is a multiple of that prime number that we say "blocks" that integer from being prime (since they are in a potential prime position: alternating from RHS to LHS).

## Performance

The current version of the algorithm has a time complexity of O(n^2), which may not be ideal for large inputs. However, it provides a unique approach to prime number generation and demonstrates an interesting property of prime numbers.

## Future Work

The next steps for this project include optimizing the algorithm and potentially applying it to other problems in number theory. We welcome contributions and ideas from other enthusiasts and researchers.
