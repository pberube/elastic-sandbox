from flask import render_template
from web import blueprint_web as web
from format1.search import Search
from format1.graph import format_graph
import urllib.parse


@web.route("/trace/<srs_id>")
def visual(srs_id):
    trace = Search('traceability')
    srs = trace.srs_by_srs_id(srs_id)
    graph = format_graph(srs)
    return render_template('traceability.html', encoded_url_data=urllib.parse.quote(graph))
