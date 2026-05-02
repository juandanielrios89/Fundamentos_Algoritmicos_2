def evaluar_numeros(lista):
    print("Iniciando analisis algoritmico")
    for numero in lista:
        if numero % 2 == 0:
            print(f"[{numero}] -es par")
        else:
            print(f"[{numero}] -es impar")

mis_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evaluar_numeros(mis_numeros) 