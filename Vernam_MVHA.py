#1. Programar el algoritmo Affin C=x*M+b, Cifrar y descifrar el lema de la
#Universidad. Usando x=1, b=7 donde M es el mensaje.

def AlgoritmoAfin(mensaje,x,b):
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    mensajeCifrado=[]
    
    #Obtención del caracter en claro y caracter cifrado en la posicion i
    for M in mensaje:
        if M != " ":
            Mi=abecedario_claro.index(M)
            Ci=(x*Mi+b)%27
            mensajeCifrado.append(abecedario_claro[Ci])
        else:
            mensajeCifrado.append(M)
    
    cifrado="".join(mensajeCifrado)
    
    return cifrado
    

def DescifrarAlgoritmoAfin(texto_cifrado,x,b):
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    texto_cifrado=texto_cifrado.upper()
    texto_cifrado=list(texto_cifrado)
    texto_claro=[]
    
    for C in texto_cifrado:
        if C != " ":
            Ci=abecedario_claro.index(C)
            Mi=(Ci-b)%27
            texto_claro.append(abecedario_claro[Mi])
        else:
            texto_claro.append(C)
    
    texto_claro="".join(texto_claro)
    return texto_claro



#2. Programar el algoritmo Vernam, Cifrar y descifrar el mensaje “Fernando Casa Sola”. 
#Usando la clave Santiago (recuerden es en binario).




def CifradoVernam(mensaje): 
    import random as rand
    import operator as op
    """Función de cifrado que requiere de una cedana de caracteres para cifrar
    y devuelce una tupla, con la cadena cifrada y una lista con las cadenas de bits
    aleatorias utilizadas para cifrar el mensaje."""
    print("\t\n*** Proceso de cifrado Vernam ***\n")
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    mensajeCifrado=[]
    mensajeClaroBin=[]
    mensajeCifradoBin=[]
    clave=[] #Lista que va a contener la cadena de bits aleatoria para el XOR
    claveBin=[]
    for i in range(len(mensaje)): #Obtenión de cadenas de bits aleatorias del mismo tamaño que el mensaje
        valorA=rand.randint(0,128)
        clave.append(valorA)
        claveBin.append(bin(valorA))
    for M in mensaje:  #Iteración para realizar el cifrado y operar los bits del mensaje xor los bits aleatorios
        index=mensaje.index(M)
        Mc=ord(M)
        mensajeClaroBin.append(bin(Mc))
        C=op.xor(Mc,clave[index])
        mensajeCifrado.append(chr(C))
        mensajeCifradoBin.append(bin(C))   
    cifrado="".join(mensajeCifrado)
    print("Esta es la cadea de bits del mensaje:")
    print(mensajeClaroBin)
    print("\nEsta es la cadea aleatoria de bits para cifrar:")
    print(claveBin)
    print("\nEsta es la cadea de bits del mensaje cifrado:")
    print(mensajeCifradoBin)
    
    return cifrado,clave


def DescifrarVernam(textoCifrado,clave):
    import random as rand
    import operator as op
    print("\t\n*** Proceso de descifrado Vernam ***\n")
    textoCifrado=list(textoCifrado)
    mensajeClaro=[]
    mensajeClaroBin=[]
    for C in textoCifrado: #Iteración para realizar el descifrado y operar los bits del mensaje xor los bits aleatorios
        index=textoCifrado.index(C)
        Cc=ord(C) #Función que se encarga de relaizar la operación XOR con dos números entreros
                  #Los transforma a binario y realiza la operación OR, el resultado lo pasa a entero.
        M=op.xor(Cc,clave[index])
        mensajeClaro.append(chr(M))
        mensajeClaroBin.append(bin(M))
    claro="".join(mensajeClaro)
    print("Esta es la cadea de bits del mensaje descifrado:")
    print(mensajeClaroBin)
    return claro



#3. Programar el algoritmo de Luciffer, Cifrar y Descifrar. 10 rondas, sustitución 1 y permutación p=4213. 
#El mensaje será su nombre completo y apellidos. Relleno letra X.
##Importante: Este algoritmo está programado con permutación p=4213
#permutación inversa p-1=3241

def CifradoLucifer(mensaje,pasadas):
    print("El mensaje a cifrar es:")
    print(mensaje)
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    tamano_mensaje=len(mensaje)
    aux=[]
    aux2=[]
    if not tamano_mensaje%8 == 0:
            for j in range(tamano_mensaje*8):
                if tamano_mensaje%8 == 0:
                    break
                else:
                    mensaje.append("X")
                    tamano_mensaje=len(mensaje)
    for i in range(pasadas):
        print("Pasada ",i+1)
        for segmento in range(1,(tamano_mensaje//8)+1):
            indicei=(segmento*8)-8
            indicef=segmento*8
            aux=mensaje[indicei:indicef]
            print("Grupo de 8 caracteres:")
            print(aux)
            for M in range(len(aux)):
                indice=abecedario_claro.index(aux[M])
                if indice==26:
                    aux[M]=abecedario_claro[0]
                else:
                    aux[M]=abecedario_claro[indice+1]

            #Ahora se aplica la permutación
            aux=[aux[3],aux[1],aux[0],aux[2],aux[7],aux[5],aux[4],aux[6]]
            aux2+=aux
            mensaje[indicei:indicef]=aux2
            aux2=[]

            print("Progreso del cifrado...")
            print(mensaje)
    mensaje="".join(mensaje)
    print("El mensaje cifrado con algoritmo Lucifer en ",i+1,"pasada(s) es:")
    return mensaje

def DescifradoLucifer(mensaje,pasadas):
    print("El mensaje a descifrar es:")
    print(mensaje)
    abecedario_claro="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_claro=list(abecedario_claro)
    mensaje=mensaje.upper()
    mensaje=list(mensaje)
    tamano_mensaje=len(mensaje)
    aux=[]
    aux2=[]
    if not tamano_mensaje%8 == 0:
            for j in range(tamano_mensaje*8):
                if tamano_mensaje%8 == 0:
                    break
                else:
                    mensaje.append("X")
                    tamano_mensaje=len(mensaje)
    for i in range(pasadas):
        print("Pasada ",i+1)
        for segmento in range(1,(tamano_mensaje//8)+1):
            indicei=(segmento*8)-8
            indicef=segmento*8
            aux=mensaje[indicei:indicef]
            print("Grupo de 8 caracteres:")
            print(aux)
            for M in range(len(aux)):
                indice=abecedario_claro.index(aux[M])
                if indice==26:
                    aux[M]=abecedario_claro[25]
                else:
                    aux[M]=abecedario_claro[indice-1]

            #Ahora se aplica la permutación
            aux=[aux[2],aux[1],aux[3],aux[0],aux[6],aux[5],aux[7],aux[4]]
            aux2+=aux
            mensaje[indicei:indicef]=aux2
            aux2=[]

            print("Progreso del cifrado...")
            print(mensaje)
    mensaje="".join(mensaje)
	 print("El mensaje descifrado con algoritmo Lucifer en ",i+1,"pasada(s) es:")
	 print(mensaje)
    return mensaje


    ## ********** Ejecución de los algoritmos. Llamado de las funciones para cifrar y descifrar.
#Ejercicio 1. Cifrado por Algoritmo Afin.

mensaje="por mi raza hablara el espiritu"
print("\t\n**** Cifrando lema de la UNAM con algoritmo afin con x=1 y b=7 ***\n")
print("Texto en claro: ",mensaje)
cifrado=AlgoritmoAfin(mensaje,1,7)
print("Texto cifrado: ",cifrado)
claro=DescifrarAlgoritmoAfin(cifrado,1,7)
print("Texto descifrado: ",claro)





#Ejercicio 2. Cifrado por algoritmo Vernam.
mensaje="Fernando Casa Sola"
resultado=CifradoVernam(mensaje) #Se almacena la salida de la función en una tupla
cifrado=resultado[0] #recuoerando el mensaje cifrado
clave=resultado[1] #recuperando la lista de bits aleatorios (clave)
print("\n\t ******* Se va a cifrar la cadena 'Fernando Casa Sola' con algoritmo Vernam. *******")
print("El mensaje cifrado es:",cifrado)
claro=DescifrarVernam(cifrado,clave)
print("\nEl mensaje descifrado es:",claro)






#Ejercicio 3. Cifrado por algoritmo Lucifer.

mensaje="hugoadrianmezavega"
pasadas=2
cifrado=CifradoLucifer(mensaje,pasadas)  
claro=DescifradoLucifer(cifrado,pasadas)


  