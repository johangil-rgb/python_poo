from persona import persona

juan = persona("juan", "castellanos", 15)
juan.mostrarPersona()

leidy= persona("leidy","alvarez", 18)
leidy.mostrarPersona()

leidy.apellido= "perez"
leidy.mostrsrPersona()

juan= leidy
juan.mostrarPersona()