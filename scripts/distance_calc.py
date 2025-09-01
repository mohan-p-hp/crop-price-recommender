import math
import pandas as pd

# Haversine formula to calculate straight-line distance between two lat/lon points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Farmer’s location (example: Tumkur, Karnataka)
farmer_lat, farmer_lon = 13.3409, 77.1010

# Load market data
df = pd.read_csv("data/markets.csv")

# Compute distance for each market
df["distance_km"] = df.apply(
    lambda row: haversine(farmer_lat, farmer_lon, row["lat"], row["lon"]),
    axis=1
)

# Show results
print(df[["market_name", "distance_km"]])

# Save to new CSV with distances
df.to_csv("data/markets_with_distance.csv", index=False)
print("\n✅ Results saved to data/markets_with_distance.csv")
