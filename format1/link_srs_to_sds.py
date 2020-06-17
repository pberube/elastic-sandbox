from search import Search
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# es.indices.delete(index='traceability', ignore=[400, 404])
# import sys
# sys.exit()

reqs = Search('projet1_reqs')
srs_list = reqs.by_prefix('srs')

i = 0
for srs in srs_list:
    digits = srs['title'].split('-')[1].split('.')
    srs_id = "{0}.{1}".format(digits[0], digits[1])
    print(srs_id)
    sds_list = reqs.sds_by_srs_id(srs_id)
    print(len(sds_list))
    for sds in sds_list:
        es.index(index='traceability', doc_type='relation', id=i, body={
            "title": str(srs['title']),
            "related": sds['title']
            })
        i = i + 1
