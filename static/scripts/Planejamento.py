

# sessão de planejamento 
#  seleções
# Roleta
# Torneio
# Rank-based
# Amostragem
# Truncado
# Elitismo

# Metricas

#  Complexidade Ciclonática
# Numero de linhas por função/ método
# Profundidae de alinhamento
# Acoplamento entre módulos
# coesão
# Loc lines of code
# Número de Classes metodos funções
#  fan-in fan-out
# código duplicado
# uso de "code smells"
# violação de padrões de estilo (linting)
# tempo de execução
# Alocação de memória por operação
# Big O

#como pretendo aplicar

# seleções
#   metodos de eliminação ou seleção 
# Roleta
#   função aleatoria random pareando com numero de genomas
# Torneio
#   pareamento de duplas 
# Rank-based
#   rankeamento 
# Amostragem
#   random com parametros de nivelamento para que a representação e variedade não seja alterada
# Truncado
#   apenas X% é selecionado entre os melhores
# Elitismo
#   apenas X% é seleciona entre os melhores porem não são alterados a elete é mantida inalterada

# Metricas

#  Complexidade Ciclonática
# Numero de linhas por função/ método
# Complexidade Ciclomática = E − N + 2P
"""omplexidade Ciclomática (radon cc)
O que é:
Mede a quantidade de caminhos lógicos independentes em um código. Isso ajuda a estimar a dificuldade de teste e manutenção.

Como é calculado:
Fórmula simplificada:

Complexidade Ciclomática = 1 + número de decisões
Decisões incluem:

if, elif, else

for, while

try, except, finally

Expressões com and, or

Alguns return, yield, raise

Classificação usada pelo Radon:
Grau	Complexidade	Nível de atenção
A	1–5	Baixo (bom)
B	6–10	Moderado
C	11–20	Médio
D	21–30	Alto
E	31–40	Muito alto
F	41+	Crítico

Comando:
radon cc arquivo.py -s -a


"""
# Profundidae de alinhamento
"""    
Profundidade de Aninhamento (Nesting)
O que é:
Refere-se ao número máximo de blocos de controle aninhados uns dentro dos outros, como if dentro de for dentro de while.

Embora o Radon não mostre essa métrica isoladamente, ela afeta diretamente a complexidade ciclomática e o índice de manutenibilidade.

Para ver a profundidade de aninhamento de forma explícita, é recomendado usar a ferramenta lizard:

lizard arquivo.py
"""
# Acoplamento entre módulos
"""O que aconteceu?
ast.parse(codigo) transformou o texto em uma árvore que representa o código.
ast.walk(arvore) percorre todos os nós dessa árvore.
Identificamos os tipos de nós 
(função, chamada, etc).
Extraímos informações úteis
(nome da função, número de argumentos, nome da função chamada).

Por que usar ast?
Porque é mais seguro e preciso do que usar regex para analisar código.
Permite fazer análises complexas, como contar chamadas, 
medir acoplamento, identificar estruturas de controle."""
# coesão
"""O que é o ast?
O módulo ast do Python converte seu código fonte (texto) em uma árvore de sintaxe abstrata. Essa árvore representa a estrutura do código — por exemplo, onde estão as funções, classes, variáveis, chamadas de métodos, etc.

Com essa árvore, você pode navegar e analisar o código de forma estruturada, diferente de só buscar palavras no texto (como regex faria).

Como usar o ast para analisar coesão?
Parsear o código: transforma o código em texto numa árvore.

Visitar os nós da árvore: cada parte do código é um nó — funções, classes, atribuições, chamadas.

Dentro de uma classe, você pode:

Percorrer os métodos (funções da classe).

Para cada método, encontrar quais atributos do objeto (self) são acessados ou modificados.

Comparar os atributos usados entre métodos:

Se muitos métodos acessam os mesmos atributos, a coesão é alta.

Se cada método usa atributos diferentes ou quase não usa atributos, a coesão é baixa.

Por que usar o ast para isso?
Você não depende de buscas de texto, que podem ser imprecisas.

Pode garantir que está analisando só os acessos reais a atributos.

Pode diferenciar contextos, como métodos, classes, etc.

Evita pegar atributos em comentários, strings ou trechos inválidos.

Exemplo do processo, em resumo
O ast identifica uma classe chamada Exemplo.

Dentro da classe, identifica 3 métodos: metodo1, metodo2, metodo3.

Para cada método, o ast percorre e anota quais atributos self.a, self.b são usados.

Depois, calcula quantos pares de métodos compartilham atributos em comum.

Essa proporção indica a coesão: próximo de 1 é alta coesão, próximo de 0 é baixa.

Em resumo
AST = representação estrutural do código que permite analisar o código de forma organizada.

Com ela, você pode extrair dados para calcular métricas como coesão, 
analisando o uso de atributos compartilhados dentro de classes, tudo isso sem mexer no código, só lendo e interpretando."""
# Loc lines of code
"""Linhas de Código (radon raw)
O que é:
Conta o número de linhas no código, com diferentes classificações.

Métricas exibidas:
LOC: Linhas totais no arquivo

LLOC: Linhas lógicas de código (com instruções)

SLOC: Linhas de código, excluindo comentários e espaços em branco

Comments: Linhas de comentário

Blank: Linhas em branco

Comando:
radon raw arquivo.py"""
# Número de Classes metodos funções
"""ast do Python para contar o número de classes, métodos e funções em um código-fonte.

Conceitos básicos
Classe: bloco definido com class Nome:.

Método: função definida dentro de uma classe (função que tem self como primeiro parâmetro).

Função: função definida fora de uma classe (definida no escopo global ou em outro lugar que não seja dentro de classe).

Como fazer com ast
Parsear o código em uma árvore.

Percorrer os nós procurando:

ClassDef → representa uma classe.

FunctionDef → representa uma função ou método.

Para distinguir método de função, verificar se a função está dentro de uma classe.

Contar quantos desses nós aparecem."""
#  fan-in fan-out
"""Como medir com AST
Para cada função/módulo, conte quantas vezes ele é chamado por outros → Fan-in.

Conte quantas chamadas ele faz para outras funções/módulos → Fan-out.

Isso pode ser obtido analisando chamadas de funções (ast.Call) dentro do código, como mostrei no exemplo anterior."""
# código duplicado
"""Quebrar o código em blocos (funções, classes ou blocos de N linhas).

Comparar blocos entre si para ver se são idênticos ou muito parecidos.

Identificar duplicações."""
# uso de "code smells"
""" lógica básica para detectar um code smell de função muito longa usando AST:

Para cada função no código:

Calcule o número de linhas da função (linha_final - linha_inicial + 1).

Se o número de linhas for maior que um limite definido (ex: 50 linhas):

  Marque a função como tendo o code smell de "função longa"."""
# violação de padrões de estilo (linting)
"""O que o Pylint faz?
Detecta violações de padrões de estilo (PEP8 e outras regras).

Encontra erros comuns, como variáveis não usadas, imports inválidos, etc.

Avalia complexidade do código (complexidade ciclomática, tamanho de funções).

Aponta possíveis problemas como código duplicado, nomes inadequados.

Dá uma nota para o código (de 0 a 10)."""
# tempo de execução
"""trecho de código (função, bloco, script):

Lógica para medir tempo de execução
Antes de executar o código, registre o tempo inicial (timestamp).

Execute o código ou função que deseja medir.

Após a execução, registre o tempo final.

Calcule a diferença:
tempo_execucao = tempo_final - tempo_inicial

Use esse valor para analisar desempenho, comparar versões ou otimizar.

Em Python, um exemplo simples usando time:
python

import time

inicio = time.time()
# código que você quer medir
fim = time.time()

print(f"Tempo de execução: {fim - inicio} segundos")"""
# Alocação de memória por operação
"""Lógica básica para medir alocação de memória
Antes de executar a operação, registre o uso atual de memória.

Execute a operação (função, trecho de código).

Registre o uso de memória imediatamente após a execução.

Calcule a diferença:
memoria_alocada = memoria_depois - memoria_antes

Use essa informação para analisar impacto da operação no consumo de memória."""
# Big O
"""Lógica básica para medir alocação de memória
Antes de executar a operação, registre o uso atual de memória.

Execute a operação (função, trecho de código).

Registre o uso de memória imediatamente após a execução.

Calcule a diferença:
memoria_alocada = memoria_depois - memoria_antes

Use essa informação para analisar impacto da operação no consumo de memória."""
# manutenabilidade
"""
Índice de Manutenibilidade (radon mi)
O que é:
Pontuação que indica o quão fácil é manter o código. Quanto maior a pontuação, mais fácil de manter.

Fatores considerados:
Complexidade ciclomática

Número de linhas de código

Porcentagem de comentários

Fórmula (simplificada):

MI = 171 - 5.2 * log2(volume) - 0.23 * complexidade - 16.2 * log2(LOC) + 50 * sin(√(2.4 * %comentários))
Interpretação dos resultados:
Índice	Interpretação
85–100	Muito fácil de manter
65–85	Aceitável
< 65	Difícil de manter

Comando:
radon mi arquivo.py -s"""