print("hola")


'''

----> FUNCION ---->

'''

total = 10

def suma_rara(numero1, numero2=7, ganado = True, vaca = "mu"):
    if numero1 <5:
        suma = numero1 + numero2 + total
        total2 = suma + 10000
        return suma
    else:
        return 7
    

def suma2():
    num1 = float(input("introduce el número 1: "))
    num2 = float(input("introduce el número 2: "))
    
    suma = num1 + num2
    print("suma hecha")
    return suma

def saludo():
    print("hola")
    

print("hola") #None
valor_retornado = len([5,6])
    

valor_retornado = suma_rara(2,3)
print(valor_retornado)
print(total)
# suma() --> el valor del return

print(suma2())


print("hola, Federico")
print("hola, Manuela")
print("hola, mucha gente")

def saluda_amigo(nombre):
    print("hola, " + nombre)
    
    
def suma_muchos(*numeros):
    '''
    Por favor, solo tres argumentos
    '''
    print(type(numeros))
    maximo = max(numeros)
    minimo = min(numeros)
    if minimo < 0 or maximo > 10:
        return 0
    else:
        return sum(numeros)



print("suma total", suma_muchos(1,5,4,2,7,8,4,5,6,3,5)) # args = (1,5,4,2,7,8,4,5,6,3,5)

print(help(suma_muchos))



def compra_cafe(**kwargs):
    print(kwargs)
    return kwargs
    
comprando_dic = compra_cafe(precio = 50, color="azul")

print(type(comprando_dic))

