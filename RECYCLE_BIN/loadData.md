# MongoDB insertMany Commands for Austin Geospatial Dataset

## Collection: `restaurants`

```javascript
db.restaurants.insertMany()
```

---

## Collection: `warehouse_items`

```javascript
db.warehouse_items.insertMany()
```

---

## Collection: `delivery_zones`

```javascript
db.delivery_zones.insertMany()
```

---

## Collection: `delivery_routes`

```javascript
db.delivery_routes.insertMany([
  {
    _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d1"),
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
    _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d2"),
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
    _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d3"),
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
    _id: ObjectId("64d1f2b3c4d5e6f7a8b9c0d4"),
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

---

## Create Indexes

```javascript
// 2dsphere index for restaurants collection
db.restaurants.createIndex({ location: "2dsphere" })

// 2dsphere index for delivery_zones collection
db.delivery_zones.createIndex({ boundary: "2dsphere" })

// 2dsphere index for delivery_routes collection
db.delivery_routes.createIndex({ route: "2dsphere" })

// 2d index for warehouse_items collection (flat surface)
db.warehouse_items.createIndex({ pos: "2d" })
```

---

## Verify Data Insertion

```javascript
// Check document counts
print("Restaurants: " + db.restaurants.countDocuments())
print("Warehouse Items: " + db.warehouse_items.countDocuments())
print("Delivery Zones: " + db.delivery_zones.countDocuments())
print("Delivery Routes: " + db.delivery_routes.countDocuments())

// Expected output:
// Restaurants: 11
// Warehouse Items: 8
// Delivery Zones: 4
// Delivery Routes: 4
```

---

## Quick Test Queries

```javascript
// Test 2dsphere: Find restaurants near Texas Capitol
db.restaurants.find({
  location: {
    $nearSphere: {
      $geometry: {
        type: "Point",
        coordinates: [-97.740310, 30.274670]
      },
      $maxDistance: 800
    }
  }
}, { name: 1, _id: 0 })

// Test 2d: Find warehouse items near picker position
db.warehouse_items.find({
  pos: {
    $near: [25, 65],
    $maxDistance: 5
  }
}, { name: 1, pos: 1, _id: 0 })

// Test $geoWithin: Find restaurants in Downtown zone
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
}, { name: 1, _id: 0 })

// Test $geoIntersects: Find zones that a delivery route passes through
db.delivery_zones.find({
  boundary: {
    $geoIntersects: {
      $geometry: {
        type: "LineString",
        coordinates: [
          [-97.742130, 30.270150],
          [-97.740000, 30.280000],
          [-97.738000, 30.290000],
          [-97.738530, 30.295840]
        ]
      }
    }
  }
}, { name: 1, _id: 0 })
```

---

## Complete Setup Script

Copy and paste this entire block to set up everything at once:

```javascript
// ============================================
// AUSTIN GEOSPATIAL DATASET - COMPLETE SETUP
// ============================================

// Drop existing collections (optional - uncomment if needed)
// db.restaurants.drop()
// db.warehouse_items.drop()
// db.delivery_zones.drop()
// db.delivery_routes.drop()

// --------------------------------------------
// INSERT RESTAURANTS
// --------------------------------------------
db.restaurants.insertMany([
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d1"),
    name: "Pinthouse Pizza",
    description: "Craft beer brewery and artisan pizzas with creative toppings and house-made ingredients",
    cuisine: "Pizza",
    rating: 4.7,
    priceRange: "$$",
    tags: ["pizza", "craft-beer", "brewery", "family-friendly", "outdoor seating"],
    location: { type: "Point", coordinates: [-97.738530, 30.295840] },
    address: { street: "4729 Burnet Road", city: "Austin", state: "TX", zip: "78756" },
    hours: { monday: "11:00-22:00", tuesday: "11:00-22:00", wednesday: "11:00-22:00", thursday: "11:00-23:00", friday: "11:00-24:00", saturday: "11:00-24:00", sunday: "11:00-21:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d2"),
    name: "Clay Pit",
    description: "Upscale Indian cuisine featuring tandoori specialties and regional curries in a historic building",
    cuisine: "Indian",
    rating: 4.5,
    priceRange: "$$$",
    tags: ["indian", "tandoori", "curry", "fine-dining", "historic", "vegetarian-options"],
    location: { type: "Point", coordinates: [-97.742130, 30.270150] },
    address: { street: "1601 Guadalupe Street", city: "Austin", state: "TX", zip: "78701" },
    hours: { monday: "11:00-14:30, 17:00-22:00", tuesday: "11:00-14:30, 17:00-22:00", wednesday: "11:00-14:30, 17:00-22:00", thursday: "11:00-14:30, 17:00-22:00", friday: "11:00-14:30, 17:00-23:00", saturday: "11:00-23:00", sunday: "11:00-21:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d3"),
    name: "Torchy's Tacos",
    description: "Damn good tacos with creative recipes and signature queso, born in Austin",
    cuisine: "Tex-Mex",
    rating: 4.4,
    priceRange: "$",
    tags: ["tacos", "tex-mex", "queso", "breakfast-tacos", "casual", "local-favorite"],
    location: { type: "Point", coordinates: [-97.744820, 30.265730] },
    address: { street: "801 Congress Avenue", city: "Austin", state: "TX", zip: "78701" },
    hours: { monday: "07:00-22:00", tuesday: "07:00-22:00", wednesday: "07:00-22:00", thursday: "07:00-22:00", friday: "07:00-23:00", saturday: "07:00-23:00", sunday: "07:00-22:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d4"),
    name: "Ramen Tatsu-Ya",
    description: "Authentic Japanese ramen with rich tonkotsu broth and handmade noodles",
    cuisine: "Japanese",
    rating: 4.8,
    priceRange: "$$",
    tags: ["ramen", "japanese", "noodles", "late-night", "umami"],
    location: { type: "Point", coordinates: [-97.723180, 30.296520] },
    address: { street: "8557 Research Boulevard", city: "Austin", state: "TX", zip: "78758" },
    hours: { monday: "11:00-22:00", tuesday: "11:00-22:00", wednesday: "11:00-22:00", thursday: "11:00-22:00", friday: "11:00-23:00", saturday: "11:00-23:00", sunday: "11:00-22:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d5"),
    name: "Texas Chili Parlor",
    description: "Legendary Austin dive bar serving award-winning chili and cold beer since 1976",
    cuisine: "American",
    rating: 4.3,
    priceRange: "$",
    tags: ["chili", "dive-bar", "historic", "beer", "casual", "austin-legend"],
    location: { type: "Point", coordinates: [-97.740890, 30.272530] },
    address: { street: "1409 Lavaca Street", city: "Austin", state: "TX", zip: "78701" },
    hours: { monday: "11:00-02:00", tuesday: "11:00-02:00", wednesday: "11:00-02:00", thursday: "11:00-02:00", friday: "11:00-02:00", saturday: "11:00-02:00", sunday: "12:00-24:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d6"),
    name: "Home Slice Pizza",
    description: "New York-style pizza by the slice with a funky Austin vibe",
    cuisine: "Pizza",
    rating: 4.6,
    priceRange: "$",
    tags: ["pizza", "new-york-style", "late-night", "casual", "local-favorite"],
    location: { type: "Point", coordinates: [-97.724270, 30.318650] },
    address: { street: "501 East 53rd Street", city: "Austin", state: "TX", zip: "78751" },
    hours: { monday: "11:00-23:00", tuesday: "11:00-23:00", wednesday: "11:00-23:00", thursday: "11:00-23:00", friday: "11:00-24:00", saturday: "11:00-24:00", sunday: "11:00-23:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d7"),
    name: "Voodoo Doughnut",
    description: "Iconic doughnut shop with wild creations and a keep Austin weird attitude",
    cuisine: "Dessert",
    rating: 4.2,
    priceRange: "$",
    tags: ["doughnuts", "dessert", "late-night", "quirky", "instagram-worthy"],
    location: { type: "Point", coordinates: [-97.739410, 30.267240] },
    address: { street: "212 East 6th Street", city: "Austin", state: "TX", zip: "78701" },
    hours: { monday: "00:00-23:59", tuesday: "00:00-23:59", wednesday: "00:00-23:59", thursday: "00:00-23:59", friday: "00:00-23:59", saturday: "00:00-23:59", sunday: "00:00-23:59" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d8"),
    name: "Amy's Ice Creams",
    description: "Beloved Austin original with handcrafted ice cream and famous crush'n toppings",
    cuisine: "Dessert",
    rating: 4.7,
    priceRange: "$",
    tags: ["ice-cream", "dessert", "local-favorite", "handcrafted", "family-friendly"],
    location: { type: "Point", coordinates: [-97.742350, 30.267890] },
    address: { street: "1012 West 6th Street", city: "Austin", state: "TX", zip: "78703" },
    hours: { monday: "11:30-23:00", tuesday: "11:30-23:00", wednesday: "11:30-23:00", thursday: "11:30-23:00", friday: "11:30-24:00", saturday: "11:30-24:00", sunday: "11:30-23:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0d9"),
    name: "Mozart's Coffee Roasters",
    description: "Lakeside coffee house with stunning views, fresh-roasted beans, and decadent desserts",
    cuisine: "Coffee",
    rating: 4.6,
    priceRange: "$$",
    tags: ["coffee", "lakeside", "dessert", "wifi", "scenic", "outdoor seating", "pastries"],
    location: { type: "Point", coordinates: [-97.785230, 30.296840] },
    address: { street: "3825 Lake Austin Boulevard", city: "Austin", state: "TX", zip: "78703" },
    hours: { monday: "07:00-23:00", tuesday: "07:00-23:00", wednesday: "07:00-23:00", thursday: "07:00-23:00", friday: "07:00-24:00", saturday: "07:00-24:00", sunday: "07:00-23:00" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0da"),
    name: "Epoch Coffee",
    description: "24-hour neighborhood coffee shop with a bohemian vibe and strong local following",
    cuisine: "Coffee",
    rating: 4.5,
    priceRange: "$",
    tags: ["coffee", "24-hours", "wifi", "late-night", "bohemian", "local-favorite", "study-spot"],
    location: { type: "Point", coordinates: [-97.722940, 30.318920] },
    address: { street: "221 West North Loop Boulevard", city: "Austin", state: "TX", zip: "78751" },
    hours: { monday: "00:00-23:59", tuesday: "00:00-23:59", wednesday: "00:00-23:59", thursday: "00:00-23:59", friday: "00:00-23:59", saturday: "00:00-23:59", sunday: "00:00-23:59" }
  },
  {
    _id: ObjectId("64a1f2b3c4d5e6f7a8b9c0db"),
    name: "Flightpath Coffeehouse",
    description: "Cozy Hyde Park coffee spot with vintage airport decor, local art, and community vibes",
    cuisine: "Coffee",
    rating: 4.4,
    priceRange: "$",
    tags: ["coffee", "wifi", "vintage", "local-art", "community", "hyde-park", "breakfast"],
    location: { type: "Point", coordinates: [-97.726580, 30.304720] },
    address: { street: "5013 Duval Street", city: "Austin", state: "TX", zip: "78751" },
    hours: { monday: "06:30-22:00", tuesday: "06:30-22:00", wednesday: "06:30-22:00", thursday: "06:30-22:00", friday: "06:30-23:00", saturday: "07:00-23:00", sunday: "07:00-22:00" }
  }
])

// --------------------------------------------
// INSERT WAREHOUSE ITEMS
// --------------------------------------------
db.warehouse_items.insertMany([
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d1"), sku: "FLOUR-AP-25LB", name: "All-Purpose Flour", category: "dry-goods", quantity: 150, pos: [23.5, 67.2] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d2"), sku: "TOMATO-CRUSHED-10", name: "Crushed San Marzano Tomatoes", category: "canned-goods", quantity: 200, pos: [24.1, 68.5] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d3"), sku: "CHEESE-MOZZ-FRESH", name: "Fresh Mozzarella", category: "refrigerated", quantity: 75, pos: [12.3, 89.1] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d4"), sku: "CHILE-ANCHO-DRIED", name: "Dried Ancho Chiles", category: "dry-goods", quantity: 50, pos: { x: 25.0, y: 65.8 } },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d5"), sku: "TORTILLA-CORN-6IN", name: "Corn Tortillas 6-inch", category: "refrigerated", quantity: 300, pos: [14.2, 87.3] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d6"), sku: "QUESO-BLEND-5LB", name: "Texas Queso Cheese Blend", category: "refrigerated", quantity: 120, pos: [15.8, 85.9] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d7"), sku: "COFFEE-BEAN-ETHIOPIAN", name: "Ethiopian Single Origin Beans", category: "dry-goods", quantity: 80, pos: [26.2, 64.5] },
  { _id: ObjectId("64b1f2b3c4d5e6f7a8b9c0d8"), sku: "SYRUP-VANILLA-750ML", name: "Vanilla Flavoring Syrup", category: "beverages", quantity: 45, pos: [28.0, 66.1] }
])

// --------------------------------------------
// INSERT DELIVERY ZONES
// --------------------------------------------
db.delivery_zones.insertMany([
  { _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d1"), name: "Downtown Austin Zone", deliveryFee: 2.99, estimatedTime: "15-25 min", boundary: { type: "Polygon", coordinates: [[[-97.755, 30.280], [-97.730, 30.280], [-97.730, 30.260], [-97.755, 30.260], [-97.755, 30.280]]] } },
  { _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d2"), name: "North Loop Zone", deliveryFee: 3.49, estimatedTime: "20-30 min", boundary: { type: "Polygon", coordinates: [[[-97.745, 30.325], [-97.715, 30.325], [-97.715, 30.295], [-97.745, 30.295], [-97.745, 30.325]]] } },
  { _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d3"), name: "Lake Austin Zone", deliveryFee: 4.99, estimatedTime: "25-40 min", boundary: { type: "Polygon", coordinates: [[[-97.800, 30.310], [-97.770, 30.310], [-97.770, 30.285], [-97.800, 30.285], [-97.800, 30.310]]] } },
  { _id: ObjectId("64c1f2b3c4d5e6f7a8b9c0d4"), name: "UT Campus Zone", deliveryFee: 2.49, estimatedTime: "15-20 min", boundary: { type: "Polygon", coordinates: [[[-97.750, 30.295], [-97.730, 30.295], [-97.730, 30.280], [-97.750, 30.280], [-97.750, 30.295]]] } }
])

// --------------------------------------------
// INSERT DELIVERY ROUTES
// --------------------------------------------
db.delivery_routes.insertMany([
  
])

// --------------------------------------------
// CREATE INDEXES
// --------------------------------------------
db.restaurants.createIndex({ location: "2dsphere" })
db.delivery_zones.createIndex({ boundary: "2dsphere" })
db.delivery_routes.createIndex({ route: "2dsphere" })
db.warehouse_items.createIndex({ pos: "2d" })

// --------------------------------------------
// VERIFY SETUP
// --------------------------------------------
print("\n✅ SETUP COMPLETE!\n")
print("Document counts:")
print("  - Restaurants: " + db.restaurants.countDocuments())
print("  - Warehouse Items: " + db.warehouse_items.countDocuments())
print("  - Delivery Zones: " + db.delivery_zones.countDocuments())
print("  - Delivery Routes: " + db.delivery_routes.countDocuments())
print("\nIndexes created:")
printjson(db.restaurants.getIndexes())
printjson(db.warehouse_items.getIndexes())
```

This complete setup script will insert all documents and create the necessary indexes in one execution. Simply paste it into mongosh to get your Austin geospatial dataset ready for the video demonstrations.