# [Floor, Ceil and Rint][title]

## Description

floor
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i  where i<=x .

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
```

ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i>=x .

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
```

rint
The rint tool rounds to the nearest integer of input element-wise.

```python
import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```

Task
You are given a 1-D array, A . Your task is to print the floor , ceil and rint of all the elements of A .
Note
In order to get the correct output format, add the line
np.set_printoptions(legacy="1.13") below the numpy import.

Input Format
A single line of input containing the space separated elements of array A .
Output Format
On the first line, print the floor of A.
On the second line, print the ceil of A.
On the third line, print the rint of A.
Sample Input
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

**Tags:** Numpy

##

[Problem-Solving-HackerRank][ajl]

[title]: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
[ajl]: https://github.com/yossef-seyam/Problem-Solving-HackerRank
