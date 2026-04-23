class Persona:

    # Método constructor
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Método para mostrar la información
    def mostrarPersona(self):
        print("\n--- Datos de la Persona ---")
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Edad:", self.edad)


def main():
    personas = []

    while True:
        print("\n=== MENÚ ===")
        print("1. Agregar persona")
        print("2. Mostrar personas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            apellidos = input("Ingrese apellidos: ")
            
            try:
                edad = int(input("Ingrese edad: "))
            except:
                print("Edad inválida")
                continue

            nueva_persona = Persona(nombre, apellidos, edad)
            personas.append(nueva_persona)
            print("Persona agregada correctamente")

        elif opcion == "2":
            if len(personas) == 0:
                print("No hay personas registradas")
            else:
                for p in personas:
                    p.mostrarPersona()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()