import argparse
import textwrap
from itertools import zip_longest
import pandas as pd
import matplotlib.pyplot as plt
from plotting import add_to_plot

plt.xkcd()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('timings')
    parser.add_argument('--impls', nargs="+")
    parser.add_argument('--colors', nargs="+", default=[])
    parser.add_argument('--points', type=int, nargs="+")
    parser.add_argument('--max-points', '--max_points', type=int)
    parser.add_argument('--dims', type=int, required=True)
    parser.add_argument('--output')
    args = parser.parse_args()

    df = pd.read_csv(args.timings)
    df = df[df.dims == args.dims]
    data = df.groupby(['impl', 'points']).agg(['mean', 'std'])

    if args.impls is None:
        args.impls = sorted(set(df.impl))

    if args.max_points is not None:
        args.points = range(args.max_points)

    fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

    for impl, color in zip_longest(args.impls, args.colors):
        ax = add_to_plot(ax, data, impl, args.points, color=color)

    ax.legend(loc='upper left')
    ax.set_title("\n".join(textwrap.wrap(f"Pairwise Manhattan Distance Timing vs Number of Points for {args.dims} dimensions per Point", 50)))
    ax.set_ylabel("Seconds")
    ax.set_xlabel("Number of Points")

    output = f"timing-vs-points-at-{args.dims}.png" if args.output is None else args.output
    plt.tight_layout()
    print(f"Saving graph to {output}")
    fig.savefig(output)


if __name__ == "__main__":
    main()
