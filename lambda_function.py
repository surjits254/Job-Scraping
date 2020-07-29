import json
import requests

def lambda_handler(event, context):
    header = {"Content-type": "application/json", "Authorization": <Neo4j username:password>}
    query = {"statements" : [ {"statement" : "LOAD CSV WITH HEADERS FROM '<You S3 file signed url>' AS csvLine MERGE (location:Location {name: csvLine.location}) MERGE (title:Job_Tile {name: csvLine.job_title, url:csvLine.url}) MERGE (type:Job_Type {name: coalesce(csvLine.type, 'Unknown')}) MERGE (location)-[:HAS_JOB]->(title)MERGE (title)-[:IS_OF_TYPE]->(type)"} ] } 

    response = requests.post("http://<Neo4j EC2 IP Address>:7474/db/data/transaction/commit",
                         data=json.dumps(query),
                         headers=header)
    return {
        'statusCode': 200,
    }
