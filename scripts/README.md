# Scripts

 * `speed.py --points p --dims d` will run all implementations for data with `p` points and `d` dimensions. Timing data will be saved into a json file in `.speed/points-p-dims-d.json` with the directory being controllable with `--acc` cli argument.
 * `speed.sh` runs the python script over a range of points and dimension sizes.
 * `agg.py` can be pointed at the directory specified by `--acc` to create a single `timing.csv`
 * `points-graph.py` can be used to create a graph where the dimensions are held constant and the points get scaled out.
 * `dims-graph.py` can be used to create a graph where the points are held constant and the digestions get scaled out.
 * `size.py` can be used to give memory requirements of different algorithms, used `--points` to set the number of points in your problem. If you are using the numpy double broadcast solution you should set the number of dimensions with `--dims`
 * `cython-jupyter-example.ipynb` can be used to see how to compile cython code in a jupyter notebook. A nicer webview can be found [here](https://nbviewer.jupyter.org/github/blester125/MIPy-Talk-Jan-2-2020/blob/master/scripts/cython-jupyter-example.ipynb)
