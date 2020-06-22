from flask import request
from flask_restplus import Namespace, Resource, fields

from api.v1.controllers.elasticController import ElasticController

api = Namespace('elastic', description="elasticsearch's playground")

elastic_controller = ElasticController()


class RequirementDTO:
    creation = api.model('requirement:create', {
        'title': fields.String(required=True, description="Title of the requirement"),
        'description': fields.String(required=True, description="Description of the requirement"),
        'type': fields.String(required=True, description="Hardware, software, etc"),
        'prefix': fields.String(required=True, description="srs or sds")
    })


@api.route('/id/<int:id>')
@api.response(200, 'Success')
class SingleId(Resource):
    def get(self, id):
        """Find one entry by id"""
        return elastic_controller.by_index_id(id)

    @api.expect(RequirementDTO.creation)
    def post(self, id):
        """Insert one entry"""
        return elastic_controller.add(id, request.json)

    def delete(self, id):
        """Delete one entry by id"""
        return elastic_controller.delete(id)


@api.route('/prefix/<string:prefix>')
@api.response(200, 'Success')
class SinglePrefix(Resource):
    def get(self, prefix):
        """Find one entry by prefix"""
        print('here')
        return elastic_controller.by_prefix(prefix)


@api.route('/title/<string:title>')
@api.response(200, 'Success')
class SingleTitle(Resource):
    def get(self, title):
        """Find one entry by title"""
        print('here')
        return elastic_controller.by_title(title)


@api.route('')
@api.response(200, 'Success')
class MultipleId(Resource):
    def delete(self):
        """Delete all entries"""
        return elastic_controller.delete()
