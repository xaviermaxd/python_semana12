def esvocal(x):
    vocales = ["a","e","i","o","u"]

    if x in vocales: 
        return True
    else:
        return False

def vocal_line(vocal):
    return True if vocal in ["a","e","i","o","u"] else False

vocal = input("ingrese una vocal: ")
print(esvocal(vocal))
print(vocal_line(vocal))