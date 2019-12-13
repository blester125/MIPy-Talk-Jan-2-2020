import random
from itertools import combinations
import pytest
import numpy as np

from pairwise_manhattan import (
    pairwise_manhattan_python_v1,
    pairwise_manhattan_python_v2,
    pairwise_manhattan_numpy_v1,
    pairwise_manhattan_numpy_v2,
    pairwise_manhattan_numpy_v3,
    pairwise_manhattan_numpy_v4,
)
from pairwise_manhattan_cython import pairwise_manhattan_cython


CENTERS = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
]

DISTS = [[0, 1, 2, 1], [1, 0, 1, 2], [2, 1, 0, 1], [1, 2, 1, 0]]


@pytest.fixture
def points():
    points, dims = random.randint(1, 100), random.randint(2, 100)
    return [[random.randint(-100, 100) for _ in range(dims)] for _ in range(points)]


def test_pairwise_manhattan():
    res = pairwise_manhattan_python_v1(CENTERS)
    assert res == gold


def test_pairwise_manhattan_zeros_on_diag(points):
    dists = pairwise_manhattan_python_v1(points)
    for i in range(len(dists)):
        assert dists[i][i] == 0


def test_pairwise_manhattan_symmetric(points):
    dists = pairwise_manhattan_python_v1(points)
    for i in range(len(dists)):
        for j in range(len(dists)):
            assert dists[i][j] == dist[j][i]


def test_pairwise_manhattan_all_equal(points):
    results = []
    results.append(pairwise_manhattan_python_v1(points))
    results.append(pairwise_manhattan_python_v2(points))
    points = [np.array(p, dtype=np.int32) for p in points]
    results.append(pairwise_manhattan_numpy_v1(points))
    results.append(pairwise_manhattan_numpy_v2(points))
    points = np.stack(points)
    results.append(pairwise_manhattan_numpy_v3(points))
    results.append(pairwise_manhattan_numpy_v4(points))
    results = [np.array(r, dtype=np.int32) for r in results]
    for i, j in combinations(results, 2):
        np.testing.assert_equal(i, j)
