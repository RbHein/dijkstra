ALGORITMO DE DIJKSTRA - CONSIGO CHEGAR AO DESTINO COM K REAIS?

Desenvolvido por Rafael Belchor Hein

-------------------------------------------------

Instruções de Execução:

- No diretório do projeto, acessando pelo Terminal, executar o comando "Python algoritmo.py" ou "Executar Arquivo Python" pelo canto superior direito do Visual Studio Code;
- O arquivo do código não se chama "dijkstra.py" para facilitar a vida do usuário na execução;


- Entrada interativa:
  * Digitar Número de Vértices V (Inteiro, > 0)
  * Digitar Número de Arestas E (Inteiro, >=0 )
  * Descrever as arestas ligando os vértices com o formato: U V Peso (u e v inteiros entre 1 e n; Peso >= 0; aceita ',' ou '.' para decimais. Exemplo: 0 1 2 para aresta ligando o
  os vértices 0 e 1, tendo a aresta peso 2);
  * Informar o Vértice de Origem (S)
  * Informar o Vértice de Destino (T)
  * Informar o "Orçamento Disponível" (K)

- Saída:
  * Se o destino é inacessível, informa o erro; 
  * Caso encontre o caminho mínimo com o orçamento disponível, informa custo mínimo (R$), caminho (sequência de vértices)
  * Detalha se é possível chegar com K reais e mostra ou o saldo restante ou valor faltante;

-------------------------------

Dicas:

- Utilizando o "grafoSugerido.png" disponível no diretório e usado nos testes do algoritmo, a descrição dos inputs do usuário seria a seguinte, 
para descobrir se seria possível partir do vértice 0 e chegar ao vértice 6 com R$ 20.

    Número de Vértices (V): 7
    Número de Arestas (E): 9

    Digite as arestas no formato: U V Peso (Origem, Destino e Peso de cada aresta)
    Aresta 1: 0 2 6
    Aresta 2: 0 1 2
    Aresta 3: 2 3 8
    Aresta 4: 1 3 5
    Aresta 5: 3 4 10
    Aresta 6: 3 5 15
    Aresta 7: 4 5 6
    Aresta 8: 4 6 2
    Aresta 9: 5 6 6

    Vértice de origem (s): 0
    Vértice destino (t): 6
    Orçamento disponível K: 20

- Após as entradas do usuário, o Algoritmo de Dijkstra é executado e disponibiliza a saída com a resposta:

    Resultado:
    Custo mínimo de 0 até 6: R$ 19.00
    Caminho utilizado: 0 -> 1 -> 3 -> 4 -> 6

    SIM — é possível chegar com R$ 20.00. Saldo: R$ 1.00

- Portanto, neste exemplo é SIM possível sair de S (Vértice 0) e chegar a T (Vértice 6) com K (20) reais.

----------------------------------------------------
