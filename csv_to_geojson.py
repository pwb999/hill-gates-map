import pandas as pd, json, math

CSV_IN = "gates.csv"
GJ_OUT = "gates.geojson"

df = pd.read_csv(CSV_IN)

def to_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except Exception:
        return None

features = []
for _, r in df.iterrows():
    lon = to_float(r["lon"])
    lat = to_float(r["lat"])
    if lon is None or lat is None:
        continue
    features.append({
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": r.to_dict()
    })

geojson = {"type": "FeatureCollection", "features": features}
with open(GJ_OUT, "w", encoding="utf-8") as f:
    json.dump(geojson, f)
print(f"✅ Wrote {len(features)} features to {GJ_OUT}")