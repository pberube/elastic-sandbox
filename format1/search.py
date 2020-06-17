from elasticsearch import Elasticsearch


class Search():
    def __init__(self, index):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        self.index = index

    def by_prefix(self, prefix):
        s = self.es.search(index=self.index, body={
            'size': 1000,
            'query': {
                'bool': {
                    'must': {
                        'match': {
                            'prefix': prefix
                            }}}}})
        result = list()
        for r in s['hits']['hits']:
            result.append(r['_source'])
        return result

    def sds_by_srs_id(self, srs_id):
        return self.by_prefix_and_spec_id('sds', srs_id)

    def srs_by_srs_id(self, srs_id):
        return self.by_prefix_and_spec_id('srs', srs_id)
        
    def by_prefix_and_spec_id(self, prefix, spec_id):
        digits = spec_id.split('.')
        query_string = "\\{0}\\.\\{1}\\.*".format(digits[0], digits[1])
        s = self.es.search(index=self.index,body= {
            'size': 1000,
              "query": {
                "bool": {
                "must": [],
                "filter": [
                    {
                    "bool": {
                        "filter": [
                        {
                            "bool": {
                            "should": [
                                {
                                "match": {
                                    "title": prefix.upper()
                                }}],
                            "minimum_should_match": 1
                            }},
                        {
                            "query_string": {
                            "query": query_string}}]}}],
                "should": [],
                "must_not": []
                }}})
        result = list()
        for r in s['hits']['hits']:
            result.append(r['_source'])
        return result
