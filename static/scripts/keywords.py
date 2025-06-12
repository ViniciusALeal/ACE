#VARIAVEL A {}
#VARIAVEL B {}
#VARIAVEL C {}
#ESTRUTURA E {}
#ESTRUTURA AUXILIAR 1 EE {}
#ESTRUTURA AUXILAIR 2 EE {}

variaveis = {
    0: "False",
    1: "True",
    
}
ifs = {
    0: """
if {a} > {b}:
    print("Entrou no if: {a} é maior que {b}")
    {e}
""",

    1: """
if {a} < {b}:
    print("Entrou no if: {a} é menor que {b}")
    {e}
""",

    2: """
if {a} and {b}:
    print("Entrou no if: {a} e {b} são verdadeiros")
    {e}
""",

    3: """
if {a} or {b}:
    print("Entrou no if: pelo menos um entre {a} e {b} é verdadeiro")
    {e}
"""
}
ifelse = {
    0: """
if {a} > {b}:
    print("Entrou no if: {a} é maior que {b}")
    {e}
else:
    print("Entrou no else: {b} é maior ou igual a {a}")
    {ee}
""",

    1: """
if {a} < {b}:
    print("Entrou no if: {a} é menor que {b}")
    {e}
else:
    print("Entrou no else: {a} é maior ou igual a {b}")
    {ee}
""",

    2: """
if {a} and {b}:
    print("Entrou no if: {a} e {b} são verdadeiros")
    {e}
else:
    print("Entrou no else: {a} ou {b} é falso")
    {ee}
""",

    3: """
if {a} or {b}:
    print("Entrou no if: pelo menos um entre {a} e {b} é verdadeiro")
    {e}
else:
    print("Entrou no else: {a} e {b} são falsos")
    {ee}
"""
}
ifelifelse = {
    0: """
if {a} > {b}:
    print("Entrou no if: {a} é maior que {b}")
    {e}
elif {a} < {b}:
    print("Entrou no elif: {a} é menor que {b}")
    {ee}
else:
    print("Entrou no else: {a} é igual a {b}")
    {eee}
""",
    1: """
if {a} < {b}:
    print("Entrou no if: {a} é menor que {b}")
    {e}
elif {a} > {b}:
    print("Entrou no elif: {a} é maior que {b}")
    {ee}
else:
    print("Entrou no else: {a} é igual a {b}")
    {eee}
""",
    2: """
if {a} and {b}:
    print("Entrou no if: {a} e {b} são verdadeiros")
    {e}
elif {a} or {b}:
    print("Entrou no elif: pelo menos um entre {a} e {b} é verdadeiro")
    {ee}
else:
    print("Entrou no else: {a} e {b} são falsos")
    {eee}
""",
    3: """
if {a} or {b}:
    print("Entrou no if: pelo menos um entre {a} e {b} é verdadeiro")
    {e}
elif {a} and {b}:
    print("Entrou no elif: ambos {a} e {b} são verdadeiros")
    {ee}
else:
    print("Entrou no else: {a} e {b} são falsos")
    {eee}
"""
}
excecoes = {
    #"try"
    0: """
try:
    {e}
    print("Operação bem-sucedida")
""",

    #"except"
    1: """
except Exception as e:
    print(f"Erro capturado: {e}")
    {e}
""",

    #"finally"
    2: """
finally:
    print("Executando o bloco finally")
    {e}
""",

    #"raise"
    3: """
if {a}:
    print("Erro levantado: {b}")
    raise Exception({b})
""",

    #"assert"
    4: """
assert {a}, "Erro: {a} deveria ser verdadeiro"
"""
}
funcoes_classes = {
    #"def"
    0: """
def {a}({b}):
    print("Executando função {a} com argumento {b}")
    {e}
""",
    #"lambda"
    1: """
{a} = lambda {b}: {c}
print("Executando lambda:", "{a}({b})")
""",
    #"class"
    2: """
class {a}:
    def __init__(self, {b}):
        print("Criando instância de {a} com {b}")
        self.{b} = {b}
"""
}
operadores = {
    #"is"
    0: """
if {a} is {b}:
    print("{a} e {b} são o mesmo objeto")
""",
    #"in"
    1: """
if {a} in {b}:
    print("{a} está dentro de {b}")
""",
    #"not"
    2: """
if not {a}:
    print("{a} é falso")
"""
}
pattern_matching = {
    #"match"
    0: """
match {a}:
    print("Executando match com {a}")
    case _:
        print("")
""",
    #"case"
    1: """
case {b}:
    print("Case ativado para {b}")
    {e}
"""
}
whiles = {
    0: """
while {a}:
    print("Entrou no while: {a} é verdadeiro")
    {e}
"""
}

controle_fluxo = {
    #"break"
    0: """
    print("Break acionado, saindo do loop")
    break
""",
    #"continue"
    1: """
    print("Continue acionado, pulando para a próxima iteração")
    continue
"""
}

estrutura_codigo = {
    
    # ifs
    0: ifs,
    # if-else
    1: ifelse,
    # if-elif-else
    2: ifelifelse,
    # loops while
    3: whiles,
    # controle de fluxo (break/continue)
    8: controle_fluxo,
    # exceções
    5: excecoes,
    # funções e classes
    6: funcoes_classes,
    # operadores
    7: operadores,
    # pattern matching
    4: pattern_matching
}
