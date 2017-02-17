import json
import requests as r
g = r.get('http://122.181.186.42:9200/anuj')
json_str = g.text
json_dict = json.dumps(json_str)
print json_dict['anuj']['settings']['index']['uuid']
               
