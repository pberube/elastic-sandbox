from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConflictError
from format1.search import Search

class ElasticController:
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        self.index = 'projet1_reqs'

    def by_index_id(self, index_id):
        return_code = 200
        return_es = None
        try:
            return_es = self.es.get(index=self.index, doc_type='requirements', id=index_id)
        except NotFoundError:
            return_code = 404
        return return_es, return_code

    def by_index_id(self, project, type, index_id):
        return_code = 200
        return_es = None
        try:
            return_es = self.es.get(index=project, doc_type=type, id=index_id)
        except NotFoundError:
            return_code = 404
        return return_es, return_code

    def by_prefix(self, prefix):
        return_code = 200
        return_es = None
        try:
            reqs = Search('projet1_reqs')
            srs = reqs.by_prefix(prefix)
        except NotFoundError:
            return_code = 404
        return srs, return_code

    def by_title(self, title):
        return_code = 200
        return_es = None
        try:
            reqs = Search('projet1_reqs')
            srs = reqs.by_title(title)
        except NotFoundError:
            return_code = 404
        return srs, return_code

    def add(self, index_id, body):
        return_code = 200
        try:
            self.es.index(index=self.index, doc_type='requirements', op_type='create', id=index_id, body=body)
        except ConflictError:
            return_code = 409
        return None, return_code

    def add(self, project_name, type, index_id, body):
        return_code = 200
        try:
            self.es.index(index=project_name, doc_type=type, op_type='create', id=index_id, body=body)
        except ConflictError:
            return_code = 409
        return None, return_code
    
    def update(self, project_name, type, index_id, body):
        return_code = 200
        try:
            self.es.update(index=project_name, doc_type=type, id=index_id, body={'doc': body})
        except ConflictError:
            return_code = 409
        return None, return_code

    def delete(self):
        return_code = 200
        try:
            self.es.indices.delete(index=self.index)
        except NotFoundError:
            return_code = 404
        return None, return_code

    def delete(self, index_id):
        return_code = 200
        try:
            self.es.delete(index=self.index, id=index_id)
        except NotFoundError:
            return_code = 404
        return None, return_code

    def delete(self, project, index_id):
        return_code = 200
        try:
            self.es.delete(index=project, id=index_id)
        except NotFoundError:
            return_code = 404
        return None, return_code
