
def format_graph(srs):
    line = '"{0}" -> "{1}"'
    query = 'digraph G {'
    for r in srs:
        query += line.format(r['title'], r['related'])
    query += '}'
    return query
