import json
import time
from DragonBall.Data.Characters import Characters

grupos = ["Guerreros Z", "Villanos", "Androides", "Dioses", "Saiyans", "Namekianos"]

todos_los_personajes = set() 

print("🔎 Fase 1: Buscando los nombres de todos los grupos...")
for grupo in grupos:
    print(f"   -> Leyendo el grupo: {grupo}...")
    nombres = Characters.get_characters_by_category(grupo)
    
    if isinstance(nombres, list) and nombres and isinstance(nombres[0], str) and "⚠️" in nombres[0]:
        print(f"      ⚠️ Saltando '{grupo}': {nombres[0]}")
    else:
        todos_los_personajes.update(nombres)

lista_final = list(todos_los_personajes)
print(f"\n✅ ¡Se encontraron {len(lista_final)} personajes únicos en total!")

print("\n⚠️ ATENCIÓN: Descargar TODOS puede tardar más de 1 hora y Fandom podría bloquearnos.")
cantidad = int(input("👉 ¿Cuántos personajes quieres descargar ahora? (Escribe un número, ej. 10 o 50): "))

personajes_a_buscar = lista_final[:cantidad]
resultados = []

print(f"\n🚀 Fase 2: Descargando información de {len(personajes_a_buscar)} personajes...")
for i, nombre in enumerate(personajes_a_buscar):
    print(f"[{i+1}/{len(personajes_a_buscar)}] Scrapeando: {nombre}...")
    
    info = Characters(nombre, all_data=True).character_information()
    resultados.append(info)
    
    time.sleep(3)

nombre_archivo = "DragonBall_Datos_Completos.json"
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    json.dump(resultados, archivo, ensure_ascii=False, indent=4)

print(f"\n🎉 ¡TERMINADO! Se ha creado el archivo '{nombre_archivo}' con toda la información.")