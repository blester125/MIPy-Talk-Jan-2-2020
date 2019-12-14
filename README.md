# Pairwise Manhattan Distance For MIPy talk

This is the code and slides from my talk at the Michigan Python Meetup on January 2nd 2019.

## Install

Normally I would suggest installing via `setup.py` but doing this makes it difficult to install an optimized version of NumPy. Using conda will bundle Intel MKL with it which really help you get the best performance from your numpy code.

```
conda install --file requirements.txt
```

Once you have the requirements installed you can install this package to make it accessible in scripts.

```
pip install -e .
```


## Implementations


