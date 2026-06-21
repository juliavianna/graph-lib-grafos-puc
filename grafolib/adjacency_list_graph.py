from .abstract_graph import AbstractGraph
from .exceptions import EdgeNotFoundError


class AdjacencyListGraph(AbstractGraph):
    """Implementação de grafo simples e direcionado usando listas de adjacência."""

    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        self._adj = [dict() for _ in range(num_vertices)]
        self._edge_count = 0

    def getEdgeCount(self) -> int:
        return self._edge_count

    def hasEdge(self, u: int, v: int) -> bool:
        self._check_vertex(u)
        self._check_vertex(v)
        return v in self._adj[u]

    def addEdge(self, u: int, v: int) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        self._check_no_loop(u, v)

        if v not in self._adj[u]:
            self._adj[u][v] = 0.0
            self._edge_count += 1

    def removeEdge(self, u: int, v: int) -> None:
        self._check_vertex(u)
        self._check_vertex(v)

        if v in self._adj[u]:
            del self._adj[u][v]
            self._edge_count -= 1

    def getVertexInDegree(self, u: int) -> int:
        self._check_vertex(u)
        return sum(1 for x in range(self._num_vertices) if u in self._adj[x])

    def getVertexOutDegree(self, u: int) -> int:
        self._check_vertex(u)
        return len(self._adj[u])

    def setEdgeWeight(self, u: int, v: int, w: float) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        if v not in self._adj[u]:
            raise EdgeNotFoundError(f"Aresta ({u}, {v}) não existe")
        self._adj[u][v] = w

    def getEdgeWeight(self, u: int, v: int) -> float:
        self._check_vertex(u)
        self._check_vertex(v)
        if v not in self._adj[u]:
            raise EdgeNotFoundError(f"Aresta ({u}, {v}) não existe")
        return self._adj[u][v]

    def exportToGEPHI(self, path: str) -> None:
        from .export import export_to_gexf
        export_to_gexf(self._num_vertices, self._iter_edges(), path)

    def _iter_edges(self):
        for u in range(self._num_vertices):
            for v, w in self._adj[u].items():
                yield u, v, w
