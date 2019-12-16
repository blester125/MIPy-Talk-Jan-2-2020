import argparse
import textwrap
import pandas as pd
import matplotlib.pyplot as plt
from plotting import add_to_plot

plt.xkcd()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('timings')
    parser.add_argument('--impls', nargs="+")
    parser.add_argument('--points', type=int, required=True)
    parser.add_argument('--dims', type=int, nargs="+")
    parser.add_argument('--output')
    args = parser.parse_args()

    df = pd.read_csv(args.timings)
    df = df[df.points == args.points]
    data = df.groupby(['impl', 'dims']).agg(['mean', 'std'])

    if args.impls is None:
        args.impls = sorted(set(df.impl))

    fig, ax = plt.subplots(figsize=(12, 8), dpi=200)

    for impl in args.impls:
        ax = add_to_plot(ax, data, impl, args.dims)

    ax.legend(loc='upper left')
    ax.set_title("\n".join(textwrap.wrap(f"Pairwise Manhattan Distance Timing vs Number of Dimensions in a Point calculated for {args.points} Points", 50)))
    ax.set_ylabel("Seconds")
    ax.set_xlabel("Dimensionality of points")

    output = f"timing-vs-dims-at-{args.points}.png" if args.output is None else args.output
    plt.tight_layout()
    fig.savefig(output)


if __name__ == "__main__":
    main()
