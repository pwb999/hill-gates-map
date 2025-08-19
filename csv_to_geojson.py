#!/usr/bin/env python3
import pandas as pd, json, math, sys

CSV_IN  = "stiles.csv"
GJ_OUT  = "stiles.geojson"
EXPECTED_COLS = {"id","name","lon","lat"}

def to_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except Exception:
        return None

def main():
    df = pd.read_csv(CSV_IN)
    have = set(df.columns.str.lower())
    missing = EXPECTED_COLS - have
    if missing:
        sys.exit(f"❌ Missing columns in {CSV_IN}: {sorted(missing)}")

    # Normalize column names
    df.columns = [c.lower() for c in df.columns]

    # Clean/basic typing
    df["id"] = pd.to_numeric(df["id"], errors="coerce").astype("Int64")
    df["name"] = df["name"].astype(str).str.strip()

    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")

    before = len(df)
    df = df.dropna(subset=["lon","lat"])
    dropped = before - len(df)

    # Optional: de-dupe by rounded coords (adjust precision as needed)
    df["_lonr"] = df["lon"].round(6)
    df["_latr"] = df["lat"].round(6)
    df = df.drop_duplicates(subset=["_lonr","_latr"]).drop(columns=["_lonr","_latr"])

    features = []
    for _, r in df.iterrows():
        lon = to_float(r["lon"])
        lat = to_float(r["lat"])
        if lon is None or lat is None:
            continue

        # Keep only the useful props (expand if you have more fields)
        props = {
            "id": int(r["id"]) if pd.notna(r["id"]) else None,
            "name": r["name"]
        }

        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},  # [lon, lat] = [x, y]
            "properties": props
        })

    geojson = {"type": "FeatureCollection", "features": features}
    with open(GJ_OUT, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, separators=(",", ":"), indent=2)

    print(f"✅ Wrote {len(features)} features to {GJ_OUT} (dropped {dropped} rows with invalid coords)")

if __name__ == "__main__":
    main()