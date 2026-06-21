from .abstract_graph import AbstractGraph
from .exceptions import EdgeNotFoundError


class AdjacencyMatrixGraph(AbstractGraph):
    """Implementação de grafo simples e direcionado usando matriz de adjacência."""

    def __init__(self, num_vertices: int):
        super().__init__(num_vertices)
        n = num_vertices
        # matriz[u][v] = peso da aresta (u, v), ou None se a aresta não existe
        self._matrix = [[None for _ in range(n)] for _ in range(n)]
        self._edge_count = 0

    def getEdgeCount(self) -> int:
        return self._edge_count

    def hasEdge(self, u: int, v: int) -> bool:
        self._check_vertex(u)
        self._check_vertex(v)
        return self._matrix[u][v] is not None

    def addEdge(self, u: int, v: int) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        self._check_no_loop(u, v)

        if self._matrix[u][v] is None:
            self._matrix[u][v] = 0.0
            self._edge_count += 1
        # idempotente: se a aresta já existe, não faz nada

    def removeEdge(self, u: int, v: int) -> None:
        self._check_vertex(u)
        self._check_vertex(v)

        if self._matrix[u][v] is not None:
            self._matrix[u][v] = None
            self._edge_count -= 1

    def getVertexInDegree(self, u: int) -> int:
        self._check_vertex(u)
        return sum(1 for x in range(self._num_vertices) if self._matrix[x][u] is not None)

    def getVertexOutDegree(self, u: int) -> int:
        self._check_vertex(u)
        return sum(1 for x in range(self._num_vertices) if self._matrix[u][x] is not None)

    def setEdgeWeight(self, u: int, v: int, w: float) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        if self._matrix[u][v] is None:
            raise EdgeNotFoundError(f"Aresta ({u}, {v}) não existe")
        self._matrix[u][v] = w

    def getEdgeWeight(self, u: int, v: int) -> float:
        self._check_vertex(u)
        self._check_vertex(v)
        if self._matrix[u][v] is None:
            raise EdgeNotFoundError(f"Aresta ({u}, {v}) não existe")
        return self._matrix[u][v]

    def exportToGEPHI(self, path: str) -> None:
        from .export import export_to_gexf
        export_to_gexf(self._num_vertices, self._iter_edges(), path)

    def _iter_edges(self):
        for u in range(self._num_vertices):
            for v in range(self._num_vertices):
                if self._matrix[u][v] is not None:
                    yield u, v, self._matrix[u][v]
