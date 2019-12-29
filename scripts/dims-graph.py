import argparse
import textwrap
from itertools import zip_longest
import pandas as pd
import matplotlib.pyplot as plt
from plotting import add_to_plot

plt.xkcd()


def main():
    parser = argparse.ArgumentParser(description="Create a graph that scales out the number of dimension while holding the number of points constant.")
    parser.add_argument('timings', help="A CSV of timings with the columns, (impl. points, dims, time)")
    parser.add_argument('--impls', nargs="+", help="The implementations to plot")
    parser.add_argument('--colors', nargs="+", default=[], help="Colors to plot each implementation with, should be aligned with the impls input array.")
    parser.add_argument('--points', type=int, required=True, help="Fix the number of points")
    parser.add_argument('--dims', type=int, nargs="+", help="A list of dimensions to plot the timing for.")
    parser.add_argument('--max_dims', '--max-dims', type=int, help="A max number of dimensions to plot, overwrites the --dims if used.")
    parser.add_argument('--output', help="The file name of the resulting graph.")
    args = parser.parse_args()

    df = pd.read_csv(args.timings)
    df = df[df.points == args.points]
    data = df.groupby(['impl', 'dims']).agg(['mean', 'std'])

    if args.impls is None:
        args.impls = sorted(set(df.impl))

    if args.max_dims is not None:
        args.dims = range(args.max_dims)

    fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

    for impl, color in zip_longest(args.impls, args.colors):
        ax = add_to_plot(ax, data, impl, args.dims, color=color)

    ax.legend(loc='upper left')
    ax.set_title("\n".join(textwrap.wrap(f"Pairwise Manhattan Distance Timing vs Number of Dimensions in a Point calculated for {args.points} Points", 50)))
    ax.set_ylabel("Seconds")
    ax.set_xlabel("Dimensionality of points")

    output = f"timing-vs-dims-at-{args.points}.png" if args.output is None else args.output
    plt.tight_layout()
    print(f"Saving graph to {output}")
    fig.savefig(output)


if __name__ == "__main__":
    main()
