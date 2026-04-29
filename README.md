# Jumpstart: Geospatial Data with MongoDB

## Prerequisites

- [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/) installed
- [`atlas` CLI](https://www.mongodb.com/docs/atlas/cli/current/install-atlas-cli/) installed
- [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/installation/installation/) installed (provides `mongoimport`)
- Docker running

## Setup — Local MongoDB Atlas Deployment

```sh
atlas local setup \
  --mdbVersion latest \
  --port 27000 \
  --force \
  --connectWith mongosh
```

## Load Data

> Open a second terminal tab for this step.

```sh
mongoimport --uri "mongodb://localhost:27000/test" --collection=delivery_zones  --file=data/delivery_zones.json  --jsonArray --drop
mongoimport --uri "mongodb://localhost:27000/test" --collection=delivery_routes --file=data/delivery_routes.json --jsonArray --drop
mongoimport --uri "mongodb://localhost:27000/test" --collection=restaurants     --file=data/restaurants.json     --jsonArray --drop
mongoimport --uri "mongodb://localhost:27000/test" --collection=warehouse_items --file=data/warehouse_items.json --jsonArray --drop
```

---

## Use Cases

```text
┌─────────────────┬─────────────────┬─────────────────┐
│   FLAT GRIDS    │    SPHERICAL    │  ADV. SEARCH    │
│                 │                 │                 │
│       ⊞         │       🌐        │       🔍        │
│                 │                 │                 │
│   2d index      │  2dsphere index │   geo type      │
│                 │                 │                 │
│                 │                 │                 │
│   $near         │  $nearSphere    │   geoShape      │
│   $geoWithin    │  $geoWithin     │   geoWithin     │
│                 │  $geoIntersects │                 │
│                 │                 │                 │
│                 │                 │                 │
│  Your units     │    Meters       │    Meters       │
└─────────────────┴─────────────────┴─────────────────┘
```

## Flat Grid — 2D

Uses a flat `[x, y]` coordinate grid. Suitable for warehouse shelf positions, game maps, or any non-geographic 2D space.

![Flat Grid 2D demo](gifs/uc1-flatgrids.gif)

### Data Model

```js
/*
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 |G|e|o|s|p|a|t|i|a|l| |D|a|t|a|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 +-+-+-+-+-+-+-+-+-+-+-+-+
 |F|l|a|t| |G|r|i|d| |2|D|
 +-+-+-+-+ +-+-+-+-+ +-+-+
*/
// Geospatial Data / 2D Use Case / Data Model
db.warehouse_items.find({}, { _id: 0, pos: 1 })
```

### Index

```js
// Geospatial Data / 2D Use Case / Index
db.warehouse_items.createIndex({ pos: "2d" })
```

### Query — `$near`

```js
// Geospatial Data / 2D Use Case / Query / $near
var filter = {
  pos: {
    $near: [25, 65],  // x, y
    $maxDistance: 5   // optional radius
  }
}
var projection = { pos: 1, name: 1, _id: 0 }

db.warehouse_items.find(filter, projection)
```

### Query — `$geoWithin $center`

```js
// Geospatial Data / 2D Use Case / Query / $geoWithin
var filter = {
  pos: {
    $geoWithin: {
      $center: [[25, 65], 5]  // [x, y], radius
    }
  }
}

db.warehouse_items.find(filter, projection)
```

---

## Spherical — 2dsphere

Uses GeoJSON with real-world longitude/latitude coordinates. Suitable for maps, delivery zones, and location-based search.

![Spherical 2dsphere demo](gifs/uc2-sphere.gif)

### Data Model

```js
/*
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 |G|e|o|s|p|a|t|i|a|l| |D|a|t|a|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 +-+-+-+-+-+-+-+-+-+
 |S|p|h|e|r|i|c|a|l|
 +-+-+-+-+-+-+-+-+-+
*/
// Geospatial Data / 2dsphere Use Case / Data Model
db.restaurants.find({}, { _id: 0, name: 1, location: 1 })
```

### Index

```js
// Geospatial Data / 2dsphere Use Case / Index
db.restaurants.createIndex({ location: "2dsphere" })
```

### Query — `$nearSphere`

```js
// Geospatial Data / 2dsphere Use Case / Query / $nearSphere
var filter = {
  location: {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]
      },
      $maxDistance: 800  // metres, optional
    }
  }
}
var projection = { name: 1, _id: 0 }

db.restaurants.find(filter, projection)
```

### Query — `$geoWithin $geometry`

```js
// Geospatial Data / 2dsphere Use Case / Query / $geoWithin
var DowntownAustinDeliveryZone = [[
  [-97.755, 30.280],
  [-97.730, 30.280],
  [-97.730, 30.260],
  [-97.755, 30.260],
  [-97.755, 30.280]
]]

var filter = {
  location: {
    $geoWithin: {
      $geometry: { type: "Polygon", coordinates: DowntownAustinDeliveryZone }
    }
  }
}

db.restaurants.find(filter, projection)
```

### Query — `$geoIntersects`

```js
// Geospatial Data / 2dsphere Use Case / Query / $geoIntersects
db.delivery_zones.find({}, { _id: 0, name: 1, boundary: 1 })
db.delivery_zones.createIndex({ boundary: "2dsphere" })

var deliveryRoute = {
  type: "LineString",
  coordinates: [
    [-97.744820, 30.265730],  // Start: Torchy's
    [-97.742000, 30.267000],
    [-97.740000, 30.268500],
    [-97.739410, 30.267240]   // End: near Voodoo Doughnut
  ]
}

db.delivery_zones.find({
  boundary: {
    $geoIntersects: {
      $geometry: deliveryRoute
    }
  }
}, { name: 1, _id: 0 })
```

---

## Advanced Search — Atlas Search + Geo

Combines full-text search with geospatial filtering in a single aggregation pipeline.

![Advanced Search demo](gifs/uc3-advancedsearch.gif)

### Data Model

```js
/*
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 |G|e|o|s|p|a|t|i|a|l| |D|a|t|a|
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
 |A|d|v|a|n|c|e|d| |S|e|a|r|c|h|
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+
*/
// Geospatial Data / Advanced Search Use Case / Data Model
db.restaurants.find({}, { _id: 0, name: 1, location: 1, tags: 1, description: 1, rating: 1 })
```

### Index

```js
// Geospatial Data / Advanced Search Use Case / Index
db.restaurants.createSearchIndex(
  "restaurants_search",
  {
    mappings: {
      dynamic: false,
      fields: {
        name:        { type: "string",      analyzer: "lucene.standard" },
        description: { type: "string",      analyzer: "lucene.english" },
        cuisine:     { type: "stringFacet" },
        location:    { type: "geo" },
        tags:        { type: "token" },
        rating:      { type: "number" }
      }
    }
  }
)
```

### Query — text + geo within 1.5 km of Texas Capitol

```js
// Geospatial Data / Advanced Search Use Case / Query
var customerLocation = {
  type: "Point",
  coordinates: [-97.740310, 30.274670]
}

db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_search",
      compound: {
        must: [{
          text: {
            query: "breakfast tacos",
            path: ["name", "description", "tags"],
            fuzzy: { maxEdits: 1 }
          }
        }],
        filter: [{
          geoWithin: {
            path: "location",
            circle: {
              center: customerLocation,
              radius: 1500  // metres
            }
          }
        }]
      }
    }
  },
  {
    $project: {
      name: 1,
      description: 1,
      cuisine: 1,
      tags: 1,
      score: { $meta: "searchScore" }
    }
  }
])
```