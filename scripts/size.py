import math
import argparse
from typing import Tuple


INT32 = 4
SCALE = 1024
SIZE_NAMES = ("B", "KiB", "MiB", "GiB", "PiB")

HDD_SCALE = 1000
HDD_SIZE_NAMES = ("B", "KB", "MB", "GB", "PB")


def human_readable_size(size: int, sizes: Tuple[str] = SIZE_NAMES, scale: int = SCALE) -> str:
    if size == 0:
        return f"0{sizes[0]}"
    idx = int(math.floor(math.log(size, scale)))
    p = math.pow(scale, idx)
    s = round(size / p, 2)
    return f"{s}{sizes[idx]}"


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the memory usage for various pairwise Manhattan Distance implementations."
    )
    parser.add_argument("--points", type=int, help="The number of points", required=True)
    parser.add_argument("--dims", type=int, help="The number of dimensions")
    args = parser.parse_args()

    size_in_bytes = args.points ** 2 * INT32
    if args.dims is not None:
        size_in_bytes *= args.dims

    print(human_readable_size(size_in_bytes))


if __name__ == "__main__":
    main()
