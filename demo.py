from grafolib import AdjacencyMatrixGraph, AdjacencyListGraph


def demo(graph, name):
    print(f"\n=== {name} ===")

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 1)

    print("Vértices:", graph.getVertexCount())
    print("Arestas:", graph.getEdgeCount())

    print("hasEdge(0, 1):", graph.hasEdge(0, 1))
    print("hasEdge(1, 0):", graph.hasEdge(1, 0))
    print("isSuccessor(0, 1):", graph.isSuccessor(0, 1))
    print("isPredecessor(0, 2):", graph.isPredecessor(0, 2))

    graph.removeEdge(1, 2)
    print("Após remover (1, 2), hasEdge(1, 2):", graph.hasEdge(1, 2))

    print("Grau de entrada de 0:", graph.getVertexInDegree(0))
    print("Grau de saída de 0:", graph.getVertexOutDegree(0))

    graph.setVertexWeight(0, 10.5)
    print("Peso do vértice 0:", graph.getVertexWeight(0))

    graph.setEdgeWeight(0, 1, 3.2)
    print("Peso da aresta (0, 1):", graph.getEdgeWeight(0, 1))

    print("Grafo vazio?", graph.isEmptyGraph())
    print("Grafo completo?", graph.isCompleteGraph())
    print("Grafo conectado?", graph.isConnected())

    output_path = f"{name.lower().replace(' ', '_')}.gexf"
    graph.exportToGEPHI(output_path)
    print(f"Grafo exportado para {output_path}")


if __name__ == "__main__":
    demo(AdjacencyMatrixGraph(3), "Adjacency Matrix Graph")
    demo(AdjacencyListGraph(3), "Adjacency List Graph")
