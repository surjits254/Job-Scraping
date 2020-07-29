import requests
import json
from flask import Flask, request
import copy
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import configparser



app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

config = configparser.ConfigParser()
config.read('conf_flask.ini')
neo4jAPi = config['common']['neo4jAPi']
authorization = config['common']['authorization']


header = {"Content-type": "application/json", "Authorization": authorization}
queryTemplate = {"statements" : [ {"statement" : "MATCH (location:Location)-[]->(job_title:Job_Tile)-[]->(job_type:Job_Type) return location,job_title,job_type limit 20"} ] } 
getQuery = {"statements" : [ {"statement" : "MATCH (location:Location)-[]->(job_title:Job_Tile)-[]->(job_type:Job_Type) return location,job_title,job_type limit 20"} ] }
customQuery = "MATCH (location:Location)-[]->(job_title:Job_Tile)-[]->(job_type:Job_Type) {0} return location,job_title,job_type limit 20"
jobTypeFilter = "WHERE job_type.name='{0}'"
locationFilter = "WHERE location.name='{0}'"
multiFilter = "WHERE location.name='{0}' and job_type.name='{1}'"
result = {"data":[]}
    
@app.route('/')
def getAll():
    
    outpt = copy.deepcopy(result)
    response = requests.post(neo4jAPi,
                         data=json.dumps(getQuery),
                         headers=header)
    
    res = response.json()
    print(res)
    cols = res['results'][0]['columns']
    data = res['results'][0]['data']
    for line in range(len(data)):
        dic = {}
        for col in range(len(cols)):
            dic[cols[col]] = data[line]['row'][col]['name']
            if(col == 1):
                dic['url'] = data[line]['row'][col]['url']
        outpt['data'].append(dic)
       
    return outpt

@app.route('/search',methods=["POST"])
def getCustom():
    inpt = request.get_json()
    print(json.dumps(inpt))
    job_type = inpt['job_type']
    location = inpt['location']
    queryFilter = {}
    query = {}
    outpt = copy.deepcopy(result)
    if(job_type == 'Other'):
        job_type = "Unknown"
        
    if(job_type !="" and location != ""):
        queryFilter = multiFilter.format(location,job_type)
    
    if(job_type !="" and location == ""):
        queryFilter = jobTypeFilter.format(job_type)
        
    if(job_type =="" and location != ""):
        queryFilter = locationFilter.format(location)
        
    if(job_type == "" and location == ""):
        q = customQuery.format("")
        query = queryTemplate
        query['statements'][0]['statement'] = q
    else:
        q = customQuery.format(queryFilter)
        query = queryTemplate
        query['statements'][0]['statement'] = q

    response = requests.post(neo4jAPi,
                         data=json.dumps(query),
                         headers=header)
    
    res = response.json()
    cols = res['results'][0]['columns']
    data = res['results'][0]['data']
    for line in range(len(data)):
        dic = {}
        for col in range(len(cols)):
            dic[cols[col]] = data[line]['row'][col]['name']
            if(col == 1):
                dic['url'] = data[line]['row'][col]['url']
        outpt['data'].append(dic)
        
    finalOutput = outpt
    outpt = result
    return finalOutput


if __name__ == '__main__':
    app.run(host="0.0.0.0")

