# Example: Choosing a Spatial Join Strategy

Suppose you need to assign millions of points to administrative polygons.

A beginner framing is: “How do I run a spatial join?”
A more useful framing is: “What is the cheapest reliable way to assign points to polygons at the volume I actually have?”

## A sensible decision path

- If the data is small and exploratory, GeoPandas is usually enough.
- If the join needs to be repeated in a shared environment, PostGIS is often the better home.
- If the data is columnar and analytical, DuckDB plus GeoParquet may be an efficient intermediate option.

## What to check before running the join

1. Are both layers using an appropriate CRS?
2. Are the polygon geometries valid?
3. Can the input be filtered spatially or by attribute first?
4. Is the result intended for one-off analysis or repeated production use?

That last question is often the one that matters most.
