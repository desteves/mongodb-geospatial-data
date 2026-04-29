# addGeoJSON
MONGODB_URI=mongodb+srv://fifa:xRzmVSTD7PbZxIVJ@atlas.aeekw.mongodb.net/fifa




mongoimport --uri ${MONGODB_URI} --type csv --headerline  --collection hostCities  --file

Convert the kickoff_at to an ISO data and store as kickoff_atISO

{
  kickoff_atISO: {
    $dateFromString: {
      dateString: {
        $substr: ["$kickoff_at", 0, 19]
      },
      format: "%Y-%m-%d %H:%M:%S"
    }
  }
} 
Geocodes FIFA documents in MongoDB using [Nominatim](https://nominatim.openstreetmap.org/) (OpenStreetMap) and writes the results back to each document.

Supports two geometry modes:
- **Point** — for venues (stadiums), built from the Nominatim centroid
- **Polygon / MultiPolygon** — for countries, built from the full boundary geometry Nominatim returns

## Collections

| Collection | Source field | Geometry | `osm` field | Location field |
|---|---|---|---|---|
| `hostCities` | `venue_name` | Point | `osm` | `location` |
| `teams` | `team_name` | Polygon / MultiPolygon | `osm` | `location` |

Each processed document receives:

| Field | Contents |
|---|---|
| `osm` | Raw Nominatim response payload |
| `location` | GeoJSON `Feature` with the appropriate geometry |

## Requirements

- Python 3.9+
- `requests`
- `pymongo`

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python addGeoJSON.py
```

## Example output

```
Found 3 documents in 'hostCities'.

  Geocoding: 'Lusail Iconic Stadium, Qatar' ...
{'boundingbox': ['25.4333', '25.4334', '51.4888', '51.4889'],
 'class': 'leisure',
 'display_name': 'Lusail Iconic Stadium, Lusail, Qatar',
 'lat': '25.4333',
 'lon': '51.4888',
 'osm_id': '123456789',
 'osm_type': 'way',
 'type': 'stadium'}
# stored under → location

Done with 'hostCities'.

Found 32 documents in 'teams'.

  Geocoding: 'Brazil' ...
{'boundingbox': ['-33.75', '5.27', '-73.98', '-28.84'],
 'class': 'boundary',
 'display_name': 'Brazil',
 'geojson': {'coordinates': [...], 'type': 'MultiPolygon'},
 'lat': '-10.3333332',
 'lon': '-53.2',
 'osm_id': '287077',
 'osm_type': 'relation',
 'type': 'administrative'}

Done with 'teams'.
```
