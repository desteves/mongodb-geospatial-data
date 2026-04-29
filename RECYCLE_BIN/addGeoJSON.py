"""
Geocode FIFA documents and persist GeoJSON results to MongoDB.

For each configured collection this script:
1. Calls the Nominatim API using a field value from each document as the query.
2. Writes the raw API payload to a configurable ``osm_field``.
3. Builds a GeoJSON Feature from that payload and writes it to a configurable ``location_field``.

Supports both Point geometry (venues) and Polygon/MultiPolygon geometry (countries).
"""

import pprint
import time
from collections.abc import Callable
from typing import Any, Optional

import requests
from pymongo import MongoClient
from pymongo.collection import Collection

# ---- CONFIG ----
MONGODB_URI = "mongodb+srv://fifa:xRzmVSTD7PbZxIVJ@atlas.aeekw.mongodb.net/fifa"
DB_NAME = "fifa"

# Nominatim endpoint (public OSM instance)
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

# Identify yourself per Nominatim policy
HEADERS = {
    "User-Agent": "FifaGeoApp/1.0 (diana@mongodb.com)"
}

# Delay in seconds between requests to respect Nominatim rate limits (1 req/s)
REQUEST_DELAY = 1.1


def geocode(query: str, polygon: bool = False) -> Optional[dict[str, Any]]:
    """Call Nominatim and return the raw top-hit payload dict.

    Args:
        query: Free-text search string passed to Nominatim.
        polygon: When ``True``, requests full polygon GeoJSON from Nominatim
            (suitable for countries or administrative boundaries).

    Returns:
        The first Nominatim result dict, or ``None`` if no results were found.

    Raises:
        requests.RequestException: If the HTTP request fails.
    """
    params: dict[str, Any] = {
        "q": query,
        "format": "json",
        "limit": 1,
    }
    if polygon:
        params["polygon_geojson"] = 1

    resp = requests.get(NOMINATIM_URL, params=params, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data[0] if data else None


def build_geojson(osm: dict[str, Any]) -> dict[str, Any]:
    """Build a GeoJSON Feature from a raw Nominatim result dict.

    Uses the full polygon geometry returned by Nominatim when ``polygon_geojson=1``
    was requested (e.g. for countries), otherwise falls back to a ``Point``.

    Args:
        osm: A single Nominatim result dict containing at minimum ``lon`` and ``lat`` keys.

    Returns:
        A GeoJSON ``Feature`` dict with the appropriate geometry and OSM metadata properties.
    """
    geometry: dict[str, Any] = osm.get("geojson") or {
        "type": "Point",
        "coordinates": [float(osm["lon"]), float(osm["lat"])],  # [lon, lat] per spec
    }
    return {
        "type": "Feature",
        "geometry": geometry,
        "properties": {
            "display_name": osm.get("display_name"),
            "osm_type": osm.get("osm_type"),
            "osm_id": osm.get("osm_id"),
            "class": osm.get("class"),
            "type": osm.get("type"),
        },
    }


def process_collection(
    coll: Collection[Any],
    source_field: str,
    query_builder: Callable[[dict[str, Any]], str],
    osm_field: str = "osm",
    location_field: str = "geojson",
    polygon: bool = False,
) -> None:
    """Geocode every document in a collection and write results back.

    Args:
        coll: The MongoDB collection to process.
        source_field: Document field whose value triggers geocoding; documents
            missing this field are skipped.
        query_builder: Callable that receives a document and returns the
            Nominatim query string for that document.
        osm_field: Field name under which the raw Nominatim payload is stored.
        location_field: Field name under which the GeoJSON Feature is stored.
        polygon: When ``True``, requests full polygon geometry from Nominatim.
    """
    docs: list[dict[str, Any]] = list(coll.find({}))
    print(f"\nFound {len(docs)} documents in '{coll.name}'.")

    for doc in docs:
        if not doc.get(source_field):
            print(f"  Skipping doc {doc['_id']} — no '{source_field}' field.")
            continue

        query = query_builder(doc)
        print(f"\n  Geocoding: '{query}' ...")
        try:
            osm = geocode(query, polygon=polygon)
        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"  ERROR — {e}")
            osm = None

        pprint.pprint(osm)

        location: Optional[dict[str, Any]] = build_geojson(osm) if osm else None

        coll.update_one(
            {"_id": doc["_id"]},
            {"$set": {osm_field: osm, location_field: location}},
        )

        # Respect Nominatim's 1-request-per-second policy
        time.sleep(REQUEST_DELAY)

    print(f"Done with '{coll.name}'.")


def main() -> None:
    """Geocode hostCities venues (Point) and teams countries (Polygon) and persist results."""
    client: MongoClient[dict[str, Any]] = MongoClient(MONGODB_URI)
    db = client[DB_NAME]

    # hostCities: geocode venue name + country context → Point geometry
    # process_collection(
    #     coll=db["hostCities"],
    #     source_field="venue_name",
    #     query_builder=lambda doc: f"{doc['venue_name']}, {doc.get('country', '')}",
    #     osm_field="osm",
    #     location_field="location",
    #     polygon=False,
    # )

    # # teams: geocode team_name as a country → Polygon/MultiPolygon geometry
    # process_collection(
    #     coll=db["teams"],
    #     source_field="team_name",
    #     query_builder=lambda doc: doc["team_name"],
    #     osm_field="osm",
    #     location_field="location",
    #     polygon=True,
    # )

    client.close()


if __name__ == "__main__":
    main()
