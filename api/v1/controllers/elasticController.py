from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConflictError

class ElasticController:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        self.index = 'projet1_reqs'

    def get(self, index_id):
        return_code = 200
        return_es = None
        try:
            return_es = self.es.get(index=self.index, doc_type='requirements', id=index_id)
        except NotFoundError:
            return_code = 404
        return return_es, return_code

    def add(self, index_id, body):
        return_code = 200
        try:
            self.es.index(index=self.index, doc_type='requirements', op_type='create', id=index_id, body=body)
        except ConflictError:
            return_code = 409
        return None, return_code

    def delete(self, index_id):
        return_code = 200
        try:
            self.es.delete(index=self.index, id=index_id)
        except NotFoundError:
            return_code = 404
        return None, return_code

    def delete(self):
        return_code = 200
        try:
            self.es.indices.delete(index=self.index)
        except NotFoundError:
            return_code = 404
        return None, return_code
