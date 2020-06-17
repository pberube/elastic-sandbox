import unittest
from format1.search import Search
from format1.graph import format_graph

class TestGraph(unittest.TestCase):
    def test_graph_format_for_srs(self):
        trace = Search('traceability')
        srs = trace.srs_by_srs_id('1.1')
        graph = format_graph(srs)
        self.assertEqual(graph, 'digraph G {"SRS-1.1" -> "SDS-1.1.1""SRS-1.1" -> "SDS-1.1.2""SRS-1.1" -> "SDS-1.1.3"}')
