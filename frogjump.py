"""
 FrogRiverOne
Find the earliest time when a frog can jump to the other side of a river.



A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X. Leaves fall from a tree onto the surface of the river.

You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in minutes.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In minute 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

    def solution(X, A)

that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Assume that:

        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

"""

def solution(X, A):
    # write your code in Python 2.7
    l = [0] * X
    len_l = len(l)
    uncovered = X
    for pos in xrange(len(A)):
        index = A[pos]
        if l[index-1] == 0:
            l[index-1] += 1
            uncovered -= 1
        if uncovered == 0: return pos
        #print pos, index, l
    return -1