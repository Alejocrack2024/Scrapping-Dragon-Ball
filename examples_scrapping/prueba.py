from DragonBall.Data.Characters import Characters

print("🔎 Buscando a Goku...")
goku = Characters("Goku")
info = goku.character_information()

print("\n--- RESULTADOS ---")
nombre = info.get("name")
print("Nombre:", nombre)
print("URL:", info.get("url_scrap"))


if nombre and "⚠️" in nombre:
    print("\n⚠️ Fandom nos ha bloqueado. ¡Espera o usa datos móviles!")
else:
    print("\n¡Todo funcionó perfecto! Aquí tienes una muestra de los datos:")
    datos = info.get("data", {})
    # La clave correcta para la raza es "species"
    raza = datos.get("species", "Raza no encontrada")
    print("Raza:", raza)
    print("\n📊 Diccionario completo de datos extraídos:")
    print(datos)