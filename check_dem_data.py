import rasterio
from pyproj import Transformer

dem_path = "/home/ritabarco/Documents/OSMFilesTests/GeoData/MDT-50cm-112198-07-2024_v01.tiff"

with rasterio.open(dem_path) as src:
    # 1. Get bounds in native CRS (EPSG:3763)
    left, bottom, right, top = src.bounds
    crs = src.crs
    
    # 2. Set up transformer to convert to standard Lat/Lon (EPSG:4326)
    transformer = Transformer.from_crs(crs, "EPSG:4326", always_xy=True)
    
    # 3. Transform corners
    west, south = transformer.transform(left, bottom)
    east, north = transformer.transform(right, top)
    
    # 4. Calculate center point
    center_lon, center_lat = transformer.transform((left + right) / 2, (bottom + top) / 2)

print("--- DEM FILE SPATIAL METADATA ---")
print(f"Native CRS: {crs}")
print(f"Native Coordinates (PT-TM06):")
print(f"  X (Easting):  {left:.2f} to {right:.2f}")
print(f"  Y (Northing): {bottom:.2f} to {top:.2f}\n")

print("--- GEOGRAPHIC BOUNDS (WGS84) ---")
print(f"Top-Left (NW Corner):  {north:.6f}, {west:.6f}")
print(f"Bottom-Right (SE Corner): {south:.6f}, {east:.6f}\n")

print("--- QUICK LINKS TO VISUALIZE AREA ---")
print(f"Center Point: {center_lat:.6f}, {center_lon:.6f}")
print(f"Google Maps Link: https://www.google.com/maps/search/?api=1&query={center_lat},{center_lon}")