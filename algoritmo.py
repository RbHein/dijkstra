import heapq

# Utilizando o Algoritmo de Dijkstra, calcula o Custo Mínimo de um vértice de origem s até todos os outros vértices do grafo Retorna as distâncias mínimas e o vetor de predecessores.
def dijkstra(adj, s):
    n = len(adj) - 1
    dist = [float('inf')] * (n + 1)
    prev = [None] * (n + 1)
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist, prev


# Reconstrói o caminho mínimo entre dois vértices (s até t) usando o vetor de predecessores. Retorna a lista de vértices que compõem o caminho na ordem correta.
def caminho(prev, s, t):
    path = []
    u = t
    while u is not None:
        path.append(u)
        if u == s:
            break
        u = prev[u]
    if path[-1] != s:
        return []
    return path[::-1]


# Etapa interativa com o usuário: 
# - Recebe número de vértices (V) e arestas (E).
# - Recebe a descrição de cada aresta (origem, destino, peso).
# - Lê vértice de origem (s), destino (t) e o orçamento K.
# - Chama a função Dijkstra, reconstrói o caminho e exibe o resultado, informando se é possível chegar ao destino dentro do orçamento.

def main():
    V = int(input("Número de Vértices (V): "))
    E = int(input("Número de Arestas (E): "))

    adj = [[] for _ in range(V + 1)]

    print("Descreva as Arestas do Grafo no formato: U V Peso (Origem, Destino e Peso de cada aresta)")
    for i in range(E):
        u, v, w = input(f"Aresta {i+1}: ").split()
        u, v, w = int(u), int(v), float(w.replace(',', '.'))
        adj[u].append((v, w))
        adj[v].append((u, w))  # grafo não dirigido

    s = int(input("\nVértice de Origem (s): "))
    t = int(input("Vértice de Destino (t): "))
    K = float(input("Orçamento Disponível (K): ").replace(',', '.'))

    dist, prev = dijkstra(adj, s)

    if dist[t] == float('inf'):
        print("\nDestino inacessível a partir da origem.")
        return

    path = caminho(prev, s, t)
    custo = dist[t]

    print("\nResultado:")
    print(f"Custo mínimo de {s} até {t}: R$ {custo:.2f}")
    print("Caminho utilizado:", " -> ".join(map(str, path)))

    if custo <= K:
        print(f"\nSIM — é possível chegar com R$ {K:.2f}. Saldo: R$ {K - custo:.2f}")
    else:
        print(f"\nNÃO — não é possível. Faltam R$ {custo - K:.2f}")

if __name__ == "__main__":
    main()
