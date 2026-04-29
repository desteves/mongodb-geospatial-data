# ASCII Art: 2dsphere Geospatial Operators

## $nearSphere - Sorted Proximity Search

Returns documents sorted by distance from a point (closest first).

```
                            $nearSphere
         ════════════════════════════════════════════

                    Finds documents near a point
                    Results SORTED by distance


                         ·················
                    ····         3         ····
                 ···      ◉ Ramen Tatsu-Ya     ···
               ··            (2.8 km)            ··
              ··                                  ··
             ·         ·············               ·
            ·      ···       2       ···            ·
           ·     ··    ◉ Clay Pit      ··           ·
           ·    ·        (520m)          ·          ·
          ·    ·    ···············       ·          ·
          ·   ·   ··       1       ··     ·          ·
          ·   ·  ·  ◉ Texas Chili   ·     ·          ·
          ·   ·  ·    Parlor        ·     ·          ·
          ·   ·  ·     (248m)       ·     ·          ·
          ·   ·  ·                  ·     ·          ·
          ·   ·  ·       ★          ·     ·          ·
          ·   ·  ·    QUERY         ·     ·          ·
          ·   ·  ·    POINT         ·     ·          ·
          ·   ·  ·                  ·     ·          ·
          ·   ·   ··              ··      ·          ·
          ·   ·    ···   800m  ···        ·          ·
           ·   ·      ·········          ·          ·
           ·    ·                       ·           ·
            ·    ··                   ··           ·
             ·     ···    1.5km   ···             ·
              ··      ·············             ··
               ··                              ··
                 ···                        ···
                    ····    3.0km      ····
                         ·················


         ┌─────────────────────────────────────────────────┐
         │  RESULTS (automatically sorted by distance):    │
         │                                                 │
         │  #1  Texas Chili Parlor .......... 248m   ✓     │
         │  #2  Clay Pit .................... 520m   ✓     │
         │  #3  Ramen Tatsu-Ya .............. 2.8km  ✓     │
         └─────────────────────────────────────────────────┘

         ★ = Query Point (center)
         ◉ = Restaurant (result)

         Key Feature: Results are SORTED by distance
```

### $nearSphere with $maxDistance

```
                    $nearSphere + $maxDistance
         ════════════════════════════════════════════

              Only returns documents within max radius


                              ◉ Ramen Tatsu-Ya
                                 (2.8 km)
                                    ✗
                              OUTSIDE RADIUS


                       ·····················
                   ···                       ···
                 ··                             ··
               ··                                 ··
              ·          ◉ Clay Pit                ·
             ·              (520m)                  ·
            ·                 ✓                     ·
            ·                                       ·
           ·                                         ·
           ·        ◉ Texas Chili Parlor             ·
           ·             (248m)                      ·
           ·               ✓                         ·
           ·                                         ·
           ·              ★ QUERY                    ·
           ·               POINT                     ·
           ·                                         ·
            ·                                       ·
            ·        $maxDistance: 800m             ·
             ·                                     ·
              ··                                 ··
                ··                             ··
                  ···                       ···
                     ·····················


         ┌─────────────────────────────────────────────────┐
         │  RESULTS (within 800m, sorted by distance):     │
         │                                                 │
         │  #1  Texas Chili Parlor .......... 248m   ✓     │
         │  #2  Clay Pit .................... 520m   ✓     │
         │  --  Ramen Tatsu-Ya .............. 2.8km  ✗     │
         └─────────────────────────────────────────────────┘
```

---

## $geoWithin - Containment Search (No Sort)

Returns documents contained within a shape. Results are **NOT** sorted.

### $geoWithin with Polygon

```
                         $geoWithin (Polygon)
         ════════════════════════════════════════════════

              Finds documents INSIDE a polygon boundary
              Results are NOT sorted by distance


              ◉ Epoch Coffee                    ◉ Home Slice
                   ✗                                 ✗
              OUTSIDE                           OUTSIDE


         ┌─────────────────────────────────────────────────────┐
         │                                                     │
         │      D O W N T O W N   A U S T I N   Z O N E        │
         │                                                     │
         │                                                     │
         │           ◉ Texas Chili Parlor                      │
         │                    ✓                                │
         │                                                     │
         │                         ◉ Clay Pit                  │
         │                              ✓                      │
         │                                                     │
         │      ◉ Amy's Ice Creams          ◉ Voodoo Doughnut  │
         │              ✓                          ✓           │
         │                                                     │
         │                  ◉ Torchy's Tacos                   │
         │                         ✓                           │
         │                                                     │
         │                                                     │
         └─────────────────────────────────────────────────────┘

                            ◉ Mozart's Coffee
                                  ✗
                             OUTSIDE


         ┌─────────────────────────────────────────────────┐
         │  RESULTS (NOT sorted, order not guaranteed):    │
         │                                                 │
         │  •  Texas Chili Parlor ................... ✓    │
         │  •  Clay Pit ............................. ✓    │
         │  •  Amy's Ice Creams ..................... ✓    │
         │  •  Voodoo Doughnut ...................... ✓    │
         │  •  Torchy's Tacos ....................... ✓    │
         └─────────────────────────────────────────────────┘

         ◉ = Restaurant
         ✓ = Inside polygon (returned)
         ✗ = Outside polygon (not returned)

         Key Feature: Results are NOT sorted
```

### $geoWithin with Circle ($centerSphere)

```
                    $geoWithin + $centerSphere
         ════════════════════════════════════════════

             Finds documents within a circular area
             Results are NOT sorted by distance


                              ◉ Ramen Tatsu-Ya
                                    ✗
                              OUTSIDE CIRCLE


                       ·····················
                   ···                       ···
                 ··                             ··
               ··          ◉ Clay Pit            ··
              ·               ✓                    ·
             ·                                      ·
            ·     ◉ Texas Chili                     ·
            ·        Parlor                          ·
           ·           ✓                              ·
           ·                                          ·
           ·   ◉ Amy's              ◉ Voodoo          ·
           ·      ✓                    ✓              ·
           ·                                          ·
           ·            ◉ Torchy's                    ·
           ·               ✓                          ·
            ·                                        ·
            ·           radius: 1.5km               ·
             ·                                     ·
              ··           center: ★             ··
                ··      [-97.74, 30.27]        ··
                  ···                       ···
                     ·····················


         ┌─────────────────────────────────────────────────┐
         │  RESULTS (NOT sorted, order not guaranteed):    │
         │                                                 │
         │  •  Clay Pit ............................. ✓    │
         │  •  Texas Chili Parlor ................... ✓    │
         │  •  Amy's Ice Creams ..................... ✓    │
         │  •  Voodoo Doughnut ...................... ✓    │
         │  •  Torchy's Tacos ....................... ✓    │
         └─────────────────────────────────────────────────┘

         Key Feature: Circular area, but NO distance sorting
```

---

## $geoIntersects - Overlap Detection

Returns documents where geometries **overlap** or **touch** the query geometry.

### $geoIntersects - Point in Polygon

```
                    $geoIntersects (Point → Polygon)
         ════════════════════════════════════════════════

            "Which delivery zones contain this customer?"


         ┌─────────────────────────────────────────────────────┐
         │                                                     │
         │              N O R T H   L O O P   Z O N E          │
         │                                                     │
         │                    Does NOT contain                 │
         │                    customer point                   │
         │                          ✗                          │
         │                                                     │
         └─────────────────────────────────────────────────────┘


         ┌─────────────────────────────────────────────────────┐
         │                                                     │
         │          D O W N T O W N   Z O N E                  │
         │                                                     │
         │                                                     │
         │                    ★ CUSTOMER                       │
         │                      LOCATION                       │
         │                        ✓                            │
         │                                                     │
         │              Zone INTERSECTS with                   │
         │              the customer point                     │
         │                                                     │
         └─────────────────────────────────────────────────────┘


         ┌─────────────────────────────────────────────────────┐
         │                                                     │
         │           L A K E   A U S T I N   Z O N E           │
         │                                                     │
         │                    Does NOT contain                 │
         │                    customer point                   │
         │                          ✗                          │
         │                                                     │
         └─────────────────────────────────────────────────────┘


         ┌─────────────────────────────────────────────────┐
         │  QUERY: Which zones intersect with customer?    │
         │                                                 │
         │  RESULT:                                        │
         │  •  Downtown Zone .................... ✓        │
         │                                                 │
         │  Customer is within Downtown delivery zone      │
         └─────────────────────────────────────────────────┘
```

### $geoIntersects - LineString through Polygons

```
                    $geoIntersects (LineString → Polygons)
         ════════════════════════════════════════════════════

              "Which delivery zones does this route cross?"


         ┌─────────────────────────────────────────────────────────────────────┐
         │                                                                     │
         │    N O R T H   L O O P                     U T   C A M P U S        │
         │         Z O N E                               Z O N E               │
         │                                                                     │
         │         ◉ START                                                     │
         │           (Epoch Coffee)                                            │
         │             │                                                       │
         │             │  Route                            Does NOT            │
         │             │  passes                           intersect           │
         │             │  through                          route               │
         │             │    ✓                                 ✗                │
         │             │                                                       │
         │             ▼                                                       │
         └─────────────│───────────────────────────────────────────────────────┘
                       │
                       │
         ┌─────────────│───────────────────────────────────────────────────────┐
         │             │                                                       │
         │    D O W N T│O W N   Z O N E                                        │
         │             │                                                       │
         │             │                                                       │
         │             │   Route                                               │
         │             │   passes                                              │
         │             │   through                                             │
         │             │      ✓                                                │
         │             │                                                       │
         │             ▼                                                       │
         │           ◉ END                                                     │
         │             (Customer)                                              │
         │                                                                     │
         └─────────────────────────────────────────────────────────────────────┘


         ┌─────────────────────────────────────────────────┐
         │  QUERY: Which zones does the route cross?       │
         │                                                 │
         │  RESULTS:                                       │
         │  •  North Loop Zone .................. ✓        │
         │  •  Downtown Zone .................... ✓        │
         │                                                 │
         │  Route passes through 2 delivery zones          │
         └─────────────────────────────────────────────────┘
```

### $geoIntersects - Polygon Overlap

```
                    $geoIntersects (Polygon → Polygon)
         ════════════════════════════════════════════════════

           "Which existing zones overlap with new zone?"


                    ┌───────────────────────┐
                    │                       │
                    │   N O R T H           │
                    │    L O O P            │
                    │                       │
                    │     Does NOT          │
                    │     overlap           │
                    │        ✗              │
                    │                       │
                    └───────────────────────┘



              ┌─────────────────────────────────────┐
              │                                     │
              │        U T   C A M P U S            │
              │                                     │
              │           Overlaps!                 │
              │              ✓                      │
              │    ┌────────────────────────────────│──────────┐
              │    │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░░░░░░░ │
              │    │ ░░░░  OVERLAP AREA  ░░░░░░░░░░░│░░░░░░░░░ │
              │    │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│░░░░░░░░░ │
              └────│────────────────────────────────┘░░░░░░░░░ │
                   │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
                   │                                           │
                   │        N E W   P R O P O S E D            │
                   │             Z O N E                       │
                   │          (Query Geometry)                 │
                   │                                           │
                   └───────────────────────────────────────────┘


         ┌─────────────────────────────────────────────────┐
         │  QUERY: Which zones overlap with new zone?      │
         │                                                 │
         │  RESULT:                                        │
         │  •  UT Campus Zone ................... ✓        │
         │                                                 │
         │  New zone overlaps with UT Campus zone          │
         └─────────────────────────────────────────────────┘
```

---

## Side-by-Side Comparison

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│     $nearSphere      │     $geoWithin       │   $geoIntersects     │
├──────────────────────┼──────────────────────┼──────────────────────┤
│                      │                      │                      │
│    "Find nearest"    │   "Find inside"      │   "Find overlap"     │
│                      │                      │                      │
│         ·····        │  ┌──────────────┐    │  ┌────────┐          │
│       ·· 3 ··        │  │              │    │  │        │          │
│      · ◉    ·        │  │  ◉  ◉   ◉    │    │  │   ───────────     │
│     ·   2    ·       │  │       ◉      │    │  │   │////│    │     │
│    ·  ◉       ·      │  │  ◉      ◉    │    │  └───│////│────┘     │
│    ·    1     ·      │  │              │    │      │////│          │
│    ·  ◉  ★    ·      │  └──────────────┘    │      ─────────       │
│    ·          ·      │                      │                      │
│     ·        ·       │  Results: Items      │  Results: Shapes     │
│      ·      ·        │  INSIDE boundary     │  that OVERLAP        │
│       ·····          │                      │                      │
│                      │                      │                      │
│  Results: SORTED     │  Results: NOT        │  Results: NOT        │
│  by distance         │  sorted              │  sorted              │
│                      │                      │                      │
├──────────────────────┼──────────────────────┼──────────────────────┤
│                      │                      │                      │
│  USE CASES:          │  USE CASES:          │  USE CASES:          │
│                      │                      │                      │
│  • Find closest      │  • Find restaurants  │  • Check if route    │
│    restaurants       │    in delivery zone  │    crosses zones     │
│                      │                      │                      │
│  • Sort by           │  • Find users in     │  • Find overlapping  │
│    proximity         │    a region          │    territories       │
│                      │                      │                      │
│  • "Nearest to me"   │  • "In this area"    │  • "Passes through"  │
│                      │                      │                      │
└──────────────────────┴──────────────────────┴──────────────────────┘
```

---

## Query Shape Support

```
┌─────────────────────────────────────────────────────────────────────┐
│                    QUERY GEOMETRY SUPPORT                           │
├──────────────────┬─────────────┬─────────────┬──────────────────────┤
│  Operator        │    Point    │  LineString │      Polygon         │
├──────────────────┼─────────────┼─────────────┼──────────────────────┤
│                  │             │             │                      │
│  $nearSphere     │     ✓       │      ✗      │        ✗             │
│                  │   Center    │             │                      │
│                  │   point     │             │                      │
│                  │             │             │                      │
├──────────────────┼─────────────┼─────────────┼──────────────────────┤
│                  │             │             │                      │
│  $geoWithin      │     ✗       │      ✗      │        ✓             │
│                  │             │             │   Boundary           │
│                  │             │             │   shape              │
│                  │             │             │                      │
├──────────────────┼─────────────┼─────────────┼──────────────────────┤
│                  │             │             │                      │
│  $geoIntersects  │     ✓       │      ✓      │        ✓             │
│                  │   "Is this  │  "Does this │   "Does this         │
│                  │    point    │   path      │    area              │
│                  │    in?"     │   cross?"   │    overlap?"         │
│                  │             │             │                      │
└──────────────────┴─────────────┴─────────────┴──────────────────────┘
```

---

## Real-World Analogy

```
┌─────────────────────────────────────────────────────────────────────┐
│                      REAL-WORLD ANALOGIES                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  $nearSphere = "What's closest to me?"                              │
│  ─────────────────────────────────────                              │
│                                                                     │
│       You're standing downtown asking:                              │
│       "Show me restaurants, closest first"                          │
│                                                                     │
│                    ★ You                                            │
│                    │                                                │
│                    ├── 100m ──► ◉ #1 Closest                        │
│                    ├── 300m ──► ◉ #2                                │
│                    └── 800m ──► ◉ #3 Farthest                       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  $geoWithin = "What's in this area?"                                │
│  ───────────────────────────────────                                │
│                                                                     │
│       Looking at a map asking:                                      │
│       "Show me everything inside downtown"                          │
│                                                                     │
│              ┌──── DOWNTOWN ────┐                                   │
│              │  ◉  ◉        ◉   │  ◉ Outside                        │
│              │       ◉   ◉      │                                   │
│              │    ◉        ◉    │  ◉ Outside                        │
│              └──────────────────┘                                   │
│                    ▲                                                │
│                    All these returned                               │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  $geoIntersects = "What does this touch?"                           │
│  ────────────────────────────────────────                           │
│                                                                     │
│       Drawing a route on a map asking:                              │
│       "Which zones does my delivery cross?"                         │
│                                                                     │
│         ┌── ZONE A ──┐                                              │
│         │      ◉─────│───────┐                                      │
│         │        ✓   │       │                                      │
│         └────────────┘       │                                      │
│                  ┌── ZONE B ─│─┐                                    │
│                  │           │ │                                    │
│                  │       ✓───│─▼                                    │
│                  │           │ │                                    │
│                  └───────────│─┘                                    │
│                              ▼                                      │
│                         ROUTE crosses                               │
│                         Zone A and Zone B                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════╗
║               2dsphere GEOSPATIAL OPERATORS CHEAT SHEET               ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  $nearSphere                                                          ║
║  ───────────                                                          ║
║  • Finds documents NEAR a point                                       ║
║  • Results SORTED by distance (closest first)                         ║
║  • Use $maxDistance to limit radius                                   ║
║  • Query with: Point only                                             ║
║                                                                       ║
║  $geoWithin                                                           ║
║  ──────────                                                           ║
║  • Finds documents INSIDE a boundary                                  ║
║  • Results NOT sorted                                                 ║
║  • Query with: Polygon, Circle ($centerSphere)                        ║
║  • Use for: "Find all in this zone"                                   ║
║                                                                       ║
║  $geoIntersects                                                       ║
║  ──────────────                                                       ║
║  • Finds documents that OVERLAP with query geometry                   ║
║  • Results NOT sorted                                                 ║
║  • Query with: Point, LineString, Polygon                             ║
║  • Use for: "Does this cross/touch that?"                             ║
║                                                                       ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  REMEMBER:                                                            ║
║  • Only $nearSphere sorts results                                     ║
║  • All operators require 2dsphere index                               ║
║  • Distances are always in METERS                                     ║
║  • Coordinates are always [longitude, latitude]                       ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```