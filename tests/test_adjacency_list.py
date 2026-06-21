import pytest

from grafolib import AdjacencyListGraph
from grafolib.exceptions import InvalidVertexError, InvalidEdgeError, EdgeNotFoundError


def make_graph():
    g = AdjacencyListGraph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    return g


def test_vertex_count():
    g = AdjacencyListGraph(4)
    assert g.getVertexCount() == 4


def test_add_edge_and_has_edge():
    g = make_graph()
    assert g.hasEdge(0, 1)
    assert not g.hasEdge(1, 0)


def test_add_edge_is_idempotent():
    g = AdjacencyListGraph(3)
    g.addEdge(0, 1)
    g.addEdge(0, 1)
    g.addEdge(0, 1)
    assert g.getEdgeCount() == 1


def test_add_edge_rejects_loop():
    g = AdjacencyListGraph(3)
    with pytest.raises(InvalidEdgeError):
        g.addEdge(0, 0)


def test_remove_edge():
    g = make_graph()
    g.removeEdge(0, 1)
    assert not g.hasEdge(0, 1)
    assert g.getEdgeCount() == 2


def test_remove_nonexistent_edge_does_not_fail():
    g = AdjacencyListGraph(3)
    g.removeEdge(0, 1)
    assert g.getEdgeCount() == 0


def test_invalid_vertex_raises():
    g = AdjacencyListGraph(3)
    with pytest.raises(InvalidVertexError):
        g.hasEdge(0, 5)
    with pytest.raises(InvalidVertexError):
        g.addEdge(-1, 0)


def test_successor_and_predecessor():
    g = make_graph()
    assert g.isSuccessor(0, 1)
    assert g.isPredecessor(0, 1)
    assert not g.isSuccessor(2, 0)


def test_divergent_and_convergent():
    g = make_graph()
    assert g.isDivergent(0, 1, 0, 2)
    assert not g.isDivergent(0, 1, 1, 2)
    assert g.isConvergent(0, 2, 1, 2)
    assert not g.isConvergent(0, 1, 0, 2)


def test_is_incident():
    g = make_graph()
    assert g.isIncident(0, 1, 0)
    assert g.isIncident(0, 1, 1)
    assert not g.isIncident(0, 1, 2)


def test_degrees():
    g = make_graph()
    assert g.getVertexOutDegree(0) == 2
    assert g.getVertexInDegree(2) == 2
    assert g.getVertexInDegree(0) == 0


def test_vertex_weight():
    g = AdjacencyListGraph(3)
    g.setVertexWeight(0, 5.0)
    assert g.getVertexWeight(0) == 5.0


def test_edge_weight():
    g = AdjacencyListGraph(3)
    g.addEdge(0, 1)
    g.setEdgeWeight(0, 1, 2.5)
    assert g.getEdgeWeight(0, 1) == 2.5


def test_edge_weight_nonexistent_edge_raises():
    g = AdjacencyListGraph(3)
    with pytest.raises(EdgeNotFoundError):
        g.getEdgeWeight(0, 1)
    with pytest.raises(EdgeNotFoundError):
        g.setEdgeWeight(0, 1, 1.0)


def test_is_empty_graph():
    g = AdjacencyListGraph(3)
    assert g.isEmptyGraph()
    g.addEdge(0, 1)
    assert not g.isEmptyGraph()


def test_is_complete_graph():
    g = AdjacencyListGraph(3)
    for u in range(3):
        for v in range(3):
            if u != v:
                g.addEdge(u, v)
    assert g.isCompleteGraph()


def test_is_not_complete_graph():
    g = make_graph()
    assert not g.isCompleteGraph()


def test_is_connected():
    g = AdjacencyListGraph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    assert g.isConnected()


def test_is_not_connected():
    g = AdjacencyListGraph(4)
    g.addEdge(0, 1)
    assert not g.isConnected()


def test_export_to_gephi(tmp_path):
    g = make_graph()
    output = tmp_path / "graph.gexf"
    g.exportToGEPHI(str(output))
    content = output.read_text(encoding="utf-8")
    assert "<gexf" in content
    assert 'source="0" target="1"' in content
