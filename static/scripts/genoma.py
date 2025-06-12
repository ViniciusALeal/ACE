import random
from keywords import estrutura_codigo, variaveis 
from placeholder import *

def seletor_de_estrutura_externa(n):
    if n not in estrutura_codigo:
        print(f"Erro: chave {n} não encontrada em estrutura_codigo")
        return None
    return estrutura_codigo[n]
    
def seletor_de_estrutura_interna(n, nn):
    estrutura = seletor_de_estrutura_externa(n)
    if estrutura is None:
        print(f"Erro: estrutura externa para {n} é None")
        return None
    if nn not in estrutura:
        print(f"Erro: chave {nn} não encontrada na estrutura interna de {n}")
        return None
    return estrutura[nn]


def seletor_de_variaveis(n):
        variavel = variaveis[n]
        return variavel  # Se já for uma string, retorna diretamente



# Função para selecionar aleatoriamente um índice do dicionário de estruturas
def seletor(lista):
    
    return random.choice(list(lista))


# Função para gerar o genoma, que agora será uma lista de números
def gerar_genoma(tamanho):
    genoma = []  # Inicializa o genoma como uma lista vazia
    self = []
    B =0
    E =0
    numero = seletor(list(estrutura_codigo))  # Seleciona um índice aleatório dentro de estrutura_codigo
    print(numero)
    while numero==8:
         numero = seletor(list(estrutura_codigo))  # Seleciona um índice aleatório dentro de estrutura_codigo
    print(numero)
    genoma.append(numero)  # Adiciona o número ao genoma
    B=numero
    numero = seletor(list(seletor_de_estrutura_externa(B)))  # Seleciona um índice aleatório dentro de estrutura_codigo
    genoma.append(numero)  # Adiciona o número ao genoma
    print(numero)
    E=numero
    estrutura= seletor_de_estrutura_interna(B,E)
    print(estrutura)
    self.append(seletor_de_estrutura_interna(B,E))
    codigo=str(estrutura)

    if achar_placeholdersA(codigo) == True:
            numero = seletor(list(variaveis))
            variavel= seletor_de_variaveis(numero)
            print(variavel)
            while variavel == None:
                print(variavel,"não é um valor incial valido")
                numero = seletor(list(variaveis))
                variavel= seletor_de_variaveis(numero)
                print(variavel)
            genoma.append(numero)
            self.append(seletor_de_variaveis(numero))
            codigo= substituir_placeolderA(codigo,variavel)
            tamanho+1
            
    if achar_placeholdersB(codigo) == True:
            numero= seletor(list(variaveis))
            genoma.append(numero)
            variavel= seletor_de_variaveis(numero)
            print(variavel)
            self.append(seletor_de_variaveis(numero))
            codigo=substituir_placeolderB(codigo,variavel)
            tamanho+1

    if achar_placeholdersC(codigo) == True:
            numero= seletor(list(variaveis))
            genoma.append(numero)
            variavel= seletor_de_variaveis(numero)
            print(variavel)
            self.append(seletor_de_variaveis(numero))
            codigo= substituir_placeolderC(codigo,variavel)
            tamanho+1

    while tamanho >= len(genoma):
            

        if tamanho >= 1:
            if achar_placeholdersE(codigo) == True:
                numero= seletor(list(estrutura_codigo))
                genoma.append(numero)
                B= numero
                print(numero)
                numero = seletor(list(seletor_de_estrutura_externa(B))) 
                genoma.append(numero)
                E= numero
                print(numero)
                self.append(seletor_de_estrutura_interna(B,E))
                codigo= substituir_placeolderE(codigo,seletor_de_estrutura_interna(B,E))
                codigo=str(codigo)

            if achar_placeholdersA(codigo) == True:
                    numero = seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderA(codigo,variavel)
                    tamanho+1
                    
            if achar_placeholdersB(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo=substituir_placeolderB(codigo,variavel)
                    tamanho+1

            if achar_placeholdersC(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderC(codigo,variavel)
                    tamanho+1
                
        if tamanho >= 1:

            if achar_placeholdersEE(codigo) == True:
                numero= seletor(list(estrutura_codigo))
                genoma.append(numero)
                B= numero
                print(numero)
                numero = seletor(list(seletor_de_estrutura_externa(B))) 
                genoma.append(numero)
                E= numero
                print(numero)
                self.append(seletor_de_estrutura_interna(B,E))
                codigo= substituir_placeolderE(codigo,seletor_de_estrutura_interna(B,E))
                codigo=str(codigo)

            if achar_placeholdersA(codigo) == True:
                    numero = seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderA(codigo,variavel)
                    tamanho+1
                    
            if achar_placeholdersB(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo=substituir_placeolderB(codigo,variavel)
                    tamanho+1

            if achar_placeholdersC(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderC(codigo,variavel)
                    tamanho+1
                    
        if tamanho >= 1:

            if achar_placeholdersEEE(codigo) == True:
                numero= seletor(list(estrutura_codigo))
                genoma.append(numero)
                B= numero
                print(numero)
                numero = seletor(list(seletor_de_estrutura_externa(B))) 
                genoma.append(numero)
                E= numero
                print(numero)
                self.append(seletor_de_estrutura_interna(B,E))
                codigo= substituir_placeolderE(codigo,seletor_de_estrutura_interna(B,E))
                codigo=str(codigo)

            if achar_placeholdersA(codigo) == True:
                    numero = seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderA(codigo,variavel)
                    tamanho+1
                    
            if achar_placeholdersB(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo=substituir_placeolderB(codigo,variavel)
                    tamanho+1

            if achar_placeholdersC(codigo) == True:
                    numero= seletor(list(variaveis))
                    genoma.append(numero)
                    variavel= seletor_de_variaveis(numero)
                    print(variavel)
                    self.append(seletor_de_variaveis(numero))
                    codigo= substituir_placeolderC(codigo,variavel)
                    tamanho+1
                    
            gene=[genoma,self,codigo]
            print(gene)
        return gene
