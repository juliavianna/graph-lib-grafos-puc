# Graph Library — Teoria de Grafos e Computabilidade

Biblioteca de criação, manipulação e análise de grafos simples e direcionados,
desenvolvida para o Trabalho Prático da disciplina de Teoria de Grafos e
Computabilidade (PUC Minas, 2026/1 — Prof. Gabriel Fonseca).

## Sobre o código

A biblioteca (`grafolib/`) implementa uma API comum para grafos simples e
direcionados, com duas representações internas intercambiáveis:

- **`AdjacencyMatrixGraph`** — arestas e pesos armazenados em matriz `n x n`.
- **`AdjacencyListGraph`** — arestas e pesos armazenados em lista de dicionários
  (um dicionário de adjacência por vértice).

Ambas estendem `AbstractGraph`, que concentra a lógica comum (validação de
índices, bloqueio de laços, pesos de vértice, e métodos derivados como
`isSuccessor`, `isEmptyGraph`, `isCompleteGraph`, `isConnected`), e implementam
apenas o que depende da estrutura de dados interna (`hasEdge`, `addEdge`,
`removeEdge`, graus, pesos de aresta, exportação para Gephi).

Restrições garantidas pela implementação:
- Grafo simples: sem laços `(u, u)` e sem arestas duplicadas.
- `addEdge` é idempotente.
- Índices de vértice inválidos e operações inconsistentes (ex.: consultar peso
  de aresta inexistente) lançam exceções (`InvalidVertexError`,
  `InvalidEdgeError`, `EdgeNotFoundError`).
- Nenhuma biblioteca pronta de grafos é utilizada — apenas a biblioteca padrão
  do Python.

## Estrutura de pastas

```
graph-lib-grafos-puc/
├── grafolib/                    # biblioteca (Etapa 1)
│   ├── __init__.py
│   ├── abstract_graph.py        # classe abstrata AbstractGraph
│   ├── adjacency_matrix_graph.py
│   ├── adjacency_list_graph.py
│   ├── exceptions.py            # exceções customizadas
│   └── export.py                # exportação para Gephi (.gexf)
├── demo.py                      # demonstração da API (fixa, sem interação)
├── demo_interativo.py           # demonstração via menu no terminal
├── tests/                       # testes automatizados (pytest)
│   ├── test_adjacency_matrix.py
│   └── test_adjacency_list.py
├── docs/                        # relatório (modelo SBC)
├── conftest.py
├── requirements.txt
├── .gitignore
└── readme.md
```
## Como rodar

### 1. Criar e ativar o ambiente virtual (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se aparecer erro de política de execução, rode antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 2. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 3. Rodar a demonstração

```powershell
python demo.py              # demonstração fixa, cobrindo toda a API
python demo_interativo.py   # demonstração interativa via menu no terminal
```

### 4. Rodar os testes

```powershell
pytest
```

### 5. Visualizar no Gephi

Os comandos acima geram arquivos `.gexf` na raiz do projeto. Abra o
[Gephi](https://gephi.org/) e use `File → Open` para importar o arquivo e
visualizar o grafo.
