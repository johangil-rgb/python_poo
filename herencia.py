# =========================
# Clase Persona
# =========================

class Persona:

    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    # getters y setters
    def getNombre(self):
        return self.__Nombre

    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos

    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad

    def setEdad(self, edad):
        self.__Edad = edad

    # mostrar datos
    def mostrarPersona(self):
        print("Nombre:", self.__Nombre)
        print("Apellidos:", self.__Apellidos)
        print("Edad:", self.__Edad)


# =========================
# Clase Alumno
# =========================

class Alumno(Persona):

    def __init__(self):
        super().__init__()   # hereda constructor de Persona
        self.__Curso = ""
        self.__Asignaturas = []

    def getCurso(self):
        return self.__Curso

    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas

    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("\n===== DATOS DEL ALUMNO =====")
        print("Nombre:", self.getNombre())
        print("Apellidos:", self.getApellidos())
        print("Edad:", self.getEdad())
        print("Curso:", self.__Curso)
        print("Asignaturas:", ", ".join(self.__Asignaturas))


# =========================
# Clase Profesor
# =========================

class Profesor(Persona):

    def __init__(self):
        super().__init__()
        self.__Especialidad = ""
        self.__Salario = 0

    def getEspecialidad(self):
        return self.__Especialidad

    def setEspecialidad(self, especialidad):
        self.__Especialidad = especialidad

    def getSalario(self):
        return self.__Salario

    def setSalario(self, salario):
        self.__Salario = salario

    def mostrarProfesor(self):
        print("\n===== DATOS DEL PROFESOR =====")
        print("Nombre:", self.getNombre())
        print("Apellidos:", self.getApellidos())
        print("Edad:", self.getEdad())
        print("Especialidad:", self.__Especialidad)
        print("Salario:", self.__Salario)


# =========================
# Método principal
# =========================

def main():

    # crear alumno
    alumno = Alumno()
    alumno.setNombre("Néstor")
    alumno.setApellidos("Páez Sarmiento")
    alumno.setEdad(25)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    # crear profesor
    profesor = Profesor()
    profesor.setNombre("Carlos")
    profesor.setApellidos("Ramírez López")
    profesor.setEdad(40)
    profesor.setEspecialidad("Programación")
    profesor.setSalario(3500)
    profesor.mostrarProfesor()


if __name__ == "__main__":
    main()