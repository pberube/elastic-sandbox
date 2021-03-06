# elastic-sandbox
Playing with elasticsearch

# Log
Day 1
* Put in place local Elasticsearch and Kibana through docker-compose.
* $ curl -X GET "localhost:9200/_cat/nodes?v&pretty"
  
Day 2
* Have a simple Flask API:
* POST - Add entry to elastic
* DELETE - Remove entry from elactic
* PUT - Change an entry
* GET - Find an entry
  
Day 3
* Populate elasticsearch with srs and sds
  
Day 4
* Populate elasticsearch with links between srs and sds
  
Day 5
* Display relation between srs and sds into a web page
  
Day 6
* New api for adding, updating and finding a requirement by _id
* The prefix and numerical part of the _id is validated

# Useful links
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/

# How to run the whole thing
## Elastic and Kibana (running in docker)
$ docker-compose -f "docker-compose.yml" up -d --build
## Graphviz minimal microservice (running in docker)
$ git clone git@github.com:sseemayer/docker-graphviz.git
$ docker run -d -p 8000:8000 --name graphviz sseemayer/graphviz
## Flask api and web page (running locally)
$ python3 app.py run
## Flask API Url
http://localhost:30000/api/v1/
## Flask Web Url
http://localhost:30000/trace/1.1
## Populate the SRS and SDS in Elasticsearch (python script ran locally)
python3 format1/insert_srs_sds.py
## Populate the relation between SRS and SDS in Elasticsearch (python script ran locally)
$ python3 format1/link_srs_to_sds.py
## Running Tests
$ python3 -m unittest tests.search_tests.TestSearch  
$ python3 -m unittest tests.graph_tests.TestGraph
# To Do
* search using the service api only, not through elasticsearch api
* add get by prefix
* add get by title
* have 2 post: one for requirements, one for relation
* test how to add new field to index. Ex: vep, ver, rsk to srs relation