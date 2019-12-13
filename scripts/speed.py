import os
import json
import time
import random
import argparse
from typing import List, Callable, Any
import numpy as np
from scipy.spatial.distance import cdist
from pairwise_manhattan import (
    pairwise_manhattan_python_v1,
    pairwise_manhattan_python_v2,
    pairwise_manhattan_numpy_v1,
    pairwise_manhattan_numpy_v2,
    pairwise_manhattan_numpy_v3,
    pairwise_manhattan_numpy_v4,
)
from pairwise_manhattan_cython import (
    pairwise_manhattan as pairwise_manhattan_cython,
    pairwise_manhattan_parallel as pairwise_manhattan_cython_p,
)


def speed_test(func: Callable, in_: Any, trials: int) -> List[float]:
    times = []
    for _ in range(trials):
        tic = time.time()
        func(in_)
        elapsed = time.time() - tic
        times.append(elapsed)
    return times


def speed_test_scipy(in_: Any, trials: int) -> List[float]:
    times = []
    for _ in range(trials):
        tic = time.time()
        cdist(in_, in_, "cityblock")
        elapsed = time.time() - tic
        times.append(elapsed)
    return times


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", default=10, type=int)
    parser.add_argument("--dims", default=2, type=int)
    parser.add_argument("--trials", default=5, type=int)
    parser.add_argument("--acc", default=".speed")
    args = parser.parse_args()

    data = [[random.randint(-100, 100) for _ in range(args.dims)] for _ in range(args.points)]

    timings = {}

    timings["python_brute"] = speed_test(pairwise_manhattan_python_v1, data, args.trials)
    timings["python_cached"] = speed_test(pairwise_manhattan_python_v2, data, args.trials)
    timings["numpy_brute"] = speed_test(
        pairwise_manhattan_numpy_v1, [np.array(d, np.float32) for d in data], args.trials
    )
    timings["numpy_cached"] = speed_test(
        pairwise_manhattan_numpy_v2, [np.array(d, dtype=np.int32) for d in data], args.trials
    )
    timings["numpy_broadcast"] = speed_test(pairwise_manhattan_numpy_v3, np.array(data, np.int32), args.trials)
    timings["numpy_double_broadcast"] = speed_test(pairwise_manhattan_numpy_v3, np.array(data, np.int32), args.trials)
    timings["scipy"] = speed_test_scipy(np.array(data, dtype=np.int32), args.trials)
    timings["cython"] = speed_test(pairwise_manhattan_cython, np.array(data, dtype=np.int32), args.trials)
    timings["cython_parallel"] = speed_test(pairwise_manhattan_cython_p, np.array(data, dtype=np.int32), args.trials)

    os.makedirs(args.acc, exist_ok=True)

    with open(os.path.join(args.acc, f"points-{args.points}-dims-{args.dims}.json"), "w") as f:
        json.dump(timings, f, indent=2)


if __name__ == "__main__":
    main()
