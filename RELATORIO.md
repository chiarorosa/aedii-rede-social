Henrique Rodeghiero
Matheus Rohrig

# Contribuição de Henrique

## Funcionalidades implementadas

Foram implementados os itens 3.2, 3.4 e 3.6 da atividade:

- `SUGERIR`: sugere pessoas a distância dois no grafo de seguidores.
- `POSTS_ENTRE`: lista posts entre duas datas, incluindo as datas-limite.
- `RANKING`: ordena todos os usuários pelo engajamento.

Os demais itens da atividade são responsabilidade do outro integrante.

## Organização do código

- `py/heap.py`: heap de máximo criada manualmente para selecionar sugestões.
- `py/grafo.py`: lista de adjacência dos seguidores e cálculo dos candidatos.
- `py/avl.py`: árvore AVL, rotações e busca por intervalo de datas.
- `py/ordenacao.py`: cálculo de engajamento e Merge Sort próprio.
- `py/main.py`: menu que carrega os dados e chama as três funcionalidades.
- `py/tests/`: testes automatizados das estruturas e do menu.

## Escolhas e complexidade

O grafo foi representado por listas de adjacência. Como os IDs vão de 1 a
2000, vetores indexados por `id - 1` foram usados para marcar quem já é
seguido e contar conexões em comum, sem usar dicionários. Os candidatos são
colocados em uma heap de máximo, priorizando mais conexões em comum e usando
o `@usuario` como desempate.

Os posts são indexados por data em uma AVL. A chave é a própria string
`AAAA-MM-DD`, pois esse formato permite comparar datas em ordem cronológica.
Cada nó guarda todos os posts da mesma data. A consulta desce apenas nos
ramos que ainda podem conter o intervalo procurado.

O ranking usa Merge Sort, pois tem complexidade O(n log n). O engajamento é
calculado por `seguidores * 2 + soma das curtidas dos posts`; em empate, vale
a ordem alfabética do `@usuario`.

| Funcionalidade | Complexidade principal |
| --- | --- |
| Sugestões | O(U + G + C log(C + 1)) |
| Inserção AVL | O(log D) |
| Posts entre datas | O(log D + P) |
| Ranking | O(U + E + P + U log U) |

U é o número de usuários, G as conexões percorridas, C os candidatos, D as
datas distintas, P os posts retornados ou processados e E as conexões totais.

## Testes realizados

Foram executados os testes automatizados com:

```text
python -m unittest discover -s py/tests -v
```

Foram validados heap vazia, prioridade e desempate, usuário inexistente,
usuário sem seguidos, exclusão de usuários já seguidos, rotações AVL,
intervalos com limites incluídos, múltiplos posts na mesma data, intervalo
sem posts, cálculo de engajamento, desempate do ranking e entradas inválidas
no menu.

Também foi executado `python py/main.py` com os arquivos fornecidos. No teste
manual, `@henrique_nascimento` recebeu duas sugestões, a consulta de
`2025-01-01` a `2025-01-01` retornou 37 posts e o ranking exibiu os 20
primeiros usuários.
