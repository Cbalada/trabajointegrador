from controller.auricular_control import controller

from view.menu import menu

def main():
    while True: 
        marca, modelo, color = menu()

        controller(marca, modelo, color)

        respuesta = input("¿va a realizar otro pedido? S/N: ")
        if respuesta.lower() != "s":
            break 

if __name__ == "__main__":
    main()
