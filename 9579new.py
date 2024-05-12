
def procesar_operaciones(entrada, operaciones):
 
    tamano = entrada[0]
    arreglo = entrada[1:]

    # Procesar cada operación
    for operacion in operaciones:
        tipo = operacion[0]
        if tipo == 'C':
           
            i = operacion[1] - 1  # Restamos 1 para ajustar el índice al contar desde 0
            nuevo_valor = operacion[2]
            arreglo[i] = nuevo_valor
        elif tipo == 'P':
            
            a = operacion[1] - 1  # Restamos 1 para ajustar el índice al contar desde 0
            b = operacion[2]
            suma_intervalo = sum(arreglo[a:b])
            print(suma_intervalo)

# Leer la entrada
entrada = list(map(int, input().split()))
num_elementos = entrada[0]
elementos_arreglo = list(map(int, input().split()))

M = int(input())

operaciones = []
# Leer la descripción de las operaciones
for _ in range(M):
    operacion = input().split()
    operacion[1:] = map(int, operacion[1:])
    operaciones.append(operacion)

# Procesar las operaciones
procesar_operaciones([num_elementos] + elementos_arreglo, operaciones)