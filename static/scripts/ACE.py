from ai import resposta_llm
from genoma import gerar_genoma
import random


def fitness(type):
    tamanho = 10
    genoma = gerar_genoma(int(tamanho))
    match type:
        case "llm":
            llmscore = f"de um score para esse código de 1 a 100 apenas o numero: {genoma}"
            print((resposta_llm((llmscore))))
        case "listest":
            pass
        case "simpletest":
            pass
while True:
    run=fitness(input())