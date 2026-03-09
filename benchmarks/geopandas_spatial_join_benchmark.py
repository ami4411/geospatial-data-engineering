"""Simple benchmark for measuring GeoPandas spatial join performance.

This is not intended to be a research-grade benchmarking framework.
It is a practical starting point for comparing workloads, testing data sizes,
and documenting how performance changes when indexing or storage choices change.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import geopandas as gpd


def load_frame(path: str) -> gpd.GeoDataFrame:
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Input file not found: {dataset_path}")
    return gpd.read_file(dataset_path)


def benchmark_spatial_join(left_path: str, right_path: str, predicate: str = "intersects") -> None:
    left = load_frame(left_path)
    right = load_frame(right_path)

    start = time.perf_counter()
    result = gpd.sjoin(left, right, predicate=predicate, how="inner")
    duration = time.perf_counter() - start

    print(f"Left rows:   {len(left):,}")
    print(f"Right rows:  {len(right):,}")
    print(f"Matches:     {len(result):,}")
    print(f"Predicate:   {predicate}")
    print(f"Elapsed:     {duration:.3f} seconds")
    print("
Interpretation:")
    print("- Compare runs across file formats, dataset sizes, and indexing strategies.")
    print("- Keep CRS consistent before benchmarking.")
    print("- Avoid drawing conclusions from one tiny sample dataset.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Benchmark a GeoPandas spatial join.")
    parser.add_argument("left", help="Path to the left-hand geospatial dataset")
    parser.add_argument("right", help="Path to the right-hand geospatial dataset")
    parser.add_argument(
        "--predicate",
        default="intersects",
        choices=["intersects", "within", "contains", "overlaps", "touches"],
        help="Spatial predicate to use",
    )
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    benchmark_spatial_join(args.left, args.right, args.predicate)
