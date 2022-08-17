"""Actividad 1. Programar algoritmo César para cifrar y descifrar para k==3"""

def cifrarCesar(cadena,k):
    """Función para realizar cifrado cesar por desplazamiento
    utilizando una llave k"""
    # K es igual a la llave de desplazamiento
    # cadena es el mensaje a cifrar
    cifrado = ""
    cadena=cadena.upper()
    for c in cadena:
        #Se verifica si es una letra mayuscula, para filtrar los espacios
        if c.isupper():
            # Se busca la posición del caracter en el código ascii
            c_ascii = ord(c)
            c_indice = ord(c) - ord("A")
            # Creación del indice de desplazamiento con la llave k
            nuevo_indice = (c_indice + k) % 26
            # Se obtiene el ascii del caracter cifrado
            nuevo_ascii = nuevo_indice + ord("A")
            #Se crea el nuevo caracter cifrado
            nuevo_caracter = chr(nuevo_ascii)
            # Concatenación de cadena final con el mensaje cifrado
            cifrado = cifrado + nuevo_caracter
        else:
            #Si es un espacio o algi distinto a una letra mayuscula, pasa tal cual
            cifrado += c
    return cifrado


def descifrarCesar(texto_cifrado,k):
    """Función para realizar cifrado cesar por desplazamiento
    utilizando una llave k"""
    # K es igual a la llave de desplazamiento
    # texto_cifrado es el mensaje a descifrar
    texto_claro = ""
    #texto_cifrado=texto_cifrado.upper()
    print("\tDescifrando - "+texto_cifrado+" ...")
    for c in texto_cifrado:
        if c.isupper():
            # Se busca la posición del caracter entre 0-25
            c_ascii = ord(c)
            c_indice = ord(c) - ord("A")
            # Efectuando el valor de la llave k para obtner el mensaje original
            nuevo_indice = (c_indice - k) % 26
            # Obtención del equivalente en ascii del caracter del mensaje original
            nuevo_ascii = nuevo_indice + ord("A")
            # Creación del caracter a partir de su valor entero en ascii
            nuevo_caracter = chr(nuevo_ascii)
            # Concatenación de cadena final con el texto descifrado
            texto_claro = texto_claro + nuevo_caracter
        else:
            #Si es un espacio o algi distinto a una letra mayuscula, pasa tal cual
            texto_claro += c
    return texto_claro

cadena="me llamo hugo y soy alumno de la facultad de ingenieria"

print("\tCifrado con Cesar utilizando llave k=3\n")
print("Texto en claro:",cadena)
texto_cifrado=cifrarCesar(cadena,3)

print("Texto cifrado",texto_cifrado)
texto_claro=descifrarCesar(texto_cifrado,3)
print("Texto descifrado",texto_claro)


# Inciso b. con palabra cable y completando el abecedario
def CesarClave(mensaje,clave):
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    clave=clave.upper()
    clave=list(clave)
    abecedario_cifrado=[]
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    
    #Colocación de la clave en el nuevo abecedario de cifrado.
    for i in clave:
        if i not in abecedario_cifrado:
            abecedario_cifrado.append(i)

    # Complementando el abecedario de cifrado
    for i in abecedario_claro:
        if i not in abecedario_cifrado:
            abecedario_cifrado.append(i)
    cifrado=[]
    indice=0
    for i in mensaje:
        if i.isupper():
            indice=abecedario_claro.index(i)
            cifrado.append(abecedario_cifrado[indice])
        else:
            cifrado += i
    cifrado="".join(cifrado)
    return cifrado

def DescidrarCesarClave(texto_cifrado,clave):
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    clave=clave.upper()
    clave=list(clave)
    abecedario_cifrado=[]
    for i in clave:
        if i not in abecedario_cifrado:
            abecedario_cifrado.append(i)

    # Complementando el abecedario de cifrado
    for i in abecedario_claro:
        if i not in abecedario_cifrado:
            abecedario_cifrado.append(i)
            
    texto_cifrado=texto_cifrado.upper()
    texto_cifrado=list(texto_cifrado)

    texto_claro=[]
    indice=0
    for i in texto_cifrado:
        if i.isupper():
            indice=abecedario_cifrado.index(i)
            texto_claro.append(abecedario_claro[indice])
        else:
            texto_claro += i
    texto_claro="".join(texto_claro)
    return texto_claro

mensaje="me llamo hugo y soy alumno de la facultad de ingenieria"
clave="seguridad"
print("\tCifrado con Cesar y palabra clave completando abecedario\n")
print("Texto en claro: ",mensaje)
cifrado=CesarClave(mensaje,clave)
print("Texto cifrado: ",cifrado)
claro=DescidrarCesarClave(cifrado,clave)
print("Texto descifrado: ",claro)


# Actividad 2 Programar el algoritmo Hill - Cifrar y Descifrar

def modulo27(valor):
    mod27=valor%27
    if mod27<0:
        mod27=mod27+27
    return mod27

def factor_modular(a):
    #a*b mod 27 = 1
    for i in range(100):
        valor=a*i%27
        if  valor == 1:
            b=i
            break
    return b

def matriz_cofactores(matriz,n):
    from numpy import matrix,zeros,size
    from numpy.linalg import det
    MC=matrix(zeros((n,n))) # Matriz de cofactores
    idx=matrix(range(n))
    for i in range(size(A,0)):
        for j in range(size(A,1)):
            fidx=idx[idx!=i]
            cidx=idx[idx!=j]
            cof=A[[[fidx[0,0]],[fidx[0,1]]],cidx]
            MC[i,j]=pow(-1,i+j)*det(cof)
    return MC
            
def cifrado_Hill(mensaje, llave):            
    import numpy as np
    import math as mt
    abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario=list(abecedario)
    contenido_matriz=[]
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    llave=llave.upper()
    llave=list(llave)
    tamano_mensaje=len(mensaje)
    faltante=0
    if not tamano_mensaje%2 == 0 or not tamano_mensaje%3 == 0 or not tamano_mensaje%4==0:
        if 2 < tamano_mensaje < 9:
            faltante=9-tamano_mensaje
        elif 9 < tamano_mensaje < 16:
            faltante=16-tamano_mensaje
        for i in range(faltante):
            mensaje.append("Z")
    mensaje_cifrado=[]
    ngramas_claro=[]
    ngramas_cifrado=[]
    aux=[]
    aux2=[]
    aux3=[]
    MMensaje=[]
    raiz_K=int(mt.sqrt(len(llave)))
    if tam_llave==4 or tam_llave==9 or tam_llave==16:
        for i in range(raiz_K):
            for j in range(raiz_K):
                indice=abecedario.index(llave[j+raiz_K*i])
                aux.append(int(indice))
            contenido_matriz.append(aux)
            aux=[]
        K=np.matrix(contenido_matriz)
    else:
        print("El tamaño de la llave debe ser de 4 o 9 o 16 caracteres")
    det_K=round(np.linalg.det(K))
    det_K=det_k%27
    print("El determinante de la matriz K es: ",det_K)
    adj_K=matriz_cofactores(K,raiz_K)%27
    adjT_K=np.transpose(adj_K)
    inv_det_K=factor_modular(det_K)
    K_inv=inv_det_K*adjT_K%27
    print("\nLa inversa de la matriz clave (K) es:")
    print(K_inv)
    for i in range(len(mensaje)//raiz_K):
        for j in range(raiz_K):
            indice=abecedario.index(mensaje[j+raiz_K*i])
            #aux.append(mensaje[j+raiz_K*i])
            aux.append(int(indice))
        for n in aux:
            aux2.append(n)
            aux3.append(aux2)
            aux2=[] 
        MMensaje=np.matrix(aux3)
        aux3=[]
        C=np.matrix(K*MMensaje%27)
        C=C.tolist()
        for a in C:
            for b in a:
                mensaje_cifrado.append(abecedario[b])
        ngramas_claro.append(aux)
        aux=[]
    mensaje_cifrado="".join(mensaje_cifrado)   
    return mensaje_cifrado

def descifrado_Hill(mensaje_cifrado, llave):
    import numpy as np
    import math as mt
    abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario=list(abecedario)
    contenido_matriz=[]
    llave=llave.upper()
    llave=list(llave)
    mensaje_cifrado=mensaje_cifrado.upper()
    mensaje_cifrado=list(mensaje_cifrado)
    mensaje_claro=[] 
    ngramas_claro=[]
    ngramas_cifrado=[]
    aux=[]
    aux2=[]
    aux3=[]
    MMensaje=[]
    raiz_K=int(mt.sqrt(len(llave)))
    if tam_llave==4 or tam_llave==9 or tam_llave==16:
        for i in range(raiz_K):
            for j in range(raiz_K):
                indice=abecedario.index(llave[j+raiz_K*i])
                aux.append(int(indice))
            contenido_matriz.append(aux)
            aux=[]
        K=np.matrix(contenido_matriz)
    else:
        print("El tamaño de la llave debe ser de 4 o 9 o 16 caracteres")  
    det_K=round(np.linalg.det(K))
    det_K=det_k%27
    print("El determinante de la matriz K es: ",det_K)
    adj_K=matriz_cofactores(K,raiz_K)%27
    adjT_K=np.transpose(adj_K)
    inv_det_K=factor_modular(det_K)
    K_inv=inv_det_K*adjT_K%27
    print("\nLa inversa de la matriz clave (K) es:")
    print(K_inv)
    for i in range(len(mensaje_cifrado)//raiz_K):
        for j in range(raiz_K):
            indice=abecedario.index(mensaje_cifrado[j+raiz_K*i])
            #aux.append(mensaje[j+raiz_K*i])
            aux.append(int(indice))
        for n in aux:
            aux2.append(n)
            aux3.append(aux2)
            aux2=[]
        MMensaje=np.matrix(aux3)
        aux3=[]
        M=np.matrix(K_inv*MMensaje%27)
        M=M.tolist()
        for a in M:
            for b in a:
                mensaje_claro.append(abecedario[int(round(b))])
        ngramas_claro.append(aux)
        aux=[]
    mensaje_claro="".join(mensaje_claro) 
    return mensaje_claro

print("\tCifrado con Hill\n")

mensaje_cifrado=cifrado_Hill("AMIGOCONDUCTOR", "peligroso")
print("\nEl mensaje cifrado es: ",mensaje_cifrado)  

mensaje_claro=descifrado_Hill(mensaje_cifrado, "peligroso")
print("\nEl mensaje descifrado es: ",mensaje_claro)

