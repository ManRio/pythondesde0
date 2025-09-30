mi_texto = "Master"
mi_texto2 = "en Python"

texto_unido = mi_texto + " " + mi_texto2

print(texto_unido)

### Mostrar texto entre comillas
comillas_simples = 'El otro día me dijo: "Ve a comprar pan"'
comillas_dobles = "El otro día me dijo: 'Ve a comprar pan'"
comillas_simples2 = 'El otro día me dijo: \'Ve a comprar pan\''
comillas_dobles2 = "El otro día me dijo: \"Ve a comprar pan\""

print(comillas_simples)
print(comillas_dobles)
print(comillas_simples2)
print(comillas_dobles2)

### Valores especiales

texto_salto = "Master\nen Python"
print(texto_salto)

texto_tab = "Master\ten Python"
print(texto_tab)

texto_borrado = "Master \r en Python" #Esto realmente no borra, es un retorno de carro
print(texto_borrado)