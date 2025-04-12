#Asignación 25: Sentencias de repetición en Python (uniformes)

import math 

TALLA_S_TELA = 1.5
TALLA_M_TELA = 3
TALLA_L_TELA = 4.5
TALLA_XL_TELA = 9

HILO_TALLA_S = 100
HILO_TALLA_M = 150
HILO_TALLA_L = 300
HILO_TALLA_XL = 600

CARRETES_H_CAFE = 1000
CARRETES_H_NEGRO = 2500
ROLLO_TELA_NEGRA = 30
ROLLO_TELA_CAFE = 50

PAQUETE_BOTONES = 30 
PAQUETE_CIERRES = 25 

continuar = str(input("¿Desea hacer un pedido? ")).lower()
while continuar == "si":
    color = str(input("¿Que color desea? (1 para cafe)(2 para negro)"))
    if color == "1":
        talla_S = int(input("¿Cuantas faldas talla S desea? "))
        talla_m = int(input("¿Cuantas faldas talla M desea? "))
        talla_l = int(input("¿Cuantas faldas talla L desea? "))
        talla_xl = int(input("¿Cuantas faldas talla XL desea? "))
        total_faldas_cafe = (talla_S + talla_S + talla_l + talla_xl)

        n_tela_s = TALLA_S_TELA / talla_S
        n_tela_m = TALLA_M_TELA / talla_m
        n_tela_l = TALLA_L_TELA / talla_l
        n_tela_xl = TALLA_XL_TELA / talla_xl
        total_tela_cafe = (n_tela_s + n_tela_m + n_tela_l + n_tela_xl)
        
        n_hilo_s = HILO_TALLA_S / talla_S 
        n_hilo_m = HILO_TALLA_M / talla_m
        n_hilo_l = HILO_TALLA_L / talla_l
        n_hilo_xl = HILO_TALLA_XL / talla_xl

        total_hilo_cafe = (n_hilo_s + n_hilo_m + n_hilo_l + n_tela_xl)
        n_rollos_cafe = math.ceil(total_tela_cafe / ROLLO_TELA_CAFE)
        n_carretes_cafe = math.ceil(total_hilo_cafe / CARRETES_H_CAFE)
        n_cajas_botones = math.ceil(total_faldas_cafe / PAQUETE_BOTONES)
        n_cajas_cajas_cierres = math.ceil(total_faldas_cafe / PAQUETE_CIERRES)

        print("El numero de rollos de tela cafe es: ", n_rollos_cafe)
        print("El numero de carretes de hilo cafe es: ", n_carretes_cafe , "El numero de cajas de botones es: ", n_cajas_botones)
        print("El numero de cajas con cierres es: ", n_cajas_cajas_cierres, "y su total de faldas es: ", total_faldas_cafe)
        
        continuar = str(input("¿Desea hacer otro pedido? ")).lower()

    elif color == "2":
        Talla_S = int(input("¿Cuantas faldas talla S desea? "))
        Talla_m = int(input("¿Cuantas faldas talla M desea? "))
        Talla_l = int(input("¿Cuantas faldas talla L desea? "))
        Talla_xl = int(input("¿Cuantas faldas talla XL desea? "))
        Total_faldas_negro = (Talla_S + Talla_S + Talla_l + Talla_xl)

        n_Tela_s = TALLA_S_TELA / Talla_S
        n_Tela_m = TALLA_M_TELA / Talla_m
        n_Tela_l = TALLA_L_TELA / Talla_l
        n_Tela_xl = TALLA_XL_TELA / Talla_xl
        Total_tela_negra = (n_Tela_s + n_Tela_m + n_Tela_l + n_Tela_xl)
        
        N_hilo_s = HILO_TALLA_S / Talla_S 
        N_hilo_m = HILO_TALLA_M / Talla_m
        N_hilo_l = HILO_TALLA_L / Talla_l
        N_hilo_xl = HILO_TALLA_XL / Talla_xl
        total_hilo_negro = (N_hilo_s + N_hilo_m + N_hilo_l + N_hilo_xl)

        n_rollos_negros = math.ceil(Total_tela_negra / ROLLO_TELA_NEGRA)
        n_carretes_negros = math.ceil(total_hilo_negro / CARRETES_H_NEGRO)
        n_cajas_botones = math.ceil(Total_faldas_negro / PAQUETE_BOTONES)
        n_cajas_cajas_cierres = math.ceil(Total_faldas_negro / PAQUETE_CIERRES)

        print("El numero de rollos de tela cafe es: ", n_rollos_negros)
        print("El numero de carretes de hilo cafe es: ", n_carretes_negros , "El numero de cajas de botones es: ", n_cajas_botones)
        print("El numero de cajas con cierres es: ", n_cajas_cajas_cierres, "y su total de faldas es: ", Total_faldas_negro)
        continuar = str(input("¿Desea hacer otro pedido? ")).lower()


    else:
        print("Elija una opcion valida")