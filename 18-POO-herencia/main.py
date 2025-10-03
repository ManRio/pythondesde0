import clases

persona = clases.Persona()

persona.setNombre("Manuel")
persona.setApellidos("Rios")
persona.setAltura("180cm")
persona.setEdad("38 Años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")

print(persona.hablar())
print("\n")

informatico = clases.Informatico()
informatico.setNombre("Paco")
informatico.setApellidos("Pérez")
informatico.setAltura("160cm")

print(f"El informatico se llama {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.programar())
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("\n")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())
