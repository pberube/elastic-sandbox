import unittest
from format1.search import Search

class TestSearch(unittest.TestCase):
    def test_search_by_prefix_srs(self):
        sw = Search('projet1_reqs')
        srs = sw.by_prefix('srs')
        self.assertEqual(len(srs), 32)
        self.assertEqual(srs[0]['title'], 'SRS-1.1')
        self.assertEqual(srs[0]['_id'], 0)
        self.assertEqual(srs[15]['title'], 'SRS-3.1')
        self.assertEqual(srs[15]['_id'], 15)
        self.assertEqual(srs[31]['title'], 'SRS-4.7')
        self.assertEqual(srs[31]['_id'], 31)

    def test_search_by_prefix_sds(self):
        sw = Search('projet1_reqs')
        sds = sw.by_prefix('sds')
        self.assertEqual(len(sds), 173)
        self.assertEqual(sds[0]['title'], 'SDS-1.1.1')
        self.assertEqual(sds[0]['_id'], 32)
        self.assertEqual(sds[100]['title'], 'SDS-3.8.5')
        self.assertEqual(sds[100]['_id'], 132)
        self.assertEqual(sds[172]['title'], 'SDS-4.7.5')
        self.assertEqual(sds[172]['_id'], 204)

    def test_search_by_title_sds(self):
        sw = Search('projet1_reqs')
        sds = sw.sds_by_srs_id('1.1')
        self.assertEqual(len(sds), 3)
        self.assertEqual(sds[0]['title'], 'SDS-1.1.1')
        self.assertEqual(sds[0]['_id'], 32)
        self.assertEqual(sds[1]['title'], 'SDS-1.1.2')
        self.assertEqual(sds[1]['_id'], 33)
        self.assertEqual(sds[2]['title'], 'SDS-1.1.3')
        self.assertEqual(sds[2]['_id'], 34)
        sds = sw.sds_by_srs_id('4.7')
        self.assertEqual(len(sds), 5)
        self.assertEqual(sds[0]['title'], 'SDS-4.7.1')
        self.assertEqual(sds[0]['_id'], 200)
        self.assertEqual(sds[1]['title'], 'SDS-4.7.2')
        self.assertEqual(sds[1]['_id'], 201)
        self.assertEqual(sds[2]['title'], 'SDS-4.7.3')
        self.assertEqual(sds[2]['_id'], 202)
        self.assertEqual(sds[3]['title'], 'SDS-4.7.4')
        self.assertEqual(sds[3]['_id'], 203)
        self.assertEqual(sds[4]['title'], 'SDS-4.7.5')
        self.assertEqual(sds[4]['_id'], 204)

    def test_search_by_title(self):
        sw = Search('projet1_reqs')
        srs = sw.by_title('SRS-1.1')
        self.assertEqual(len(srs), 1)
        self.assertEqual(srs[0]['title'], 'SRS-1.1')
        self.assertEqual(srs[0]['_id'], 0)

    def test_search_srs_related_sds(self):
        trace = Search('traceability')
        srs = trace.srs_by_srs_id('1.1')
        self.assertEqual(len(srs), 3)
        self.assertEqual(srs[0]['title'], 'SRS-1.1')
        self.assertEqual(srs[0]['_id'], 0)
        self.assertEqual(srs[1]['title'], 'SRS-1.1')
        self.assertEqual(srs[1]['_id'], 1)
        self.assertEqual(srs[2]['title'], 'SRS-1.1')
        self.assertEqual(srs[2]['_id'], 2)
        self.assertEqual(srs[0]['related'], 'SDS-1.1.1')
        self.assertEqual(srs[1]['related'], 'SDS-1.1.2')
        self.assertEqual(srs[2]['related'], 'SDS-1.1.3')
