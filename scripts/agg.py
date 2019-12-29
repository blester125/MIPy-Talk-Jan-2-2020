import os
import re
import json
import argparse
from typing import Tuple
import pandas as pd


FILE_REGEX = re.compile(r"^points-(?P<points>\d+)-dims-(?P<dims>\d+).json$")


def extract_params(file_name: str) -> Tuple[str, str]:
    m = FILE_REGEX.search(file_name)
    return int(m.group("points")), int(m.group("dims"))


def add_timing_data(file_name: str, points: int, dims: int, df: pd.DataFrame) -> pd.DataFrame:
    with open(file_name) as f:
        data = json.load(f)
    for algo, timings in data.items():
        for time in timings:
            df = df.append({"impl": algo, "points": points, "dims": dims, "time": time}, ignore_index=True)
    return df


def main():
    parser = argparse.ArgumentParser(
        description="Aggregate a collection of timing json files into csv with (impl, points, dims, time) columns."
    )
    parser.add_argument(
        "--data-dir", "--data_dir", default="speed_data", help="The directory to read timing data json files from."
    )
    parser.add_argument(
        "--output",
        default=os.path.join("speed_data", "timing.csv"),
        help="The name of the csv containing the aggregated timing data.",
    )
    args = parser.parse_args()

    df = pd.DataFrame([], columns=["impl", "points", "dims", "time"])

    for file_name in os.listdir(args.data_dir):
        if FILE_REGEX.match(file_name):
            points, dims = extract_params(file_name)
            df = add_timing_data(os.path.join(args.data_dir, file_name), points, dims, df)

    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
