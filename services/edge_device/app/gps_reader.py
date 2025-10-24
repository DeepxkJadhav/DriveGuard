import random

def get_current_location():
    """
    Return current GPS location.
    For demo purposes, randomize around a fixed point.
    """
    base_lat = 37.7749   # Example: San Francisco
    base_lon = -122.4194

    lat = base_lat + random.uniform(-0.001, 0.001)
    lon = base_lon + random.uniform(-0.001, 0.001)
    return {"lat": lat, "lon": lon}
