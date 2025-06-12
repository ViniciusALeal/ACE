import re


# A
def achar_placeholdersA(codigo):
    if re.search(r'\{a\}', codigo):
        return True
    else:
        return False
def substituir_placeolderA(codigo,valor):
    codigo = re.sub(r"{a}", valor, codigo)
    return codigo
    
# B
def achar_placeholdersB(codigo):
    if re.search(r'\{b\}', codigo):
        return True
    else:
        return False
def substituir_placeolderB(codigo,valor):
    codigo = re.sub(r"{b}", valor, codigo)
    return codigo   

# C
def achar_placeholdersC(codigo):
    if re.search(r'\{c\}', codigo):
        return True
    else:
        return False
def substituir_placeolderC(codigo,valor):
    codigo = re.sub(r"{c}", valor, codigo)
    return codigo

# E 
def achar_placeholdersE(codigo):
    if re.search(r'\{e\}', codigo):
        return True
    else:
        return False
def substituir_placeolderE(codigo,valor):
    codigo = re.sub(r"{e}", valor, codigo)
    return codigo

# EE 
def achar_placeholdersEE(codigo):
    if re.search(r'\{ee\}', codigo):
        return True
    else:
        return False
def substituir_placeolderEE(codigo,bloco):
    codigo = re.sub(r"{ee}", bloco, codigo)
    return codigo   

# EEE  
def achar_placeholdersEEE(codigo):
    if re.search(r'\{eee\}', codigo):
        return True
    else:
        return False
def substituir_placeolderEEE(codigo,bloco):
    codigo = re.sub(r"{eee}", bloco, codigo)
    return codigo




