# cython: language_level=3

# cython tries to transparently select the abs function including the python
# one with the data type isn't an int. This import forces it to use the C
# version which we can use without the gil
from libc.stdlib cimport abs
cimport cython
from cython.parallel cimport prange
import numpy as np

@cython.wraparound(False)
@cython.boundscheck(False)
cpdef int[:, :] pairwise_manhattan(int[:, :] points):
    cdef int n = points.shape[0]
    cdef int m = points.shape[1]
    results = np.zeros((n, n), dtype=np.int32)
    cdef int[:, :] results_view = results
    cdef int i, j, k, dist
    for i in range(n):
        for j in range(i, n):
            dist = 0
            for k in range(m):
                dist += abs(points[i, k] - points[j, k])
            results_view[i, j] = dist
            results_view[j, i] = dist
    return results


@cython.wraparound(False)
@cython.boundscheck(False)
cpdef pairwise_manhattan_parallel(int[:, :] points):
    cdef int n = points.shape[0]
    cdef int m = points.shape[1]
    results = np.zeros((n, n), dtype=np.int32)
    cdef int[:, :] results_view = results
    cdef int i, j, k, dist
    for i in prange(n, nogil=True, schedule='guided'):
        for j in range(1, n):
            dist = 0
            for k in range(m):
                # We use x = x + y instead of x += y because with the
                # latter x is interpreted as a reduction variable that
                # cython doesn't let us read in a loop. This keeps it
                # local
                dist = dist + abs(points[i, k] - points[j, k])
            results_view[i, j] = dist
            results_view[j, i] = dist
    return results
