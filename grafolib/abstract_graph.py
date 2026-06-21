from abc import ABC, abstractmethod

from .exceptions import InvalidVertexError, InvalidEdgeError


class AbstractGraph(ABC):
    """Define a API comum para representações de grafos simples e direcionados."""

    def __init__(self, num_vertices: int):
        if num_vertices < 0:
            raise InvalidVertexError("numVertices não pode ser negativo")
        self._num_vertices = num_vertices
        self._vertex_weights = [0.0] * num_vertices

    def _check_vertex(self, v: int) -> None:
        if not isinstance(v, int) or v < 0 or v >= self._num_vertices:
            raise InvalidVertexError(f"Índice de vértice inválido: {v}")

    def _check_no_loop(self, u: int, v: int) -> None:
        if u == v:
            raise InvalidEdgeError("Não é permitido laço (u, u)")

    def getVertexCount(self) -> int:
        return self._num_vertices

    def setVertexWeight(self, v: int, w: float) -> None:
        self._check_vertex(v)
        self._vertex_weights[v] = w

    def getVertexWeight(self, v: int) -> float:
        self._check_vertex(v)
        return self._vertex_weights[v]

    def isEmptyGraph(self) -> bool:
        return self.getEdgeCount() == 0

    def isCompleteGraph(self) -> bool:
        n = self._num_vertices
        max_edges = n * (n - 1)
        return self.getEdgeCount() == max_edges

    def isSuccessor(self, u: int, v: int) -> bool:
        return self.hasEdge(u, v)

    def isPredecessor(self, u: int, v: int) -> bool:
        return self.hasEdge(u, v)

    def isDivergent(self, u1: int, v1: int, u2: int, v2: int) -> bool:
        self._check_vertex(u1)
        self._check_vertex(v1)
        self._check_vertex(u2)
        self._check_vertex(v2)
        return u1 == u2

    def isConvergent(self, u1: int, v1: int, u2: int, v2: int) -> bool:
        self._check_vertex(u1)
        self._check_vertex(v1)
        self._check_vertex(u2)
        self._check_vertex(v2)
        return v1 == v2

    def isIncident(self, u: int, v: int, x: int) -> bool:
        self._check_vertex(u)
        self._check_vertex(v)
        self._check_vertex(x)
        return x == u or x == v

    def isConnected(self) -> bool:
        """Verifica conectividade tratando o grafo como não direcionado
        (existe caminho entre quaisquer dois vértices ignorando direção)."""
        n = self._num_vertices
        if n == 0:
            return True

        visited = [False] * n
        stack = [0]
        visited[0] = True
        count = 1

        while stack:
            u = stack.pop()
            for v in range(n):
                if not visited[v] and (self.hasEdge(u, v) or self.hasEdge(v, u)):
                    visited[v] = True
                    count += 1
                    stack.append(v)

        return count == n

    @abstractmethod
    def getEdgeCount(self) -> int:
        ...

    @abstractmethod
    def hasEdge(self, u: int, v: int) -> bool:
        ...

    @abstractmethod
    def addEdge(self, u: int, v: int) -> None:
        ...

    @abstractmethod
    def removeEdge(self, u: int, v: int) -> None:
        ...

    @abstractmethod
    def getVertexInDegree(self, u: int) -> int:
        ...

    @abstractmethod
    def getVertexOutDegree(self, u: int) -> int:
        ...

    @abstractmethod
    def setEdgeWeight(self, u: int, v: int, w: float) -> None:
        ...

    @abstractmethod
    def getEdgeWeight(self, u: int, v: int) -> float:
        ...

    @abstractmethod
    def exportToGEPHI(self, path: str) -> None:
        ...
