from grafolib import AdjacencyMatrixGraph, AdjacencyListGraph
from grafolib.exceptions import InvalidVertexError, InvalidEdgeError, EdgeNotFoundError


def criar_grafo():
    while True:
        tipo = input("Representação (1 = matriz de adjacência, 2 = lista de adjacência): ").strip()
        if tipo in ("1", "2"):
            break
        print("Opção inválida.")

    while True:
        try:
            n = int(input("Número de vértices do grafo: ").strip())
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    if tipo == "1":
        return AdjacencyMatrixGraph(n)
    return AdjacencyListGraph(n)


def menu():
    print("""
1  - Adicionar aresta
2  - Remover aresta
3  - Verificar sucessor/predecessor
4  - Calcular grau de entrada/saída
5  - Definir peso de vértice
6  - Consultar peso de vértice
7  - Definir peso de aresta
8  - Consultar peso de aresta
9  - Verificar se o grafo é vazio
10 - Verificar se o grafo é completo
11 - Verificar se o grafo é conectado
12 - Exportar para Gephi
0  - Sair
""")


def ler_int(mensagem):
    return int(input(mensagem).strip())


def main():
    graph = criar_grafo()
    print(f"\nGrafo criado com {graph.getVertexCount()} vértices.")

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                u = ler_int("Vértice de origem (u): ")
                v = ler_int("Vértice de destino (v): ")
                graph.addEdge(u, v)
                print(f"Aresta ({u}, {v}) adicionada. Total de arestas: {graph.getEdgeCount()}")

            elif opcao == "2":
                u = ler_int("Vértice de origem (u): ")
                v = ler_int("Vértice de destino (v): ")
                graph.removeEdge(u, v)
                print(f"Aresta ({u}, {v}) removida. Total de arestas: {graph.getEdgeCount()}")

            elif opcao == "3":
                u = ler_int("u: ")
                v = ler_int("v: ")
                print(f"{v} é sucessor de {u}? {graph.isSuccessor(u, v)}")
                print(f"{u} é predecessor de {v}? {graph.isPredecessor(u, v)}")

            elif opcao == "4":
                u = ler_int("Vértice: ")
                print(f"Grau de entrada: {graph.getVertexInDegree(u)}")
                print(f"Grau de saída: {graph.getVertexOutDegree(u)}")

            elif opcao == "5":
                v = ler_int("Vértice: ")
                w = float(input("Peso: ").strip())
                graph.setVertexWeight(v, w)
                print(f"Peso do vértice {v} definido como {w}")

            elif opcao == "6":
                v = ler_int("Vértice: ")
                print(f"Peso do vértice {v}: {graph.getVertexWeight(v)}")

            elif opcao == "7":
                u = ler_int("Vértice de origem (u): ")
                v = ler_int("Vértice de destino (v): ")
                w = float(input("Peso: ").strip())
                graph.setEdgeWeight(u, v, w)
                print(f"Peso da aresta ({u}, {v}) definido como {w}")

            elif opcao == "8":
                u = ler_int("Vértice de origem (u): ")
                v = ler_int("Vértice de destino (v): ")
                print(f"Peso da aresta ({u}, {v}): {graph.getEdgeWeight(u, v)}")

            elif opcao == "9":
                print(f"Grafo vazio? {graph.isEmptyGraph()}")

            elif opcao == "10":
                print(f"Grafo completo? {graph.isCompleteGraph()}")

            elif opcao == "11":
                print(f"Grafo conectado? {graph.isConnected()}")

            elif opcao == "12":
                path = input("Caminho do arquivo de saída (ex: grafo.gexf): ").strip()
                graph.exportToGEPHI(path)
                print(f"Grafo exportado para {path}")

            elif opcao == "0":
                print("Encerrando.")
                break

            else:
                print("Opção inválida.")

        except (InvalidVertexError, InvalidEdgeError, EdgeNotFoundError, ValueError) as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
