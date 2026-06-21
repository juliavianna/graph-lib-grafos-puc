def export_to_gexf(num_vertices, edges, path: str) -> None:
    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">')
    lines.append('  <graph mode="static" defaultedgetype="directed">')
    lines.append('    <nodes>')
    for i in range(num_vertices):
        lines.append(f'      <node id="{i}" label="{i}" />')
    lines.append('    </nodes>')
    lines.append('    <edges>')
    for edge_id, (u, v, w) in enumerate(edges):
        lines.append(f'      <edge id="{edge_id}" source="{u}" target="{v}" weight="{w}" />')
    lines.append('    </edges>')
    lines.append('  </graph>')
    lines.append('</gexf>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
