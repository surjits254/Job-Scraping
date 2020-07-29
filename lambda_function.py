import json
import requests

def lambda_handler(event, context):
    header = {"Content-type": "application/json", "Authorization": "bmVvNGo6YW5raU5lbzRq"}
    query = {"statements" : [ {"statement" : "LOAD CSV WITH HEADERS FROM 'https://craig-scraped-data.s3.amazonaws.com/craiglist.csv?AWSAccessKeyId=ASIATOEBR2BVWLKN2VAI&Expires=1595714711&x-amz-security-token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCFbozJveE1bZdmCComJg6cK5xcrYgb%2BHIvxV0Z8zmYBQIgCgijza5ltCx%2FSJi0%2FYlYiRHOte0bDJLAoq%2FL37%2BByjIqvQMIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwyMzY0OTQ5MDEzNTUiDEHRSKkN2AvpzvqbBiqRA8iiCnS%2B68UyBL9%2BCZG4Tg%2BIUNisTYBe3xo1GhBmupKrzdL90%2BfhsTyaceWRepXuyJHqwZ6ga6qKDKqWLhF8WfvnizG8HjHGm4HsBBQen3k7wJqypDlUuCUbUCHsBpY5USS2zng0HzlyLw8O1wMhDFawRI7Z5XjymA5HgrSa39cYTbOUof77BwF5y9okhbEKP4EJYtBYAbD3LALKgm2HTtYl%2BcFZeY%2F%2BcHxhZ1PEagUswupR4BASJAJxeBb%2FbmWRZBnH8IPNXofg3HwkyD%2B3qryzQEPjkFpmlvjbRvkNwcSLp1oiBjy28FWh9yByrsNfnGgUBwocS5PD9UBIqJRp1%2FVVEGnLKJ2D5FiZ8hzzEPU16KKpkMk981LXmnlr87pvdd1EgzMzVghvtq56qNZsCtW6SIlNm2C4TbYOJES%2Bv75a5JzK9Bd%2BoVIiv928%2Brt18nUwBIxUFgNzuiivvpKUeEC5QaG9K4BB9KHM9Gbg8EYtmB0Fz3Ogo%2F2u3pAU5gzvMAHnveOoSFPPULt5q2LUCiCfMJ%2B88vgFOusBpLMtyiDesM3K2R%2F8Zvhy9vUaOYZX9tzGvngKwderdcP%2BzLoj9K1Q0sa2oWcLZ6jT9qUUoqm6wPCteiXMF8kCvCxrG2mNEA%2FxOe7IK7E9oSDJZ7vGQLS%2F3njR307WpFqzQcN2CSO9w8%2BLK%2BqwpuXzwxxS1UlrYoMKBczwwCt3Qf6T9FHw6t8HFsr5HCfz0pwatQUkgJHGFpFUOxU%2F36FPzJhEBaRnR%2FiDPvu1ja%2B4CH5dwexYkpGUVwJvsfm5wJL83m8fjbSjnFUNMA6mNkG8uCFYnI7pnlzX43GJsu2ZKWowISHpkAcwsQGDNQ%3D%3D&Signature=odkf3PMvB9SY78gbjFsnLMGx1wA%3D' AS csvLine MERGE (location:Location {name: csvLine.location}) MERGE (title:Job_Tile {name: csvLine.job_title, url:csvLine.url}) MERGE (type:Job_Type {name: coalesce(csvLine.type, 'Unknown')}) MERGE (location)-[:HAS_JOB]->(title)MERGE (title)-[:IS_OF_TYPE]->(type)"} ] } 

    response = requests.post("http://54.234.30.108:7474/db/data/transaction/commit",
                         data=json.dumps(query),
                         headers=header)
    return {
        'statusCode': 200,
    }
