#Tarea 7 criptografía. Alumno Hugo Meza
#1. Programar el algoritmo de Data Encryption Standard

import random
import numpy as np

def base_key_product(): # Generación de clave aleatoria
    base_key = []
    for i in range(64):
        base_key.append(random.choice([0, 1]))
    return base_key


def round_key_product(base_key): # Generar clave redonda
    pc_1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
    pc_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
    left_turn = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    PC1_key = []
    C_key = []
    D_key = []
    round_key = []
    # Reemplazo de PC-1
    for i in range(len(pc_1)):
        PC1_key.append(base_key[pc_1[i] - 1])
    # Se completa el reemplazo, lo siguiente se divide C0, D0
    C_key.append(PC1_key[0:28])
    D_key.append(PC1_key[28:56])
    # Realiza 16 rondas de desplazamiento circular a la izquierda
    for i in range(16):
        C_key.append(left_turn_f(C_key[i], left_turn[i]))
        D_key.append(left_turn_f(D_key[i], left_turn[i]))
    # Reemplazo de PC-2
    for i in range(16):
        tmp = []
        for j in range(len(pc_2)):
            tmp.append((C_key[i + 1] + D_key[i + 1])[pc_2[j] - 1])
        round_key.append(tmp)
    # over
    return round_key


def left_turn_f(lst, k):  # Mover a la izquierda k
    return lst[k:] + lst[:k]


def IP(plaintxt):  # IP de reemplazo inicial
    ip_list = [58, 50, 42, 34, 26, 18, 10, 2,
               60, 52, 44, 36, 28, 20, 12, 4,
               62, 54, 46, 38, 30, 22, 14, 6,
               64, 56, 48, 40, 32, 24, 16, 8,
               57, 49, 41, 33, 25, 17, 9, 1,
               59, 51, 43, 35, 27, 19, 11, 3,
               61, 53, 45, 37, 29, 21, 13, 5,
               63, 55, 47, 39, 31, 23, 15, 7]
    if (len(plaintxt) != 64):
        print("length of txt is error")
        return
    ip_txt = []
    for i in range(64):
        ip_txt.append(plaintxt[ip_list[i] - 1])
    return ip_txt


def IP_1(txt):
    ip_1_list = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25]
    secret = []
    for i in range(64):
        secret.append(txt[ip_1_list[i] - 1])
    return secret


def change_16(plaint_ip_list, key):
    # 16 iteraciones aquí
    L_txt = []
    R_txt = []
    # L0 R0
    L_txt.append(plaint_ip_list[0:32])
    R_txt.append(plaint_ip_list[32:64])
    # Iteración
    for i in range(16):
        # Li <-- Ri-1
        L_txt.append(R_txt[i])

        # Ri <--Li-1 ^ f()
        L = np.array(L_txt[i])
        f_result = np.array(f(key[i], R_txt[i]))

        R_txt.append((L ^ f_result).tolist())

    return R_txt[16] + L_txt[16]  # En la última ronda, no es necesario intercambiar los paquetes izquierdo y derecho, por lo que el intercambio se restablece nuevamente al estado original.


def f(K, R):
    # Extensión
    E_48 = np.array(E_box(R))
    # print('E-box')
    # print(E_48)
    key = np.array(K)
    # XOR, caja S
    # np.bitwise_xor(R_48,key)
    result = (E_48 ^ key).tolist()
    # print('xor:')
    # print(result)
    S_32 = S_box(result)
    # print('S-32:')
    # print(S_32)
    # P-box
    P_32 = P_box(S_32)
    # print('P-box:')
    # print(P_32)
    return P_32  # return list


def E_box(R):  # list32
    # La función E_Box completa la expansión 32bits -> 48bits
    e_box_list = [32, 1, 2, 3, 4, 5,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]
    e_rusult = []
    for i in range(48):
        e_rusult.append(R[e_box_list[i] - 1])

    return e_rusult  # list48


def S_box(txt):  # txt es una lista de 48 bits de longitud
    s = []
    s_result = []
    s_box_table = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
         ],
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
         3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
         0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
         13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
         ],
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
         13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
         13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
         1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
         ],
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
         13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
         10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
         3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
         ],
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
         14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
         4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
         11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
         ],
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
         10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
         9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
         4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
         ],
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
         13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
         1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
         6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
         ],
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
         1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
         7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
         2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
         ]]
    # Divide el cuadro s
    for i in range(8):
        s.append(txt[6 * i:6 * i + 6])
        # print(s[i])
    # s  
    for i in range(8):
        # Extrae el primero y el último como el valor de y, y el resto como el valor de x, y conviértelo a decimal
        y = int(str(s[i][0]) + str(s[i][5]), 2)
        x = int(''.join(list(map(str, s[i][1:5]))), 2)
        # i representa la i + 1a caja
        # número representa el número en el cuadro
        number = 16 * y + x
        # z representa el número decimal correspondiente
        z = s_box_table[i][number]
        # Convierta a binario, mantenga 4 dígitos y convierta a una lista, los elementos son caracteres
        tmp = list(bin(z)[2:].zfill(4))
        # Convertir elementos de la lista en números
        tmp = list(map(eval, tmp))
        s_result.append(tmp)
    return s_result[0] + s_result[1] + s_result[2] + s_result[3] + s_result[4] + s_result[5] + s_result[6] + s_result[7]


def P_box(S_32):
    p_box_list = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30,
                  6, 22, 11, 4, 25]
    p_result = []
    for i in range(32):
        p_result.append(S_32[p_box_list[i] - 1])
    return p_result


def DES(base_key, txt):
    round_key = round_key_product((base_key))
    return IP_1(change_16(IP(txt), round_key))


def DES_Decrypt(str_secret, str_key):  # str str
    # str to list
    secret = list(map(eval, str_secret))
    base_key = list(map(eval, str_key))
    round_key = round_key_product((base_key))

    return IP_1(change_16_decrypt(IP(secret), round_key))


def change_16_decrypt(plaint_ip_list, key):
    # 16 iteraciones aquí
    L_txt = []
    R_txt = []
    # R16L16
    R_txt.append(plaint_ip_list[0:32])
    L_txt.append(plaint_ip_list[32:64])
    # Iteración
    for i in range(16):
        R_txt.append(L_txt[i])

        R = np.array(R_txt[i])
        f_result = np.array(f(key[15 - i], L_txt[i]))
        L_txt.append((R ^ f_result).tolist())

    return L_txt[16] + R_txt[16]

def convert_plano(txt):
    plano=txt
    plano=plano.upper()
    plano=list(plano)
    bit="0x"
    bit1=bit+"".join(plano[0:2])
    bit2=bit+"".join(plano[2:4])
    bit3=bit+"".join(plano[4:6])
    bit4=bit+"".join(plano[6:8])
    bit5=bit+"".join(plano[8:10])
    bit6=bit+"".join(plano[10:12])
    bit7=bit+"".join(plano[12:14])
    bit8=bit+"".join(plano[14:16])
    bit1=chr(int(bit1,16))
    bit2=chr(int(bit2,16))
    bit3=chr(int(bit3,16))
    bit4=chr(int(bit4,16))
    bit5=chr(int(bit5,16))
    bit6=chr(int(bit6,16))
    bit7=chr(int(bit7,16))
    bit8=chr(int(bit8,16))
    plano=[bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8]
    plano="".join(plano) 
    return plano
def convert_hexa(txt):
    txt=txt.upper()
    txt=list(txt)
    for i in range(len(txt)):
        if txt[i] != " ":
            aux=ord(txt[i])
            txt[i]=hex(aux)[2:]
    txt="".join(txt)
    return txt
    
txt = input("Ingrese palabra de 64 bits: ")  # Hexadecimal
txt=txt.upper()
txt=list(txt)
for i in range(len(txt)):
    if txt[i] != " ":
        aux=ord(txt[i])
        txt[i]=hex(aux)[2:]
    
txt="".join(txt)       
txt = bin(int(txt, 16))[2:]  # Binario
if len(txt) < 64:
    txt = txt.zfill(64)  # Finalización automática de menos de 64 bits
elif len(txt) > 64:
    print("Agrupe primero para asegurarse de que sea menor o igual a 64 bits \ n")
    exit(0)
print('Representación binaria de texto plano')
print(''.join(txt))
txt = list(map(eval, txt))
#base_key = base_key_product()
# base_key = [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0,
#            1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
base_key = input ("Ingrese la clave de 64 bits: ") # hexadecimal
base_key = convert_hexa(base_key)
base_key = (bin (int (base_key, 16))[2:]).zfill(64) # Binario
base_key=list(map(eval,base_key))
# base_key=list(map(eval,base_key))
print('Clave inicial:')
out_base_key = ''.join(str(i) for i in base_key)
print(out_base_key)
print('Resultado de cifrado DES:')
out_DES_result = ''.join(str(i) for i in DES(base_key, txt))
print(out_DES_result)
# Inicie el descifrado a continuación
print('Resultado de descifrado:')
decrypt_result = DES_Decrypt(out_DES_result, out_base_key)
decrypt_result = ''.join(list(map(str, decrypt_result)))
print(decrypt_result)
descifrado=convert_plano(hex(int(decrypt_result, 2))[2:])
#print(hex(int(decrypt_result, 2))[2:])
print("El resultado de descifrar por algoritmo DES es: ")
print(descifrado)