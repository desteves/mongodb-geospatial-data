Set Shell zsh
Set FontSize 14
Set CursorBlink false
Set FontFamily "SpaceMono Nerd Font"
Set Width 1920
Set Height 1080
Set Margin 20
Set MarginFill "#00684A"
Set BorderRadius 10
Set TypingSpeed 150ms
Require glow
Require mongosh

Copy "glow visuals/a02-flatgrids.md"
Paste
Enter
Sleep 5s
Copy " --port 27000 --quiet"
Type "mongosh"
Paste
Sleep 1s
Enter
Copy "// Geospatial Data / Flat Grid / Data Model"
Paste
Sleep 1s
Enter
Type "db.warehouse_items.find({},{_id:0, pos: 1})"
Enter
Sleep 1s
Copy "// Geospatial Data / Flat Grid / Index"
Enter
Sleep 1s
Type "db.warehouse_items.createIndex({ pos: '2d' })"
Enter
Sleep 1s
Copy "// Geospatial Data / Flat Grid / Query / $near"
Paste
Sleep 1s
Copy "// Note: Results will be sorted by distance."
Paste
Enter
Sleep 1s
Enter
Type "var filter = {"
Enter
Type "  pos: {"
Enter
Type "    $near: [25, 65],"
Enter
Type "    $maxDistance: 5"
Enter
Type "  }"
Enter
Type "};"
Enter
Type "var projection = { pos: 1, name: 1, _id: 0 };"
Enter
Type "db.warehouse_items.find(filter, projection)"
Enter
Sleep 3s
Type "// Geospatial Data / 2D Use Case / Query / $geoWithin"
Enter
Sleep 1s
Copy "Note: Results will NOT be sorted."
Paste
Enter
Sleep 1s
Type "var filter = {"
Enter
Type "  pos: {"
Enter
Type "    $geoWithin: {"
Enter
Type "      $center: [[25, 65], 5]"
Enter
Type "    }"
Enter
Type "  }"
Enter
Type "};"
Enter
Type "db.warehouse_items.find(filter, projection)"
Enter
Sleep 3s
Type "exit"
Enter