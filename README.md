# OSM Location 3D

This project downloads OSM footprint data, merges DEM tiles, and generates 3D meshes for buildings and trees.

## Setup with uv

From the repository root:

```bash
uv sync
uv run osmlocation3d --config src/osmlocation3d/configs/ist.yaml
```

Or run the module directly:

```bash
uv run python src/osmlocation3d/main.py --config src/osmlocation3d/configs/ist.yaml
```

## Configuration

The `--config` option is required. Choose one of the provided profiles or pass a path to another YAML config:

```bash
uv run osmlocation3d --config src/osmlocation3d/configs/monsanto.yaml
uv run osmlocation3d --config src/osmlocation3d/configs/academia_militar.yaml
```

The profiles are in [src/osmlocation3d/configs](src/osmlocation3d/configs). Relative DEM, geoid, and output paths are resolved from the repository root.

## Files of interest

- [src/osmlocation3d/main.py](src/osmlocation3d/main.py): main processing pipeline
- [src/osmlocation3d/configs](src/osmlocation3d/configs): location-specific YAML profiles
- [pyproject.toml](pyproject.toml): uv-managed dependency metadata
