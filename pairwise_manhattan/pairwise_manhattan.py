from typing import List
import numpy as np


def pairwise_manhattan_python_v1(points: List[List[int]]) -> List[List[int]]:
    results = []
    # For each pair of points
    for i in range(len(points)):
        dist_i_j = []
        for j in range(len(points)):
            # Manhattan distance
            dist_i_j.append(sum(abs(p1 - p2) for p1, p2 in zip(points[i], points[j])))
        results.append(dist_i_j)
    return results


def pairwise_manhattan_python_v1(points: List[List[int]]) -> List[List[int]]:
    results = []
    for x in points:
        dist = []
        for y in points:
            dist.append(sum(abs(x_i - y_i) for x_i, y_i in zip(x, y)))
        results.append(dist)
    return results


def pairwise_manhattan_python_v2(points: List[List[int]]) -> List[List[int]]:
    # Preallocate the results
    results = [[None] * len(points) for _ in range(len(points))]
    # Look at every pair of you and the ones after you, one before you were calculated when they looked at you
    for i in range(len(points)):
        for j in range(i, len(points)):
            # Manhattan distance calculation
            dist = sum(abs(p1 - p2) for p1, p2 in zip(points[i], points[j]))
            # Manhattan distance is symmetric so only calculate one for each pair
            results[i][j] = dist
            results[j][i] = dist
    return results


def pairwise_manhattan_numpy_v1(points: List[np.ndarray]) -> np.ndarray:
    results = np.zeros((len(points), len(points)), dtype=np.int32)
    for i in range(len(points)):
        for j in range(len(points)):
            results[i, j] = np.sum(np.abs(points[i] - points[j]))
    return results


def pairwise_manhattan_numpy_v2(points: List[np.ndarray]) -> np.ndarray:
    results = np.zeros((len(points), len(points)), dtype=np.int32)
    for i in range(len(points)):
        for j in range(i, len(points)):
            dist = np.sum(np.abs(points[i] - points[j]))
            results[i, j] = dist
            results[j, i] = dist
    return results


def pairwise_manhattan_numpy_v3(points: np.ndarray) -> np.ndarray:
    results = []
    for i in range(len(points)):
        results.append(np.sum(np.abs(points[i] - points), axis=-1))
    return np.stack(results)


def pairwise_manhattan_numpy_broadcast_cached(points: np.ndarray) -> np.ndarray:
    results = np.zeros((len(points), len(points)), dtype=np.int32)
    dists = []
    for i in range(len(points)):
        dists.append(np.sum(np.abs(points[i] - points[i:]), axis=-1))
    for i, dist in enumerate(dists):
        results[i, i:] = dist
    i_lower = np.tril_indices(len(points), -1)
    results[i_lower] = results.T[i_lower]
    return results


def pairwise_manhattan_numpy_v4(points: np.ndarray) -> np.ndarray:
    # return np.sum(np.abs(np.expand_dims(points, 1) - np.expand_dims(points, 0)), axis=-1)
    return np.sum(np.abs(points[:, None] - points), axis=-1)
