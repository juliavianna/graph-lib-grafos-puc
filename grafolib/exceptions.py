class InvalidVertexError(Exception):
    """Levantada quando um índice de vértice é inválido."""
    pass


class EdgeNotFoundError(Exception):
    """Levantada quando se tenta consultar/operar sobre uma aresta inexistente."""
    pass


class InvalidEdgeError(Exception):
    """Levantada quando se tenta criar uma aresta inválida (ex: laço (u, u))."""
    pass
