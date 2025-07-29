# [Min and Max][title]

## Description

min
The tool min returns the minimum value along a given axis.
```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
```
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.
max
The tool max returns the maximum value along a given axis.
```python
import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
```
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

Task
You are given a 2-D array with dimensions X.
Your task is to perform the min function over axis  and then find the max of that.
Input Format
The first line of input contains the space separated values of  and .
The next  lines contains  space separated integers.
Output Format
Compute the min along axis  and then print the max of that result.
Sample Input
4 2
2 5
3 7
1 3
4 0

Sample Output
3

Explanation
The min along axis  = 
The max of  =

**Tags:** Numpy

##
[Problem-Solving-HackerRank][ajl]

[title]: https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
[ajl]: https://github.com/yossef-seyam/Problem-Solving-HackerRank