from flask import request
from flask_restplus import Namespace, Resource, fields

from api.v1.controllers.elasticController import ElasticController
from api.v1.controllers.projectController import validate_project_name, validate_id

api = Namespace('project', description="Project Services")

elastic_controller = ElasticController()


class RequirementDTO:
    creation = api.model('requirement:create', {
        'title': fields.String(required=True, description="Title of the requirement"),
        'description': fields.String(required=True, description="Description of the requirement"),
        'type': fields.String(required=True, description="Hardware, software, etc"),
        'prefix': fields.String(required=True, description="srs or sds")
    })


@api.route('/<string:project_name>/<string:entry_id>')
@api.response(200, 'Success')
class Project(Resource):
    def get(self, project_name, entry_id):
        """Find one entry by its id"""
        if validate_project_name(project_name):
            if validate_id(entry_id):
                response = elastic_controller.by_index_id(project_name, 'requirements', entry_id.upper())
            else:
                response = None, '502 Invalid Id'
        else:
            response = None, '501 Project does not exist'
        return response

    @api.expect(RequirementDTO.creation)
    def post(self, project_name, entry_id):
        """Insert one entry"""
        if validate_project_name(project_name):
            if validate_id(entry_id):
                response = elastic_controller.add(project_name, 'requirements', entry_id.upper(), request.json)
            else:
                response = None, '502 Invalid Id'
        else:
            response = None, '501 Project does not exist'
        return response

    @api.expect(RequirementDTO.creation)
    def put(self, project_name, entry_id):
        """Insert one entry"""
        if validate_project_name(project_name):
            if validate_id(entry_id):
                response = elastic_controller.update(project_name, 'requirements', entry_id.upper(), request.json)
            else:
                response = None, '502 Invalid Id'
        else:
            response = None, '501 Project does not exist'
        return response

    def delete(self, project_name, entry_id):
        """Delete one entry by id"""
        if validate_project_name(project_name):
            if validate_id(entry_id):
                response = elastic_controller.delete(project_name, entry_id.upper())
            else:
                response = None, '502 Invalid Id'
        else:
            response = None, '501 Project does not exist'
        return response
