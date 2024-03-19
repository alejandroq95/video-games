from random import randint
import os
import time
import random

#Functions
def loading_dots(duration, interval):
    start_time = time.time()
    print("Loading Number Race")
    while time.time() - start_time < duration:
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(interval)

def main_menu():
    menu_status = True
    opt_status = True
    jugadores = []
    niveles = {
    "1": 20,
    "2": 30,
    "3": 50,
    "4": 100,
    }
    posiciones = {}
    tiradas_consecutivas = {}
    def tirar_dado1():
        return random.randint(1, 6)
    
    def validar_jugadores(numero_jugadores):
        while not 2 <= numero_jugadores <= 4:
            numero_jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))
        return numero_jugadores
    
    def seleccionar_nivel():
        
        while True:
            nivel = input("Seleccione el nivel de tablero (1-4): ")
        if nivel in niveles:
            return nivel
        print("Opción no válida. Ingrese un valor entre 1 y 4.")
    nivel =0
    def mover_ficha(jugador, tirada):
        posiciones[jugador] += tirada
        if posiciones[jugador] >= niveles[nivel]:
            print(f"¡Felicidades! {jugador} ha ganado la carrera.")
        return True
    return False

    def jugar_turno():
        for jugador in jugadores:
         print(f"Turno de {jugador}:")
        tirada1 = tirar_dado()
        tirada2 = tirar_dado()
        print(f"Tirada 1: {tirada1}")
        print(f"Tirada 2: {tirada2}")
        
        # Validación de tres pares consecutivos
        if tirada1 == tirada2:
            tiradas_consecutivas[jugador] += 1
            if tiradas_consecutivas[jugador] == 3:
                print(f"{jugador} ha ganado la carrera por obtener tres pares consecutivos.")
                return True
        else:
            tiradas_consecutivas[jugador] = 0
        
        movimiento = tirada1 + tirada2
        print(f"Movimiento: {movimiento}")
        
        if mover_ficha(jugador, movimiento):
            return True
    return False
    def iniciar_juego():
    # Obtener la cantidad de jugadores
        numero_jugadores = validar_jugadores(int(input("Ingrese la cantidad de jugadores (2-4): ")))
    
    # Obtener el nivel de tablero
        nivel = seleccionar_nivel()
    
    # Inicializar las variables
        for i in range(numero_jugadores):
            jugadores.append(f"Jugador {i + 1}")
            posiciones[f"Jugador {i + 1}"] = 0
            tiradas_consecutivas[f"Jugador {i + 1}"] = 0
    
    # Bucle del juego
    while True:
        if jugar_turno():
            break
    while menu_status:
       
        os.system('clear')
        print(":::::::::::::::::")
        print("::: MAIN MENU :::")
        print(":::::::::::::::::")
        print("[1]. Play")
        print("[2]. Help")
        print("[3]. About us")
        print("[4]. Exit")
        
        while opt_status:
            opt = int(input(".::: Press any option: "))
            if opt < 1 or opt > 4:
                print("::: Invalid option, try again :::")
            else:
                opt_status = False


        if opt == 4:
            break
        if opt == 1:
            iniciar_juego()

#Main
os.system('clear')
loading_dots(5, 0.5)
main_menu()
