import unittest
from api.v1.controllers.projectController import validate_project_name, validate_id

class TestProject(unittest.TestCase):
    def test_project_name_validation(self):
        self.assertTrue(validate_project_name('project1'))
        self.assertTrue(validate_project_name('project1_reqs'))
        self.assertFalse(validate_project_name('project'))
        self.assertFalse(validate_project_name('project2'))

    def test_ids_validation(self):
        self.assertTrue(validate_id('SRS-1'))
        self.assertTrue(validate_id('SRS-1.1'))
        self.assertTrue(validate_id('SRS-1.1.2'))
        self.assertTrue(validate_id('SDS-10'))
        self.assertTrue(validate_id('SDS-10.1'))
        self.assertTrue(validate_id('SDS-10.1.2'))        
        self.assertTrue(validate_id('SDS-10.1.2.3'))        
        self.assertFalse(validate_id('adsf'))
        self.assertFalse(validate_id('SRS'))
        self.assertFalse(validate_id('SRS1'))
        self.assertFalse(validate_id('SRS1.1'))
        self.assertFalse(validate_id('SRS1-1.1'))
        self.assertFalse(validate_id('1SRS'))
        self.assertFalse(validate_id('1SRS-1.1'))
        self.assertFalse(validate_id('SRS.1'))
        self.assertFalse(validate_id('SRS-.1'))
        self.assertFalse(validate_id('SRS-1.1a'))
        self.assertFalse(validate_id('SRS-1.a'))
        self.assertFalse(validate_id('SRS-a.a'))
        self.assertFalse(validate_id('SRS-1-'))
