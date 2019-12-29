# Pairwise Manhattan Distance For MIPy talk

[![Actions Status](https://github.com/blester125/MIPy-Talk-Jan-2-2019/workflows/Unit%20Test/badge.svg)](https://github.com/blester125/MIPy-Talk-Jan-2-2019/actions)

This is the code and [slides](https://github.com/blester125/MIPy-Talk-Jan-2-2020/blob/master/slides/slides.pdf) from my talk at the Michigan Python Meetup on January 2nd 2020.


## Install

Normally I would suggest installing via `setup.py` but doing this makes it difficult to install an optimized version of NumPy. Using conda will bundle Intel MKL with it which really help you get the best performance from your numpy code.

```
conda install --file requirements.txt
conda install --file requirements-dev.txt
```

Once you have the requirements installed you can install this package to make it accessible in scripts.

```
pip install -e .
```


## Implementations

 * `pairwise_manhattan_python_v1` The simplest implementation, it iterates through all pairs of points and calculates the distances between them. It doesn't do any optimizations such as reusing the distance calculated between point i and point j as the distance between point j and point i because manhattan distance is symmetric.
 * `pairwise_manhattan_python_v2` This is another python implementation which reuses calculations for previous points.
 * `pairwise_manhattan_numpy_v1` This is an implementation where the points are a list of numpy arrays. The manhattan distance between pairs of points is computed via numpy in a vectorized fashion.
 * `pairwise_manhattan_numpy_v2` This is like the last one but the distance calculated between pairs of points is reused for the pair in the opposite order.
 * `pairwise_manhattan_numpy_v3` This iterates over the pairs and will broadcast a single point over the rest of the points to calculate the distance between it and all other points in a single operation.
 * `pairwise_manhattan_numpy_v4` This reshapes the points into two tensors of shape `[N, 1, M]` and `[1, N, M]`. This results in both sets of points broadcasting over each other to calculate the pair wise distances in a single op.
 * `pairwise_manhattan_cython` This is a cython port of the `pairwise_manhattan_python_v2` implementation.
 * `pairwise_manhattan_cython_p` This is the previous implementation with parallelization over the iterations of points. I haven't seen huge speed gains from this, there is probably some parameters like `OPEN_MP_THREADS` and the `prange` schedule that need to be tweaked.


## Docker

You can use docker to play with implementations or rerun the speed test or graph creation code.

```
docker build -t manhattan_distance .
docker run -it manhattan_distance
```

This will drop you into a python shell with the software installed.

Use

```
docker run -it manhattan_distance /bin/bash
conda activate MIPy
```

to get a bash shell to run scripts.
