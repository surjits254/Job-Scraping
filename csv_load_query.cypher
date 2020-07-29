LOAD CSV WITH HEADERS FROM "https://docs.google.com/spreadsheets/d/1MhlqTVUAgz2ZMRRQi0XkmPHaD8CRS_igE0mj7rZUHz8/export?format=csv&id=1MhlqTVUAgz2ZMRRQi0XkmPHaD8CRS_igE0mj7rZUHz8&gid=347262759" AS csvLine

MERGE (location:Location {name: csvLine.location})
MERGE (title:Job_Tile {name: csvLine.job_title, url:csvLine.url})
MERGE (type:Job_Type {name: coalesce(csvLine.type, "Unknown")})
MERGE (location)-[:HAS_JOB]->(title)
MERGE (title)-[:IS_OF_TYPE]->(type)
