LOAD CSV WITH HEADERS FROM "<FIle URL>" AS csvLine

MERGE (location:Location {name: csvLine.location})
MERGE (title:Job_Tile {name: csvLine.job_title, url:csvLine.url})
MERGE (type:Job_Type {name: coalesce(csvLine.type, "Unknown")})
MERGE (location)-[:HAS_JOB]->(title)
MERGE (title)-[:IS_OF_TYPE]->(type)
