<!-- # Geospatial Video: Visual Assets & Dataset Specification -->
<!-- ## Dataset: Food Delivery Platform (Austin, TX) -->
<!-- A unified dataset featuring iconic Austin restaurants and coffee shops that works across all three use cases. -->
<!-- ## Complete Sample Dataset -->

### Collection: `restaurants`

```javascript
// Document 1: Pinthouse Pizza (Burnet Road)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d1"),
  name: "Pinthouse Pizza",
  description: "Craft beer brewery and artisan pizzas with creative toppings and house-made ingredients",
  cuisine: "Pizza",
  rating: 4.7,
  priceRange: "$$",
  tags: ["pizza", "craft-beer", "brewery", "family-friendly", "outdoor seating"],

  location: {
    type: "Point",
    coordinates: [-97.738530, 30.295840]
  },

  address: {
    street: "4729 Burnet Road",
    city: "Austin",
    state: "TX",
    zip: "78756"
  },

  hours: {
    monday: "11:00-22:00",
    tuesday: "11:00-22:00",
    wednesday: "11:00-22:00",
    thursday: "11:00-23:00",
    friday: "11:00-24:00",
    saturday: "11:00-24:00",
    sunday: "11:00-21:00"
  }
}

// Document 2: Clay Pit (Downtown - Guadalupe)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d2"),
  name: "Clay Pit",
  description: "Upscale Indian cuisine featuring tandoori specialties and regional curries in a historic building",
  cuisine: "Indian",
  rating: 4.5,
  priceRange: "$$$",
  tags: ["indian", "tandoori", "curry", "fine-dining", "historic", "vegetarian-options"],

  location: {
    type: "Point",
    coordinates: [-97.742130, 30.270150]
  },

  address: {
    street: "1601 Guadalupe Street",
    city: "Austin",
    state: "TX",
    zip: "78701"
  },

  hours: {
    monday: "11:00-14:30, 17:00-22:00",
    tuesday: "11:00-14:30, 17:00-22:00",
    wednesday: "11:00-14:30, 17:00-22:00",
    thursday: "11:00-14:30, 17:00-22:00",
    friday: "11:00-14:30, 17:00-23:00",
    saturday: "11:00-23:00",
    sunday: "11:00-21:00"
  }
}

// Document 3: Torchy's Tacos (Downtown - Congress Ave)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d3"),
  name: "Torchy's Tacos",
  description: "Damn good tacos with creative recipes and signature queso, born in Austin",
  cuisine: "Tex-Mex",
  rating: 4.4,
  priceRange: "$",
  tags: ["tacos", "tex-mex", "queso", "breakfast-tacos", "casual", "local-favorite"],

  location: {
    type: "Point",
    coordinates: [-97.744820, 30.265730]
  },

  address: {
    street: "801 Congress Avenue",
    city: "Austin",
    state: "TX",
    zip: "78701"
  },

  hours: {
    monday: "07:00-22:00",
    tuesday: "07:00-22:00",
    wednesday: "07:00-22:00",
    thursday: "07:00-22:00",
    friday: "07:00-23:00",
    saturday: "07:00-23:00",
    sunday: "07:00-22:00"
  }
}

// Document 4: Ramen Tatsu-Ya (North Lamar)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d4"),
  name: "Ramen Tatsu-Ya",
  description: "Authentic Japanese ramen with rich tonkotsu broth and handmade noodles",
  cuisine: "Japanese",
  rating: 4.8,
  priceRange: "$$",
  tags: ["ramen", "japanese", "noodles", "late-night", "umami"],

  location: {
    type: "Point",
    coordinates: [-97.723180, 30.296520]
  },

  address: {
    street: "8557 Research Boulevard",
    city: "Austin",
    state: "TX",
    zip: "78758"
  },

  hours: {
    monday: "11:00-22:00",
    tuesday: "11:00-22:00",
    wednesday: "11:00-22:00",
    thursday: "11:00-22:00",
    friday: "11:00-23:00",
    saturday: "11:00-23:00",
    sunday: "11:00-22:00"
  }
}

// Document 5: Texas Chili Parlor (Downtown - Lavaca)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d5"),
  name: "Texas Chili Parlor",
  description: "Legendary Austin dive bar serving award-winning chili and cold beer since 1976",
  cuisine: "American",
  rating: 4.3,
  priceRange: "$",
  tags: ["chili", "dive-bar", "historic", "beer", "casual", "austin-legend"],

  location: {
    type: "Point",
    coordinates: [-97.740890, 30.272530]
  },

  address: {
    street: "1409 Lavaca Street",
    city: "Austin",
    state: "TX",
    zip: "78701"
  },

  hours: {
    monday: "11:00-02:00",
    tuesday: "11:00-02:00",
    wednesday: "11:00-02:00",
    thursday: "11:00-02:00",
    friday: "11:00-02:00",
    saturday: "11:00-02:00",
    sunday: "12:00-24:00"
  }
}

// Document 6: Home Slice Pizza (North Loop)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d6"),
  name: "Home Slice Pizza",
  description: "New York-style pizza by the slice with a funky Austin vibe",
  cuisine: "Pizza",
  rating: 4.6,
  priceRange: "$",
  tags: ["pizza", "new-york-style", "late-night", "casual", "local-favorite"],

  location: {
    type: "Point",
    coordinates: [-97.724270, 30.318650]
  },

  address: {
    street: "501 East 53rd Street",
    city: "Austin",
    state: "TX",
    zip: "78751"
  },

  hours: {
    monday: "11:00-23:00",
    tuesday: "11:00-23:00",
    wednesday: "11:00-23:00",
    thursday: "11:00-23:00",
    friday: "11:00-24:00",
    saturday: "11:00-24:00",
    sunday: "11:00-23:00"
  }
}

// Document 7: Voodoo Doughnut (6th Street)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d7"),
  name: "Voodoo Doughnut",
  description: "Iconic doughnut shop with wild creations and a keep Austin weird attitude",
  cuisine: "Dessert",
  rating: 4.2,
  priceRange: "$",
  tags: ["doughnuts", "dessert", "late-night", "quirky", "instagram-worthy"],

  location: {
    type: "Point",
    coordinates: [-97.739410, 30.267240]
  },

  address: {
    street: "212 East 6th Street",
    city: "Austin",
    state: "TX",
    zip: "78701"
  },

  hours: {
    monday: "00:00-23:59",
    tuesday: "00:00-23:59",
    wednesday: "00:00-23:59",
    thursday: "00:00-23:59",
    friday: "00:00-23:59",
    saturday: "00:00-23:59",
    sunday: "00:00-23:59"
  }
}

// Document 8: Amy's Ice Creams (Downtown - 6th Street)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d8"),
  name: "Amy's Ice Creams",
  description: "Beloved Austin original with handcrafted ice cream and famous crush'n toppings",
  cuisine: "Dessert",
  rating: 4.7,
  priceRange: "$",
  tags: ["ice-cream", "dessert", "local-favorite", "handcrafted", "family-friendly"],

  location: {
    type: "Point",
    coordinates: [-97.742350, 30.267890]
  },

  address: {
    street: "1012 West 6th Street",
    city: "Austin",
    state: "TX",
    zip: "78703"
  },

  hours: {
    monday: "11:30-23:00",
    tuesday: "11:30-23:00",
    wednesday: "11:30-23:00",
    thursday: "11:30-23:00",
    friday: "11:30-24:00",
    saturday: "11:30-24:00",
    sunday: "11:30-23:00"
  }
}

// Document 9: Mozart's Coffee Roasters (Lake Austin)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d9"),
  name: "Mozart's Coffee Roasters",
  description: "Lakeside coffee house with stunning views, fresh-roasted beans, and decadent desserts",
  cuisine: "Coffee",
  rating: 4.6,
  priceRange: "$$",
  tags: ["coffee", "lakeside", "dessert", "wifi", "scenic", "outdoor seating", "pastries"],

  location: {
    type: "Point",
    coordinates: [-97.785230, 30.296840]
  },

  address: {
    street: "3825 Lake Austin Boulevard",
    city: "Austin",
    state: "TX",
    zip: "78703"
  },

  hours: {
    monday: "07:00-23:00",
    tuesday: "07:00-23:00",
    wednesday: "07:00-23:00",
    thursday: "07:00-23:00",
    friday: "07:00-24:00",
    saturday: "07:00-24:00",
    sunday: "07:00-23:00"
  }
}

// Document 10: Epoch Coffee (North Loop)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0da"),
  name: "Epoch Coffee",
  description: "24-hour neighborhood coffee shop with a bohemian vibe and strong local following",
  cuisine: "Coffee",
  rating: 4.5,
  priceRange: "$",
  tags: ["coffee", "24-hours", "wifi", "late-night", "bohemian", "local-favorite", "study-spot"],

  location: {
    type: "Point",
    coordinates: [-97.722940, 30.318920]
  },

  address: {
    street: "221 West North Loop Boulevard",
    city: "Austin",
    state: "TX",
    zip: "78751"
  },

  hours: {
    monday: "00:00-23:59",
    tuesday: "00:00-23:59",
    wednesday: "00:00-23:59",
    thursday: "00:00-23:59",
    friday: "00:00-23:59",
    saturday: "00:00-23:59",
    sunday: "00:00-23:59"
  }
}

// Document 11: Flightpath Coffeehouse (Hyde Park - Duval Street)
{
  _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0db"),
  name: "Flightpath Coffeehouse",
  description: "Cozy Hyde Park coffee spot with vintage airport decor, local art, and community vibes",
  cuisine: "Coffee",
  rating: 4.4,
  priceRange: "$",
  tags: ["coffee", "wifi", "vintage", "local-art", "community", "hyde-park", "breakfast"],

  location: {
    type: "Point",
    coordinates: [-97.726580, 30.304720]
  },

  address: {
    street: "5013 Duval Street",
    city: "Austin",
    state: "TX",
    zip: "78751"
  },

  hours: {
    monday: "06:30-22:00",
    tuesday: "06:30-22:00",
    wednesday: "06:30-22:00",
    thursday: "06:30-22:00",
    friday: "06:30-23:00",
    saturday: "07:00-23:00",
    sunday: "07:00-22:00"
  }
}
```

### Collection: `warehouse_items` (For 2d Index Demo)

```javascript
// Restaurant supply warehouse uses a 100x100 meter grid system
{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d1"),
  sku: "FLOUR-AP-25LB",
  name: "All-Purpose Flour",
  category: "dry-goods",
  quantity: 150,
  pos: [23.5, 67.2]  // Legacy coordinate pair: [x, y] in meters
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d2"),
  sku: "TOMATO-CRUSHED-10",
  name: "Crushed San Marzano Tomatoes",
  category: "canned-goods",
  quantity: 200,
  pos: [24.1, 68.5]
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d3"),
  sku: "CHEESE-MOZZ-FRESH",
  name: "Fresh Mozzarella",
  category: "refrigerated",
  quantity: 75,
  pos: [12.3, 89.1]
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d4"),
  sku: "CHILE-ANCHO-DRIED",
  name: "Dried Ancho Chiles",
  category: "dry-goods",
  quantity: 50,
  pos: { x: 25.0, y: 65.8 }  // Alternative: embedded document format
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d5"),
  sku: "TORTILLA-CORN-6IN",
  name: "Corn Tortillas 6-inch",
  category: "refrigerated",
  quantity: 300,
  pos: [14.2, 87.3]
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d6"),
  sku: "QUESO-BLEND-5LB",
  name: "Texas Queso Cheese Blend",
  category: "refrigerated",
  quantity: 120,
  pos: [15.8, 85.9]
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d7"),
  sku: "COFFEE-BEAN-ETHIOPIAN",
  name: "Ethiopian Single Origin Beans",
  category: "dry-goods",
  quantity: 80,
  pos: [26.2, 64.5]
}

{
  _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d8"),
  sku: "SYRUP-VANILLA-750ML",
  name: "Vanilla Flavoring Syrup",
  category: "beverages",
  quantity: 45,
  pos: [28.0, 66.1]
}
```

### Collection: `delivery_zones` (For Polygon Demo)

```javascript
// Downtown Austin Zone
{
  _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d1"),
  name: "Downtown Austin Zone",
  deliveryFee: 2.99,
  estimatedTime: "15-25 min",
  boundary: {
    type: "Polygon",
    coordinates: [[
      [-97.755, 30.280],
      [-97.730, 30.280],
      [-97.730, 30.260],
      [-97.755, 30.260],
      [-97.755, 30.280]  // Closes the polygon
    ]]
  }
}

// North Loop / Hyde Park Zone
{
  _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d2"),
  name: "North Loop Zone",
  deliveryFee: 3.49,
  estimatedTime: "20-30 min",
  boundary: {
    type: "Polygon",
    coordinates: [[
      [-97.745, 30.325],
      [-97.715, 30.325],
      [-97.715, 30.295],
      [-97.745, 30.295],
      [-97.745, 30.325]
    ]]
  }
}

// Lake Austin / Tarrytown Zone
{
  _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d3"),
  name: "Lake Austin Zone",
  deliveryFee: 4.99,
  estimatedTime: "25-40 min",
  boundary: {
    type: "Polygon",
    coordinates: [[
      [-97.800, 30.310],
      [-97.770, 30.310],
      [-97.770, 30.285],
      [-97.800, 30.285],
      [-97.800, 30.310]
    ]]
  }
}

// UT Campus / Central Zone
{
  _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d4"),
  name: "UT Campus Zone",
  deliveryFee: 2.49,
  estimatedTime: "15-20 min",
  boundary: {
    type: "Polygon",
    coordinates: [[
      [-97.750, 30.295],
      [-97.730, 30.295],
      [-97.730, 30.280],
      [-97.750, 30.280],
      [-97.750, 30.295]
    ]]
  }
}
```

### Collection: `delivery_routes` (For $geoIntersects Demo)

```javascript
// Active delivery from Epoch Coffee to a customer in Hyde Park
{
  _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d1"),
  driverId: "DRV-ATX-1042",
  status: "active",
  orderId: "ORD-78751-001",
  restaurant: "Epoch Coffee",
  route: {
    type: "LineString",
    coordinates: [
      [-97.722940, 30.318920],  // Start: Epoch Coffee
      [-97.724500, 30.315000],  // Waypoint 1: Heading south
      [-97.726000, 30.310000],  // Waypoint 2
      [-97.727500, 30.305500]   // End: Customer near Flightpath
    ]
  }
}

// Active delivery from Downtown to North Loop
{
  _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d2"),
  driverId: "DRV-ATX-2187",
  status: "active",
  orderId: "ORD-78756-002",
  restaurant: "Clay Pit",
  route: {
    type: "LineString",
    coordinates: [
      [-97.742130, 30.270150],  // Start: Clay Pit (Downtown)
      [-97.740000, 30.280000],  // Waypoint 1: Heading north
      [-97.738000, 30.290000],  // Waypoint 2: Crossing into UT area
      [-97.738530, 30.295840]   // End: Near Pinthouse Pizza
    ]
  }
}

// Active delivery from Mozart's across town
{
  _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d3"),
  driverId: "DRV-ATX-3391",
  status: "active",
  orderId: "ORD-78703-003",
  restaurant: "Mozart's Coffee Roasters",
  route: {
    type: "LineString",
    coordinates: [
      [-97.785230, 30.296840],  // Start: Mozart's (Lake Austin)
      [-97.770000, 30.290000],  // Waypoint 1: Heading east
      [-97.755000, 30.280000],  // Waypoint 2: Approaching Downtown
      [-97.742350, 30.267890]   // End: Near Amy's Ice Creams (Downtown)
    ]
  }
}

// Active delivery from Torchy's Downtown to customer nearby
{
  _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d4"),
  driverId: "DRV-ATX-4456",
  status: "active",
  orderId: "ORD-78701-004",
  restaurant: "Torchy's Tacos",
  route: {
    type: "LineString",
    coordinates: [
      [-97.744820, 30.265730],  // Start: Torchy's (Downtown Congress)
      [-97.742000, 30.267000],  // Waypoint 1: Heading to 6th
      [-97.740000, 30.268500],  // Waypoint 2
      [-97.739410, 30.267240]   // End: Near Voodoo Doughnut
    ]
  }
}
```

---

## Visual Assets by Section

### Opening Hook

| Visual ID | Description | Specifications |
|-----------|-------------|----------------|
| `HOOK-01` | Split screen layout | Left 40%: JSON document (use Clay Pit). Right 60%: Three stacked map views |
| `HOOK-02` | Grid map thumbnail | Simple 2D warehouse grid with dots representing items |
| `HOOK-03` | Globe map thumbnail | Spherical map of Austin with restaurant/coffee pins |
| `HOOK-04` | Search interface thumbnail | Search bar with "breakfast tacos" and map results |

---

### Use Case 1: Flat Surfaces (2d Index)

| Visual ID | Description | Content |
|-----------|-------------|---------|
| `2D-01` | Section title card | "Use Case 1: Flat Surfaces" with grid icon |
| `2D-02` | Legacy pairs comparison | Code editor showing both formats side by side |
| `2D-03` | Warehouse floor plan | Top-down grid view (100x100m) with labeled sections |
| `2D-04` | Index creation terminal | Dark terminal with command |
| `2D-05` | Query animation | Show picker location, radius expanding, items highlighting |
| `2D-06` | Results display | Terminal showing sorted results with distances |

**Visual `2D-02` Content:**
```javascript
// Array format (recommended)
pos: [23.5, 67.2]

// Embedded document format
pos: { x: 23.5, y: 67.2 }

// ⚠️ First value = x-axis (longitude equivalent)
// ⚠️ Second value = y-axis (latitude equivalent)
```

**Visual `2D-03` Warehouse Layout:**
```
┌─────────────────────────────────────────────────────────┐
│  RESTAURANT SUPPLY WAREHOUSE (100m x 100m)              │
├─────────────┬──────────────┬────────────────────────────┤
│             │              │                            │
│  DRY GOODS  │    CANNED    │       REFRIGERATED         │
│ (20-30, 60-75) (20-30, 75-90)    (10-20, 80-95)         │
│   ◉ Flour   │  ◉ Tomatoes  │      ◉ Mozzarella          │
│   ◉ Chiles  │              │      ◉ Tortillas           │
│   ◉ Coffee  │              │      ◉ Queso               │
│   ◉ Syrup   │              │                            │
├─────────────┼──────────────┼────────────────────────────┤
│             │              │                            │
│   SPICES    │   PRODUCE    │         LOADING            │
│ (40-60, 20-40) (60-90, 30-60)         DOCK              │
│             │              │                            │
│             │              │                            │
├─────────────┴──────────────┴────────────────────────────┤
│  ★ PICKER LOCATION (25, 65)                             │
│  ◉ = Inventory Item    ★ = Current Position             │
└─────────────────────────────────────────────────────────┘
```

**Visual `2D-04` Terminal Content:**
```javascript
// Create 2d index for flat-surface queries
db.warehouse_items.createIndex({ pos: "2d" })
```

**Visual `2D-05` Query Content:**
```javascript
// Find items nearest to picker at position [25, 65]
db.warehouse_items.find({
  pos: {
    $near: [25, 65],
    $maxDistance: 10  // Within 10 meters
  }
})
```

**Visual `2D-06` Results Content:**
```javascript
// Results sorted by distance (closest first)
[
  { sku: "CHILE-ANCHO-DRIED", name: "Dried Ancho Chiles",
    pos: [25.0, 65.8], distance: 0.8 },
  { sku: "COFFEE-BEAN-ETHIOPIAN", name: "Ethiopian Single Origin Beans",
    pos: [26.2, 64.5], distance: 1.3 },
  { sku: "SYRUP-VANILLA-750ML", name: "Vanilla Flavoring Syrup",
    pos: [28.0, 66.1], distance: 3.2 },
  { sku: "FLOUR-AP-25LB", name: "All-Purpose Flour",
    pos: [23.5, 67.2], distance: 2.6 }
]
```

---

### Use Case 2: Spherical Math (2dsphere Index)

| Visual ID | Description | Content |
|-----------|-------------|---------|
| `SPHERE-01` | Section title card | "Use Case 2: Spherical Math" with globe icon |
| `SPHERE-02` | GeoJSON Point structure | Annotated code block |
| `SPHERE-03` | GeoJSON Polygon structure | Annotated code block |
| `SPHERE-04` | Austin map with all locations | Map showing all 11 restaurant/coffee pins |
| `SPHERE-05` | Index creation terminal | Dark terminal with command |
| `SPHERE-06` | $nearSphere visual | Map showing user location at Texas Capitol + radius + sorted pins |
| `SPHERE-07` | $geoWithin visual | Map showing Downtown zone polygon with contained restaurants |
| `SPHERE-08` | $geoIntersects visual | Map showing delivery route from Torchy's crossing Downtown zone |

**Visual `SPHERE-02` Content:**
```javascript
// GeoJSON Point (Torchy's Tacos Downtown location)
{
  location: {
    type: "Point",           // ← Required type field
    coordinates: [           // ← Required coordinates array
      -97.744820,            // ← Longitude FIRST
      30.265730              // ← Latitude SECOND
    ]
  }
}
```

**Visual `SPHERE-03` Content:**
```javascript
// GeoJSON Polygon (Downtown Austin Delivery Zone)
{
  boundary: {
    type: "Polygon",
    coordinates: [[          // ← Note: nested array
      [-97.755, 30.280],     // ← Point 1 (NW corner)
      [-97.730, 30.280],     // ← Point 2 (NE corner)
      [-97.730, 30.260],     // ← Point 3 (SE corner)
      [-97.755, 30.260],     // ← Point 4 (SW corner)
      [-97.755, 30.280]      // ← Point 5 (closes polygon)
    ]]                       //   Must match Point 1!
  }
}
```

**Visual `SPHERE-04` Austin Map Pin Locations:**
```
Restaurant & Coffee Pins for Austin Map:
┌────────────────────────────────────────────────────────────┐
│                                                            │
│    ◉ Epoch Coffee (30.318, -97.722) [24hr]                │
│    ◉ Home Slice Pizza (30.318, -97.724)                   │
│                    [NORTH LOOP ZONE]                       │
│                                                            │
│    ◉ Flightpath Coffeehouse (30.304, -97.726)             │
│                    [HYDE PARK]                             │
│                                                            │
├──────────────────────────────┬─────────────────────────────┤
│                              │                             │
│  ◉ Mozart's Coffee           │  ◉ Pinthouse Pizza          │
│    (30.296, -97.785)         │    (30.295, -97.738)        │
│      [LAKE AUSTIN ZONE]      │  ◉ Ramen Tatsu-Ya           │
│                              │    (30.296, -97.723)        │
│                              │      [UT CAMPUS ZONE]       │
│                              │                             │
├──────────────────────────────┴─────────────────────────────┤
│                                                            │
│              ◉ Texas Chili Parlor (30.272, -97.740)       │
│              ◉ Clay Pit (30.270, -97.742)                 │
│              ◉ Amy's Ice Creams (30.267, -97.742)         │
│              ◉ Voodoo Doughnut (30.267, -97.739)          │
│              ◉ Torchy's Tacos (30.265, -97.744)           │
│                    [DOWNTOWN ZONE]                         │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Visual `SPHERE-05` Terminal Content:**
```javascript
// Create 2dsphere index for spherical queries
db.restaurants.createIndex({ location: "2dsphere" })

// Result
{
  "createdCollectionAutomatically": false,
  "numIndexesBefore": 1,
  "numIndexesAfter": 2,
  "ok": 1
}
```

**Visual `SPHERE-06` Query Content:**
```javascript
// Find restaurants within 800 meters of Texas State Capitol
db.restaurants.find({
  location: {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]  // Texas Capitol
      },
      $maxDistance: 800  // ← Distance in METERS
    }
  }
})

// Returns (sorted by distance):
// 1. Texas Chili Parlor (~250m)
// 2. Clay Pit (~520m)
// 3. Amy's Ice Creams (~760m)
// 4. Voodoo Doughnut (~780m)
```

**Visual `SPHERE-07` Query Content:**
```javascript
// Find restaurants within Downtown Austin delivery zone
db.restaurants.find({
  location: {
    $geoWithin: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [-97.755, 30.280],
          [-97.730, 30.280],
          [-97.730, 30.260],
          [-97.755, 30.260],
          [-97.755, 30.280]
        ]]
      }
    }
  }
})

// Returns:
// - Clay Pit
// - Texas Chili Parlor
// - Voodoo Doughnut
// - Amy's Ice Creams
// - Torchy's Tacos
```

**Visual `SPHERE-08` Query Content:**
```javascript
// Check if delivery route passes through Downtown zone
db.delivery_zones.find({
  boundary: {
    $geoIntersects: {
      $geometry: {
        type: "LineString",
        coordinates: [
          [-97.744820, 30.265730],  // Start: Torchy's
          [-97.742000, 30.267000],
          [-97.740000, 30.268500],
          [-97.739410, 30.267240]   // End: Near Voodoo Doughnut
        ]
      }
    }
  }
})

// Returns: Downtown Austin Zone (route stays within boundary)
```

---

### Use Case 3: MongoDB Search

| Visual ID | Description | Content |
|-----------|-------------|---------|
| `SEARCH-01` | Section title card | "Use Case 3: Atlas Search" with magnifying glass + map icon |
| `SEARCH-02` | Atlas UI screenshot | Search index creation interface |
| `SEARCH-03` | Index definition JSON | Full index configuration |
| `SEARCH-04` | Combined query visual | Split: search bar with "tacos breakfast queso" + map with filtered results |
| `SEARCH-05` | geoShape query code | Complete aggregation pipeline |
| `SEARCH-06` | Results with scoring | Results showing Torchy's with relevance scores |

**Visual `SEARCH-03` Content:**
```javascript
// Atlas Search Index Definition
{
  "analyzer": "lucene.standard",
  "mappings": {
    "dynamic": false,
    "fields": {
      "name": {
        "type": "string",
        "analyzer": "lucene.standard"
      },
      "description": {
        "type": "string",
        "analyzer": "lucene.english"
      },
      "cuisine": {
        "type": "stringFacet"
      },
      "location": {
        "type": "geo"
      },
      "tags": {
        "type": "token"
      }
    }
  }
}
```

**Visual `SEARCH-05` Content:**
```javascript
// Find "tacos" or "breakfast" spots within 1km of Texas Capitol
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
              center: {
                type: "Point",
                coordinates: [-97.740310, 30.274670]  // Texas Capitol
              },
              radius: 1500  // ← Radius in METERS
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

**Visual `SEARCH-06` Results Content:**
```javascript
// Results with relevance scores
[
  {
    name: "Torchy's Tacos",
    description: "Damn good tacos with creative recipes and signature queso...",
    cuisine: "Tex-Mex",
    tags: ["tacos", "tex-mex", "queso", "breakfast-tacos", "casual", "local-favorite"],
    score: 14.234  // High score: matches "tacos", "breakfast", AND "queso"
  },
  {
    name: "Voodoo Doughnut",
    description: "Iconic doughnut shop with wild creations...",
    cuisine: "Dessert",
    tags: ["doughnuts", "dessert", "late-night", "quirky"],
    score: 2.112  // Lower score: partial match only
  }
]
```

---

### Closing

| Visual ID | Description | Content |
|-----------|-------------|---------|
| `CLOSE-01` | Three-column summary | Icons for each use case with key operator |
| `CLOSE-02` | Documentation CTA | MongoDB docs links with QR code |
| `CLOSE-03` | End card | MongoDB logo + "Jumpstart: Geospatial Data" |

**Visual `CLOSE-01` Content:**
```
┌─────────────────┬─────────────────┬─────────────────┐
│   FLAT GRIDS    │    SPHERICAL    │  ADV. SEARCH    │
│                 │                 │                 │
│       ⊞         │       🌐        │       🔍        │
│                 │                 │                 │
│   2d index      │  2dsphere index │   geo type      │
│                 │                 │                 │
│                 │                 │                 │
│   $near         │  $nearSphere    │   geoShape      │
│                 │  $geoWithin     │   geoWithin     │
│                 │  $geoIntersects │                 │
│                 │                 │                 │
│                 │                 │                 │
│  Your units     │    Meters       │    Meters       │
└─────────────────┴─────────────────┴─────────────────┘
```

---

## Animation Sequences

### Animation 1: Warehouse Proximity Search (Use Case 1)
1. Warehouse grid appears with item dots
2. Picker location (★) drops at position [25, 65]
3. Circular radius expands from picker (10m)
4. Items within radius highlight sequentially (Ancho Chiles → Coffee Beans → Vanilla Syrup → Flour)
5. Distance labels appear next to each item

### Animation 2: Austin Downtown Proximity (Use Case 2)
1. Austin map loads with Texas Capitol marker highlighted
2. 800m radius circle expands from Capitol
3. Restaurant pins appear within radius: Texas Chili Parlor → Clay Pit → Amy's Ice Creams → Voodoo Doughnut
4. Pins outside radius (Torchy's at ~1km) remain grayed out
5. Distance labels show meters from Capitol

### Animation 3: Downtown Zone Containment (Use Case 2)
1. Downtown Austin zone polygon draws on map
2. All 11 location pins visible
3. Pins outside boundary (North Loop, Lake Austin, UT Campus) fade/gray out
4. Clay Pit, Texas Chili Parlor, Voodoo Doughnut, Amy's, and Torchy's pulse/highlight
5. Zone label "Downtown Austin Zone" appears

### Animation 4: Route Intersection (Use Case 2)
1. Downtown Austin zone polygon visible
2. Torchy's Tacos pin highlighted as origin
3. Route line draws point-by-point heading toward 6th Street
4. Route stays within Downtown zone boundary
5. "Route within Downtown Zone" label appears

### Animation 5: Combined Taco Search (Use Case 3)
1. Search bar appears with cursor
2. "tacos breakfast queso" types in
3. Map zooms to Texas Capitol location
4. 1.5km radius circle appears
5. Non-matching restaurants fade out
6. Torchy's Tacos highlights prominently
7. Score badge appears (Torchy's: 14.2)

---

## Color Palette Recommendation

| Element | Color | Hex |
|---------|-------|-----|
| MongoDB Green | Primary brand | `#00ED64` |
| Austin Orange | Local accent (UT) | `#BF5700` |
| Coffee Brown | Coffee shops | `#6F4E37` |
| User Location | Accent blue | `#1A73E8` |
| Search Radius | Transparent blue | `#1A73E833` |
| Polygon Fill | Transparent green | `#00ED6422` |
| Polygon Stroke | Solid green | `#00ED64` |
| Route Line | Austin orange | `#BF5700` |
| Highlighted Result | Yellow | `#FFD600` |
| Code Background | Dark gray | `#1E1E1E` |
| Terminal Background | Darker gray | `#0D0D0D` |

---

## File Deliverables Checklist

```
/visuals
  /01-hook
    HOOK-01-split-screen.png
    HOOK-02-grid-thumb.png
    HOOK-03-austin-globe-thumb.png
    HOOK-04-search-thumb.png

  /02-flat-surfaces
    2D-01-title-card.png
    2D-02-legacy-pairs.png
    2D-03-warehouse-layout.png
    2D-04-terminal-index.png
    2D-05-query-animation.mp4
    2D-06-results.png

  /03-spherical
    SPHERE-01-title-card.png
    SPHERE-02-geojson-point.png
    SPHERE-03-geojson-polygon.png
    SPHERE-04-austin-map.png
    SPHERE-05-terminal-index.png
    SPHERE-06-nearsphere-animation.mp4
    SPHERE-07-geowithin-animation.mp4
    SPHERE-08-geointersects-animation.mp4

  /04-atlas-search
    SEARCH-01-title-card.png
    SEARCH-02-atlas-ui.png
    SEARCH-03-index-definition.png
    SEARCH-04-combined-visual.png
    SEARCH-05-query-code.png
    SEARCH-06-results.png

  /05-closing
    CLOSE-01-summary.png
    CLOSE-02-cta.png
    CLOSE-03-end-card.png

/data
  restaurants.json
  warehouse_items.json
  delivery_zones.json
  delivery_routes.json
```

---

## Quick Reference: Austin Location Coordinates

### Downtown Restaurants

| Restaurant | Longitude | Latitude | Address |
|------------|-----------|----------|---------|
| Clay Pit | -97.742130 | 30.270150 | 1601 Guadalupe St |
| Texas Chili Parlor | -97.740890 | 30.272530 | 1409 Lavaca St |
| Voodoo Doughnut | -97.739410 | 30.267240 | 212 E 6th St |
| Amy's Ice Creams | -97.742350 | 30.267890 | 1012 W 6th St |
| Torchy's Tacos | -97.744820 | 30.265730 | 801 Congress Ave |

### North Loop / Hyde Park

| Restaurant | Longitude | Latitude | Address |
|------------|-----------|----------|---------|
| Epoch Coffee | -97.722940 | 30.318920 | 221 W North Loop Blvd |
| Home Slice Pizza | -97.724270 | 30.318650 | 501 E 53rd St |
| Flightpath Coffeehouse | -97.726580 | 30.304720 | 5013 Duval St |
| Pinthouse Pizza | -97.738530 | 30.295840 | 4729 Burnet Rd |
| Ramen Tatsu-Ya | -97.723180 | 30.296520 | 8557 Research Blvd |

### Lake Austin

| Restaurant | Longitude | Latitude | Address |
|------------|-----------|----------|---------|
| Mozart's Coffee | -97.785230 | 30.296840 | 3825 Lake Austin Blvd |

### Delivery Zones

| Zone | NW Corner | SE Corner | Restaurants Inside |
|------|-----------|-----------|-------------------|
| Downtown | -97.755, 30.280 | -97.730, 30.260 | Clay Pit, Texas Chili Parlor, Voodoo, Amy's, Torchy's |
| North Loop | -97.745, 30.325 | -97.715, 30.295 | Epoch, Home Slice, Flightpath, Pinthouse, Ramen Tatsu-Ya |
| Lake Austin | -97.800, 30.310 | -97.770, 30.285 | Mozart's |
| UT Campus | -97.750, 30.295 | -97.730, 30.280 | Pinthouse, Ramen Tatsu-Ya |

---

This gives you a complete Austin-themed dataset with accurate downtown locations for Torchy's and Amy's, plus the North Loop location for Home Slice, making all the geospatial demonstrations realistic and locally accurate.



# MongoDB Geospatial Use Cases: Complete mongosh Commands

## Setup: Create Database

```javascript
use geospatial_demo
```

---

## Use Case 1: Flat Surfaces (2d Index)

### Insert Data

```javascript
db.warehouse_items.insertMany()
```

### Create Index

```javascript
db.warehouse_items.createIndex({ pos: "2d" })
```

### Example Queries

```javascript
// Query 1: Find items nearest to picker at position [25, 65]
// Returns results sorted by distance (closest first)
db.warehouse_items.find({
  pos: {
    $near: [25, 65]
  }
})
```

```javascript
// Query 2: Find items within 5 meters of picker
db.warehouse_items.find({
  pos: {
    $near: [25, 65],
    $maxDistance: 5
  }
})
```

```javascript
// Query 3: Find items within a rectangular area (box)
// Useful for searching within a specific warehouse zone
db.warehouse_items.find({
  pos: {
    $geoWithin: {
      $box: [
        [20, 60],   // Bottom-left corner
        [30, 70]    // Top-right corner
      ]
    }
  }
})
```

```javascript
// Query 4: Find items within a circular area
// Center: [25, 65], Radius: 10 meters
db.warehouse_items.find({
  pos: {
    $geoWithin: {
      $center: [
        [25, 65],   // Center point
        10          // Radius in coordinate units (meters)
      ]
    }
  }
})
```

```javascript
// Query 5: Find items within a polygon (custom zone shape)
db.warehouse_items.find({
  pos: {
    $geoWithin: {
      $polygon: [
        [10, 60],
        [30, 60],
        [30, 90],
        [10, 90]
      ]
    }
  }
})
```

### Verify Results

```javascript
// Check index was created
db.warehouse_items.getIndexes()

// Count documents
db.warehouse_items.countDocuments()
```

---

## Use Case 2: Spherical Math (2dsphere Index)

### Insert Restaurants

```javascript
db.restaurants.insertMany([
  {
    name: "Pinthouse Pizza",
    description: "Craft beer brewery and artisan pizzas with creative toppings and house-made ingredients",
    cuisine: "Pizza",
    rating: 4.7,
    priceRange: "$$",
    tags: ["pizza", "craft-beer", "brewery", "family-friendly", "outdoor seating"],
    location: {
      type: "Point",
      coordinates: [-97.738530, 30.295840]
    },
    address: {
      street: "4729 Burnet Road",
      city: "Austin",
      state: "TX",
      zip: "78756"
    }
  },
  {
    name: "Clay Pit",
    description: "Upscale Indian cuisine featuring tandoori specialties and regional curries in a historic building",
    cuisine: "Indian",
    rating: 4.5,
    priceRange: "$$$",
    tags: ["indian", "tandoori", "curry", "fine-dining", "historic", "vegetarian-options"],
    location: {
      type: "Point",
      coordinates: [-97.742130, 30.270150]
    },
    address: {
      street: "1601 Guadalupe Street",
      city: "Austin",
      state: "TX",
      zip: "78701"
    }
  },
  {
    name: "Torchy's Tacos",
    description: "Damn good tacos with creative recipes and signature queso, born in Austin",
    cuisine: "Tex-Mex",
    rating: 4.4,
    priceRange: "$",
    tags: ["tacos", "tex-mex", "queso", "breakfast-tacos", "casual", "local-favorite"],
    location: {
      type: "Point",
      coordinates: [-97.744820, 30.265730]
    },
    address: {
      street: "801 Congress Avenue",
      city: "Austin",
      state: "TX",
      zip: "78701"
    }
  },
  {
    name: "Ramen Tatsu-Ya",
    description: "Authentic Japanese ramen with rich tonkotsu broth and handmade noodles",
    cuisine: "Japanese",
    rating: 4.8,
    priceRange: "$$",
    tags: ["ramen", "japanese", "noodles", "late-night", "umami"],
    location: {
      type: "Point",
      coordinates: [-97.723180, 30.296520]
    },
    address: {
      street: "8557 Research Boulevard",
      city: "Austin",
      state: "TX",
      zip: "78758"
    }
  },
  {
    name: "Texas Chili Parlor",
    description: "Legendary Austin dive bar serving award-winning chili and cold beer since 1976",
    cuisine: "American",
    rating: 4.3,
    priceRange: "$",
    tags: ["chili", "dive-bar", "historic", "beer", "casual", "austin-legend"],
    location: {
      type: "Point",
      coordinates: [-97.740890, 30.272530]
    },
    address: {
      street: "1409 Lavaca Street",
      city: "Austin",
      state: "TX",
      zip: "78701"
    }
  },
  {
    name: "Home Slice Pizza",
    description: "New York-style pizza by the slice with a funky Austin vibe",
    cuisine: "Pizza",
    rating: 4.6,
    priceRange: "$",
    tags: ["pizza", "new-york-style", "late-night", "casual", "local-favorite"],
    location: {
      type: "Point",
      coordinates: [-97.724270, 30.318650]
    },
    address: {
      street: "501 East 53rd Street",
      city: "Austin",
      state: "TX",
      zip: "78751"
    }
  },
  {
    name: "Voodoo Doughnut",
    description: "Iconic doughnut shop with wild creations and a keep Austin weird attitude",
    cuisine: "Dessert",
    rating: 4.2,
    priceRange: "$",
    tags: ["doughnuts", "dessert", "late-night", "quirky", "instagram-worthy"],
    location: {
      type: "Point",
      coordinates: [-97.739410, 30.267240]
    },
    address: {
      street: "212 East 6th Street",
      city: "Austin",
      state: "TX",
      zip: "78701"
    }
  },
  {
    name: "Amy's Ice Creams",
    description: "Beloved Austin original with handcrafted ice cream and famous crush'n toppings",
    cuisine: "Dessert",
    rating: 4.7,
    priceRange: "$",
    tags: ["ice-cream", "dessert", "local-favorite", "handcrafted", "family-friendly"],
    location: {
      type: "Point",
      coordinates: [-97.742350, 30.267890]
    },
    address: {
      street: "1012 West 6th Street",
      city: "Austin",
      state: "TX",
      zip: "78703"
    }
  },
  {
    name: "Mozart's Coffee Roasters",
    description: "Lakeside coffee house with stunning views, fresh-roasted beans, and decadent desserts",
    cuisine: "Coffee",
    rating: 4.6,
    priceRange: "$$",
    tags: ["coffee", "lakeside", "dessert", "wifi", "scenic", "outdoor seating", "pastries"],
    location: {
      type: "Point",
      coordinates: [-97.785230, 30.296840]
    },
    address: {
      street: "3825 Lake Austin Boulevard",
      city: "Austin",
      state: "TX",
      zip: "78703"
    }
  },
  {
    name: "Epoch Coffee",
    description: "24-hour neighborhood coffee shop with a bohemian vibe and strong local following",
    cuisine: "Coffee",
    rating: 4.5,
    priceRange: "$",
    tags: ["coffee", "24-hours", "wifi", "late-night", "bohemian", "local-favorite", "study-spot"],
    location: {
      type: "Point",
      coordinates: [-97.722940, 30.318920]
    },
    address: {
      street: "221 West North Loop Boulevard",
      city: "Austin",
      state: "TX",
      zip: "78751"
    }
  },
  {
    name: "Flightpath Coffeehouse",
    description: "Cozy Hyde Park coffee spot with vintage airport decor, local art, and community vibes",
    cuisine: "Coffee",
    rating: 4.4,
    priceRange: "$",
    tags: ["coffee", "wifi", "vintage", "local-art", "community", "hyde-park", "breakfast"],
    location: {
      type: "Point",
      coordinates: [-97.726580, 30.304720]
    },
    address: {
      street: "5013 Duval Street",
      city: "Austin",
      state: "TX",
      zip: "78751"
    }
  }
])
```

### Insert Delivery Zones

```javascript
db.delivery_zones.insertMany([
  {
    name: "Downtown Austin Zone",
    deliveryFee: 2.99,
    estimatedTime: "15-25 min",
    boundary: {
      type: "Polygon",
      coordinates: [[
        [-97.755, 30.280],
        [-97.730, 30.280],
        [-97.730, 30.260],
        [-97.755, 30.260],
        [-97.755, 30.280]
      ]]
    }
  },
  {
    name: "North Loop Zone",
    deliveryFee: 3.49,
    estimatedTime: "20-30 min",
    boundary: {
      type: "Polygon",
      coordinates: [[
        [-97.745, 30.325],
        [-97.715, 30.325],
        [-97.715, 30.295],
        [-97.745, 30.295],
        [-97.745, 30.325]
      ]]
    }
  },
  {
    name: "Lake Austin Zone",
    deliveryFee: 4.99,
    estimatedTime: "25-40 min",
    boundary: {
      type: "Polygon",
      coordinates: [[
        [-97.800, 30.310],
        [-97.770, 30.310],
        [-97.770, 30.285],
        [-97.800, 30.285],
        [-97.800, 30.310]
      ]]
    }
  },
  {
    name: "UT Campus Zone",
    deliveryFee: 2.49,
    estimatedTime: "15-20 min",
    boundary: {
      type: "Polygon",
      coordinates: [[
        [-97.750, 30.295],
        [-97.730, 30.295],
        [-97.730, 30.280],
        [-97.750, 30.280],
        [-97.750, 30.295]
      ]]
    }
  }
])
```

### Insert Delivery Routes

```javascript
db.delivery_routes.insertMany([
  {
    driverId: "DRV-ATX-1042",
    status: "active",
    orderId: "ORD-78751-001",
    restaurant: "Epoch Coffee",
    route: {
      type: "LineString",
      coordinates: [
        [-97.722940, 30.318920],
        [-97.724500, 30.315000],
        [-97.726000, 30.310000],
        [-97.727500, 30.305500]
      ]
    }
  },
  {
    driverId: "DRV-ATX-2187",
    status: "active",
    orderId: "ORD-78756-002",
    restaurant: "Clay Pit",
    route: {
      type: "LineString",
      coordinates: [
        [-97.742130, 30.270150],
        [-97.740000, 30.280000],
        [-97.738000, 30.290000],
        [-97.738530, 30.295840]
      ]
    }
  },
  {
    driverId: "DRV-ATX-3391",
    status: "active",
    orderId: "ORD-78703-003",
    restaurant: "Mozart's Coffee Roasters",
    route: {
      type: "LineString",
      coordinates: [
        [-97.785230, 30.296840],
        [-97.770000, 30.290000],
        [-97.755000, 30.280000],
        [-97.742350, 30.267890]
      ]
    }
  },
  {
    driverId: "DRV-ATX-4456",
    status: "active",
    orderId: "ORD-78701-004",
    restaurant: "Torchy's Tacos",
    route: {
      type: "LineString",
      coordinates: [
        [-97.744820, 30.265730],
        [-97.742000, 30.267000],
        [-97.740000, 30.268500],
        [-97.739410, 30.267240]
      ]
    }
  }
])
```

### Create Indexes

```javascript
// Index for restaurants
db.restaurants.createIndex({ location: "2dsphere" })

// Index for delivery zones
db.delivery_zones.createIndex({ boundary: "2dsphere" })

// Index for delivery routes
db.delivery_routes.createIndex({ route: "2dsphere" })
```

### Example Queries

#### $nearSphere - Sorted Proximity

```javascript
// Query 1: Find restaurants within 800 meters of Texas State Capitol
// Results are automatically sorted by distance (closest first)
db.restaurants.find({
  location: {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]  // Texas Capitol
      },
      $maxDistance: 800  // Distance in meters
    }
  }
}, {
  name: 1,
  cuisine: 1,
  "address.street": 1,
  _id: 0
})
```

```javascript
// Query 2: Find the 3 closest restaurants to a user location
db.restaurants.find({
  location: {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]
      }
    }
  }
}, {
  name: 1,
  cuisine: 1,
  _id: 0
}).limit(3)
```

#### $geoWithin - Containment (No Sort)

```javascript
// Query 3: Find restaurants within Downtown Austin delivery zone
// Note: Results are NOT sorted by distance
db.restaurants.find({
  location: {
    $geoWithin: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [-97.755, 30.280],
          [-97.730, 30.280],
          [-97.730, 30.260],
          [-97.755, 30.260],
          [-97.755, 30.280]
        ]]
      }
    }
  }
}, {
  name: 1,
  cuisine: 1,
  _id: 0
})
```

```javascript
// Query 4: Find restaurants within a circular area (1.5km radius)
// Using $centerSphere for spherical calculations
db.restaurants.find({
  location: {
    $geoWithin: {
      $centerSphere: [
        [-97.740310, 30.274670],  // Center: Texas Capitol
        1.5 / 6378.1              // Radius in radians (1.5km / Earth's radius in km)
      ]
    }
  }
}, {
  name: 1,
  cuisine: 1,
  _id: 0
})
```

#### $geoIntersects - Overlap Detection

```javascript
// Query 5: Find delivery zones that a specific route passes through
db.delivery_zones.find({
  boundary: {
    $geoIntersects: {
      $geometry: {
        type: "LineString",
        coordinates: [
          [-97.742130, 30.270150],  // Start: Clay Pit
          [-97.740000, 30.280000],  // Heading north
          [-97.738000, 30.290000],  // Crossing zones
          [-97.738530, 30.295840]   // End: Pinthouse area
        ]
      }
    }
  }
}, {
  name: 1,
  deliveryFee: 1,
  _id: 0
})
```

```javascript
// Query 6: Check if a customer location is within any delivery zone
db.delivery_zones.find({
  boundary: {
    $geoIntersects: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]  // Customer location
      }
    }
  }
}, {
  name: 1,
  deliveryFee: 1,
  estimatedTime: 1,
  _id: 0
})
```

```javascript
// Query 7: Find all active delivery routes that pass through Downtown zone
db.delivery_routes.find({
  route: {
    $geoIntersects: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [-97.755, 30.280],
          [-97.730, 30.280],
          [-97.730, 30.260],
          [-97.755, 30.260],
          [-97.755, 30.280]
        ]]
      }
    }
  }
}, {
  driverId: 1,
  restaurant: 1,
  status: 1,
  _id: 0
})
```

#### Aggregation with $geoNear

```javascript
// Query 8: Find restaurants with calculated distance using aggregation
db.restaurants.aggregate([
  {
    $geoNear: {
      near: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]  // Texas Capitol
      },
      distanceField: "distance",       // Field to store calculated distance
      maxDistance: 2000,               // 2km max
      spherical: true,                 // Use spherical geometry
      distanceMultiplier: 0.001        // Convert meters to kilometers
    }
  },
  {
    $project: {
      name: 1,
      cuisine: 1,
      distance_km: { $round: ["$distance", 2] },
      _id: 0
    }
  }
])
```

```javascript
// Query 9: Find nearest pizza places with distance
db.restaurants.aggregate([
  {
    $geoNear: {
      near: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]
      },
      distanceField: "distance",
      query: { cuisine: "Pizza" },     // Filter by cuisine
      spherical: true
    }
  },
  {
    $project: {
      name: 1,
      distance_meters: { $round: ["$distance", 0] },
      _id: 0
    }
  }
])
```

### Verify Results

```javascript
// Check indexes
db.restaurants.getIndexes()
db.delivery_zones.getIndexes()
db.delivery_routes.getIndexes()

// Count documents
print("Restaurants: " + db.restaurants.countDocuments())
print("Delivery Zones: " + db.delivery_zones.countDocuments())
print("Delivery Routes: " + db.delivery_routes.countDocuments())
```

---

## Use Case 3: Atlas Search (geoWithin)

> **Note:** Atlas Search requires MongoDB Atlas. These commands will only work on an Atlas cluster with a Search index configured.

### Data Setup

Use the same `restaurants` collection from Use Case 2. If you haven't inserted it yet:

```javascript
// Use the restaurants insertMany from Use Case 2 above
```

### Create Atlas Search Index

Create this index in the Atlas UI (Database > Search > Create Index):

**Index Name:** `restaurants_geo_search`

**Index Definition:**
```json
{
  "mappings": {
    "dynamic": false,
    "fields": {
      "name": {
        "type": "string",
        "analyzer": "lucene.standard"
      },
      "description": {
        "type": "string",
        "analyzer": "lucene.english"
      },
      "cuisine": {
        "type": "stringFacet"
      },
      "location": {
        "type": "geo"
      },
      "tags": {
        "type": "token"
      },
      "rating": {
        "type": "number"
      }
    }
  }
}
```

### Example Queries

```javascript
// Query 1: Search for "breakfast tacos" within 1.5km of Texas Capitol
db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_geo_search",
      compound: {
        must: [
          {
            text: {
              query: "breakfast tacos",
              path: ["name", "description", "tags"],
              fuzzy: {
                maxEdits: 1
              }
            }
          }
        ],
        filter: [
          {
            geoWithin: {
              path: "location",
              circle: {
                center: {
                  type: "Point",
                  coordinates: [-97.740310, 30.274670]  // Texas Capitol
                },
                radius: 1500  // Radius in meters
              }
            }
          }
        ]
      }
    }
  },
  {
    $project: {
      name: 1,
      description: 1,
      cuisine: 1,
      tags: 1,
      "address.street": 1,
      score: { $meta: "searchScore" },
      _id: 0
    }
  }
])
```

```javascript
// Query 2: Search for "pizza" within Downtown Austin polygon
db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_geo_search",
      compound: {
        must: [
          {
            text: {
              query: "pizza",
              path: ["name", "description", "tags"]
            }
          }
        ],
        filter: [
          {
            geoWithin: {
              path: "location",
              geometry: {
                type: "Polygon",
                coordinates: [[
                  [-97.755, 30.280],
                  [-97.730, 30.280],
                  [-97.730, 30.260],
                  [-97.755, 30.260],
                  [-97.755, 30.280]
                ]]
              }
            }
          }
        ]
      }
    }
  },
  {
    $project: {
      name: 1,
      cuisine: 1,
      score: { $meta: "searchScore" },
      _id: 0
    }
  }
])
```

```javascript
// Query 3: Search for "coffee wifi" within 3km, sorted by relevance
db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_geo_search",
      compound: {
        must: [
          {
            text: {
              query: "coffee wifi",
              path: ["name", "description", "tags"],
              fuzzy: {
                maxEdits: 1
              }
            }
          }
        ],
        filter: [
          {
            geoWithin: {
              path: "location",
              circle: {
                center: {
                  type: "Point",
                  coordinates: [-97.722940, 30.318920]  // North Loop area
                },
                radius: 3000
              }
            }
          }
        ]
      }
    }
  },
  {
    $project: {
      name: 1,
      description: 1,
      tags: 1,
      score: { $meta: "searchScore" },
      _id: 0
    }
  }
])
```

```javascript
// Query 4: Combine text search with geo filter and minimum rating
db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_geo_search",
      compound: {
        must: [
          {
            text: {
              query: "tacos",
              path: ["name", "description", "tags"]
            }
          }
        ],
        filter: [
          {
            geoWithin: {
              path: "location",
              circle: {
                center: {
                  type: "Point",
                  coordinates: [-97.740310, 30.274670]
                },
                radius: 2000
              }
            }
          },
          {
            range: {
              path: "rating",
              gte: 4.0
            }
          }
        ]
      }
    }
  },
  {
    $project: {
      name: 1,
      rating: 1,
      cuisine: 1,
      score: { $meta: "searchScore" },
      _id: 0
    }
  }
])
```

```javascript
// Query 5: Search with boosted scoring for specific terms
db.restaurants.aggregate([
  {
    $search: {
      index: "restaurants_geo_search",
      compound: {
        should: [
          {
            text: {
              query: "local-favorite",
              path: "tags",
              score: { boost: { value: 3 } }
            }
          },
          {
            text: {
              query: "Austin",
              path: "description",
              score: { boost: { value: 2 } }
            }
          }
        ],
        filter: [
          {
            geoWithin: {
              path: "location",
              circle: {
                center: {
                  type: "Point",
                  coordinates: [-97.740310, 30.274670]
                },
                radius: 5000
              }
            }
          }
        ]
      }
    }
  },
  {
    $limit: 5
  },
  {
    $project: {
      name: 1,
      tags: 1,
      score: { $meta: "searchScore" },
      _id: 0
    }
  }
])
```

```javascript
// Query 6: Faceted search with geo filter
db.restaurants.aggregate([
  {
    $searchMeta: {
      index: "restaurants_geo_search",
      facet: {
        operator: {
          geoWithin: {
            path: "location",
            circle: {
              center: {
                type: "Point",
                coordinates: [-97.740310, 30.274670]
              },
              radius: 3000
            }
          }
        },
        facets: {
          cuisineTypes: {
            type: "string",
            path: "cuisine"
          }
        }
      }
    }
  }
])
```

---

## Complete Setup Script

Run this entire script to set up all three use cases at once:

```javascript
// ============================================
// GEOSPATIAL DEMO - COMPLETE SETUP
// ============================================

use geospatial_demo

// Drop existing collections (optional)
db.warehouse_items.drop()
db.restaurants.drop()
db.delivery_zones.drop()
db.delivery_routes.drop()

print("\n📦 Setting up Use Case 1: Warehouse (2d Index)...\n")

// --------------------------------------------
// USE CASE 1: WAREHOUSE ITEMS (2d)
// --------------------------------------------
db.warehouse_items.insertMany([
  { sku: "FLOUR-AP-25LB", name: "All-Purpose Flour", category: "dry-goods", quantity: 150, pos: [23.5, 67.2] },
  { sku: "TOMATO-CRUSHED-10", name: "Crushed San Marzano Tomatoes", category: "canned-goods", quantity: 200, pos: [24.1, 68.5] },
  { sku: "CHEESE-MOZZ-FRESH", name: "Fresh Mozzarella", category: "refrigerated", quantity: 75, pos: [12.3, 89.1] },
  { sku: "CHILE-ANCHO-DRIED", name: "Dried Ancho Chiles", category: "dry-goods", quantity: 50, pos: { x: 25.0, y: 65.8 } },
  { sku: "TORTILLA-CORN-6IN", name: "Corn Tortillas 6-inch", category: "refrigerated", quantity: 300, pos: [14.2, 87.3] },
  { sku: "QUESO-BLEND-5LB", name: "Texas Queso Cheese Blend", category: "refrigerated", quantity: 120, pos: [15.8, 85.9] },
  { sku: "COFFEE-BEAN-ETHIOPIAN", name: "Ethiopian Single Origin Beans", category: "dry-goods", quantity: 80, pos: [26.2, 64.5] },
  { sku: "SYRUP-VANILLA-750ML", name: "Vanilla Flavoring Syrup", category: "beverages", quantity: 45, pos: [28.0, 66.1] }
])

db.warehouse_items.createIndex({ pos: "2d" })

print("✅ Warehouse items inserted and indexed\n")

print("🍕 Setting up Use Case 2: Restaurants (2dsphere Index)...\n")

// --------------------------------------------
// USE CASE 2: RESTAURANTS (2dsphere)
// --------------------------------------------
db.restaurants.insertMany([
  { name: "Pinthouse Pizza", description: "Craft beer brewery and artisan pizzas with creative toppings and house-made ingredients", cuisine: "Pizza", rating: 4.7, priceRange: "$$", tags: ["pizza", "craft-beer", "brewery", "family-friendly", "outdoor seating"], location: { type: "Point", coordinates: [-97.738530, 30.295840] }, address: { street: "4729 Burnet Road", city: "Austin", state: "TX", zip: "78756" } },
  { name: "Clay Pit", description: "Upscale Indian cuisine featuring tandoori specialties and regional curries in a historic building", cuisine: "Indian", rating: 4.5, priceRange: "$$$", tags: ["indian", "tandoori", "curry", "fine-dining", "historic", "vegetarian-options"], location: { type: "Point", coordinates: [-97.742130, 30.270150] }, address: { street: "1601 Guadalupe Street", city: "Austin", state: "TX", zip: "78701" } },
  { name: "Torchy's Tacos", description: "Damn good tacos with creative recipes and signature queso, born in Austin", cuisine: "Tex-Mex", rating: 4.4, priceRange: "$", tags: ["tacos", "tex-mex", "queso", "breakfast-tacos", "casual", "local-favorite"], location: { type: "Point", coordinates: [-97.744820, 30.265730] }, address: { street: "801 Congress Avenue", city: "Austin", state: "TX", zip: "78701" } },
  { name: "Ramen Tatsu-Ya", description: "Authentic Japanese ramen with rich tonkotsu broth and handmade noodles", cuisine: "Japanese", rating: 4.8, priceRange: "$$", tags: ["ramen", "japanese", "noodles", "late-night", "umami"], location: { type: "Point", coordinates: [-97.723180, 30.296520] }, address: { street: "8557 Research Boulevard", city: "Austin", state: "TX", zip: "78758" } },
  { name: "Texas Chili Parlor", description: "Legendary Austin dive bar serving award-winning chili and cold beer since 1976", cuisine: "American", rating: 4.3, priceRange: "$", tags: ["chili", "dive-bar", "historic", "beer", "casual", "austin-legend"], location: { type: "Point", coordinates: [-97.740890, 30.272530] }, address: { street: "1409 Lavaca Street", city: "Austin", state: "TX", zip: "78701" } },
  { name: "Home Slice Pizza", description: "New York-style pizza by the slice with a funky Austin vibe", cuisine: "Pizza", rating: 4.6, priceRange: "$", tags: ["pizza", "new-york-style", "late-night", "casual", "local-favorite"], location: { type: "Point", coordinates: [-97.724270, 30.318650] }, address: { street: "501 East 53rd Street", city: "Austin", state: "TX", zip: "78751" } },
  { name: "Voodoo Doughnut", description: "Iconic doughnut shop with wild creations and a keep Austin weird attitude", cuisine: "Dessert", rating: 4.2, priceRange: "$", tags: ["doughnuts", "dessert", "late-night", "quirky", "instagram-worthy"], location: { type: "Point", coordinates: [-97.739410, 30.267240] }, address: { street: "212 East 6th Street", city: "Austin", state: "TX", zip: "78701" } },
  { name: "Amy's Ice Creams", description: "Beloved Austin original with handcrafted ice cream and famous crush'n toppings", cuisine: "Dessert", rating: 4.7, priceRange: "$", tags: ["ice-cream", "dessert", "local-favorite", "handcrafted", "family-friendly"], location: { type: "Point", coordinates: [-97.742350, 30.267890] }, address: { street: "1012 West 6th Street", city: "Austin", state: "TX", zip: "78703" } },
  { name: "Mozart's Coffee Roasters", description: "Lakeside coffee house with stunning views, fresh-roasted beans, and decadent desserts", cuisine: "Coffee", rating: 4.6, priceRange: "$$", tags: ["coffee", "lakeside", "dessert", "wifi", "scenic", "outdoor seating", "pastries"], location: { type: "Point", coordinates: [-97.785230, 30.296840] }, address: { street: "3825 Lake Austin Boulevard", city: "Austin", state: "TX", zip: "78703" } },
  { name: "Epoch Coffee", description: "24-hour neighborhood coffee shop with a bohemian vibe and strong local following", cuisine: "Coffee", rating: 4.5, priceRange: "$", tags: ["coffee", "24-hours", "wifi", "late-night", "bohemian", "local-favorite", "study-spot"], location: { type: "Point", coordinates: [-97.722940, 30.318920] }, address: { street: "221 West North Loop Boulevard", city: "Austin", state: "TX", zip: "78751" } },
  { name: "Flightpath Coffeehouse", description: "Cozy Hyde Park coffee spot with vintage airport decor, local art, and community vibes", cuisine: "Coffee", rating: 4.4, priceRange: "$", tags: ["coffee", "wifi", "vintage", "local-art", "community", "hyde-park", "breakfast"], location: { type: "Point", coordinates: [-97.726580, 30.304720] }, address: { street: "5013 Duval Street", city: "Austin", state: "TX", zip: "78751" } }
])

db.restaurants.createIndex({ location: "2dsphere" })

print("✅ Restaurants inserted and indexed\n")

print("🚗 Setting up delivery zones and routes...\n")

// --------------------------------------------
// DELIVERY ZONES
// --------------------------------------------
db.delivery_zones.insertMany([
  { name: "Downtown Austin Zone", deliveryFee: 2.99, estimatedTime: "15-25 min", boundary: { type: "Polygon", coordinates: [[[-97.755, 30.280], [-97.730, 30.280], [-97.730, 30.260], [-97.755, 30.260], [-97.755, 30.280]]] } },
  { name: "North Loop Zone", deliveryFee: 3.49, estimatedTime: "20-30 min", boundary: { type: "Polygon", coordinates: [[[-97.745, 30.325], [-97.715, 30.325], [-97.715, 30.295], [-97.745, 30.295], [-97.745, 30.325]]] } },
  { name: "Lake Austin Zone", deliveryFee: 4.99, estimatedTime: "25-40 min", boundary: { type: "Polygon", coordinates: [[[-97.800, 30.310], [-97.770, 30.310], [-97.770, 30.285], [-97.800, 30.285], [-97.800, 30.310]]] } },
  { name: "UT Campus Zone", deliveryFee: 2.49, estimatedTime: "15-20 min", boundary: { type: "Polygon", coordinates: [[[-97.750, 30.295], [-97.730, 30.295], [-97.730, 30.280], [-97.750, 30.280], [-97.750, 30.295]]] } }
])

db.delivery_zones.createIndex({ boundary: "2dsphere" })

// --------------------------------------------
// DELIVERY ROUTES
// --------------------------------------------
db.delivery_routes.insertMany([
  { driverId: "DRV-ATX-1042", status: "active", orderId: "ORD-78751-001", restaurant: "Epoch Coffee", route: { type: "LineString", coordinates: [[-97.722940, 30.318920], [-97.724500, 30.315000], [-97.726000, 30.310000], [-97.727500, 30.305500]] } },
  { driverId: "DRV-ATX-2187", status: "active", orderId: "ORD-78756-002", restaurant: "Clay Pit", route: { type: "LineString", coordinates: [[-97.742130, 30.270150], [-97.740000, 30.280000], [-97.738000, 30.290000], [-97.738530, 30.295840]] } },
  { driverId: "DRV-ATX-3391", status: "active", orderId: "ORD-78703-003", restaurant: "Mozart's Coffee Roasters", route: { type: "LineString", coordinates: [[-97.785230, 30.296840], [-97.770000, 30.290000], [-97.755000, 30.280000], [-97.742350, 30.267890]] } },
  { driverId: "DRV-ATX-4456", status: "active", orderId: "ORD-78701-004", restaurant: "Torchy's Tacos", route: { type: "LineString", coordinates: [[-97.744820, 30.265730], [-97.742000, 30.267000], [-97.740000, 30.268500], [-97.739410, 30.267240]] } }
])

db.delivery_routes.createIndex({ route: "2dsphere" })

print("✅ Delivery zones and routes inserted and indexed\n")

// --------------------------------------------
// VERIFICATION
// --------------------------------------------
print("============================================")
print("           SETUP COMPLETE!                  ")
print("============================================\n")

print("📊 Document Counts:")
print("   - Warehouse Items: " + db.warehouse_items.countDocuments())
print("   - Restaurants: " + db.restaurants.countDocuments())
print("   - Delivery Zones: " + db.delivery_zones.countDocuments())
print("   - Delivery Routes: " + db.delivery_routes.countDocuments())

print("\n📑 Indexes Created:")
print("   - warehouse_items.pos: 2d")
print("   - restaurants.location: 2dsphere")
print("   - delivery_zones.boundary: 2dsphere")
print("   - delivery_routes.route: 2dsphere")

print("\n🚀 Ready to run example queries!")
print("\n⚠️  Note: Use Case 3 (Atlas Search) requires:")
print("   1. MongoDB Atlas cluster")
print("   2. Create Search index named 'restaurants_geo_search'")
print("   3. See index definition in the documentation")
```

---

## Quick Test Commands

After running the setup, test each use case:

```javascript
// Test Use Case 1: 2d Index
db.warehouse_items.find({ pos: { $near: [25, 65], $maxDistance: 5 } }, { name: 1, pos: 1, _id: 0 })

// Test Use Case 2: 2dsphere - $nearSphere
db.restaurants.find({ location: { $nearSphere: { $geometry: { type: "Point", coordinates: [-97.740310, 30.274670] }, $maxDistance: 800 } } }, { name: 1, _id: 0 })

// Test Use Case 2: 2dsphere - $geoWithin
db.restaurants.find({ location: { $geoWithin: { $geometry: { type: "Polygon", coordinates: [[[-97.755, 30.280], [-97.730, 30.280], [-97.730, 30.260], [-97.755, 30.260], [-97.755, 30.280]]] } } } }, { name: 1, _id: 0 })

// Test Use Case 2: 2dsphere - $geoIntersects
db.delivery_zones.find({ boundary: { $geoIntersects: { $geometry: { type: "Point", coordinates: [-97.740310, 30.274670] } } } }, { name: 1, _id: 0 })
```