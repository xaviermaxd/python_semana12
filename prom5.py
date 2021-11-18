def sumar(numeros) -> int : 
    return sum(numeros)

def multiplicar(numeros) -> int:
    mul = 1
    for i in numeros:
        mul *= i
    return mul

lista = [1,2,3,4]

print("la suma es: ",sumar(lista))
print("la multiplicacion es: ",multiplicar(lista))