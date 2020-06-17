import unittest
from format1.search import Search

class TestSearch(unittest.TestCase):
    def test_search_by_prefix_srs(self):
        sw = Search('projet1_reqs')
        srs = sw.by_prefix('srs')
        self.assertEqual(len(srs), 32)
        self.assertEqual(srs[0]['title'], 'SRS-1.1')
        self.assertEqual(srs[15]['title'], 'SRS-3.1')
        self.assertEqual(srs[31]['title'], 'SRS-4.7')

    def test_search_by_prefix_sds(self):
        sw = Search('projet1_reqs')
        srs = sw.by_prefix('sds')
        self.assertEqual(len(srs), 173)
        self.assertEqual(srs[0]['title'], 'SDS-1.1.1')
        self.assertEqual(srs[100]['title'], 'SDS-3.8.5')
        self.assertEqual(srs[172]['title'], 'SDS-4.7.5')

    def test_search_by_title_sds(self):
        sw = Search('projet1_reqs')
        sds = sw.sds_by_srs_id('1.1')
        self.assertEqual(len(sds), 3)
        self.assertEqual(sds[0]['title'], 'SDS-1.1.1')
        self.assertEqual(sds[1]['title'], 'SDS-1.1.2')
        self.assertEqual(sds[2]['title'], 'SDS-1.1.3')
        sds = sw.sds_by_srs_id('4.7')
        self.assertEqual(len(sds), 5)
        self.assertEqual(sds[0]['title'], 'SDS-4.7.1')
        self.assertEqual(sds[1]['title'], 'SDS-4.7.2')
        self.assertEqual(sds[2]['title'], 'SDS-4.7.3')
        self.assertEqual(sds[3]['title'], 'SDS-4.7.4')
        self.assertEqual(sds[4]['title'], 'SDS-4.7.5')

    def test_search_srs_related_sds(self):
        trace = Search('traceability')
        srs = trace.srs_by_srs_id('1.1')
        self.assertEqual(len(srs), 3)
        self.assertEqual(srs[0]['title'], 'SRS-1.1')
        self.assertEqual(srs[1]['title'], 'SRS-1.1')
        self.assertEqual(srs[2]['title'], 'SRS-1.1')
        self.assertEqual(srs[0]['related'], 'SDS-1.1.1')
        self.assertEqual(srs[1]['related'], 'SDS-1.1.2')
        self.assertEqual(srs[2]['related'], 'SDS-1.1.3')
