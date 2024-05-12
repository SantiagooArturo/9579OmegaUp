
M = int(input("Ingrese cantidad de operaciones: "))

for m in range(M):

    arr = [2,4,6,8,10]
    longitud_arr_inicial = len(arr)
    arr_diferencia = []
    N = 5 #cantidad de valores que va completar segun la diferencia en la que avanza la secuencia

    """"
    diferencia = 0
    #DETERMINAR SUECUENCIA
    for i in range(len(arr)):
        diferencia  = arr[i] - arr[i - 1]
        arr_diferencia.append(diferencia)
    """

    confirmacion = False
    intervalo_diferencia = 0

    for i in range(1, int((len(arr))/2)):
        #print(i)
        #print(arr[i], arr[i - 1])
            
        if(arr[i] - arr[i - 1] == arr[i + 1] - arr[i]):
            confirmacion = True
            intervalo_diferencia = arr[i] - arr[i - 1]
        else:
            confirmacion = False
    
    print(confirmacion, intervalo_diferencia)

    for a in range(N):        
        for i in range(len(arr)):
            arr.append(arr[-1] + intervalo_diferencia)
            break
        
        
    M = 2 #cantidad de veces que se van a efectuar las operaciones
    I = 0  
    F = 0  
    suma = 0

    I = int(input("ingrese I: "))
    arr[I] = "V"
    F = int(input("Ingrese F"))
        
    while(F > 0 and F <= len(arr)):
        interv_fin = F - 1
        suma = sum(arr[I + 1:interv_fin])
        break

    print(suma)

    print(arr)