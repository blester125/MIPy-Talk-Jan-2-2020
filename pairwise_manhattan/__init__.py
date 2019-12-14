__version__ = "0.1.0"


from pairwise_manhattan.pairwise_manhattan import (
    pairwise_manhattan_python_v1,
    pairwise_manhattan_python_v2,
    pairwise_manhattan_numpy_v1,
    pairwise_manhattan_numpy_v2,
    pairwise_manhattan_numpy_v3,
    pairwise_manhattan_numpy_v4,
)

from pairwise_manhattan.pairwise_manhattan_cython import (
    pairwise_manhattan as pairwise_manhattan_cython,
    pairwise_manhattan_parallel as pairwise_manhattan_cython_p,
)
