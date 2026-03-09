# Geospatial Data Lakes

Geospatial teams often inherit a patchwork of shapefiles, GeoJSON exports, rasters on shared drives, and a database that nobody entirely trusts. A data lake approach can tidy that up, but only if it is done with some discipline.

## Why people move in this direction

A geospatial data lake becomes attractive once you need one or more of the following:

- repeatable ingestion of multiple spatial sources
- separation between raw and curated layers
- support for both analytical and operational workloads
- cheaper storage for large vector or raster collections
- a route towards reproducible modelling and reporting

## A practical layout

```text
/raw
  /imagery
  /boundaries
  /events

/curated
  /admin
  /transport
  /environment

/analytics
  /feature_store
  /benchmark_inputs
```

## Recommended operating pattern

A sensible baseline is:

1. land raw data unchanged
2. validate geometry and metadata early
3. standardise projection rules and naming conventions
4. publish curated GeoParquet layers for analysis
5. expose heavier or repeated queries through PostGIS or DuckDB

## Why GeoParquet matters

GeoParquet is useful because it behaves like a modern analytical format rather than a legacy GIS container. In practice that means:

- columnar reads
- cleaner interoperability with analytical tools
- better fit for partitioned storage
- easier movement between Python, SQL, and cloud workflows

## Where teams get this wrong

The common mistakes are familiar:

- treating the lake as a dumping ground
- skipping metadata discipline
- mixing coordinate systems casually
- failing to separate raw and curated layers
- assuming “cloud-native” automatically means “well designed”

A data lake is not the architecture. It is only one layer of it.
