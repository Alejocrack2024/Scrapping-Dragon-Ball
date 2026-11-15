import json
import time
from DragonBall.Data.Characters import Characters

categoria = "Villanos"

print(f"🚀 Iniciando extracción MASIVA de la categoría: '{categoria}'")

resultados = Characters.scrape_group(categoria, limit=10, delay=3)

if isinstance(resultados, list) and resultados and isinstance(resultados[0], str):
    print("⚠️", resultados[0])
else:
    nombre_archivo = f"{categoria}_datos.json"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, ensure_ascii=False, indent=4)
    
    print(f"\n✅ ¡Éxito! Se han guardado {len(resultados)} personajes en el archivo: {nombre_archivo}")
    print("👉 Abre ese archivo en VS Code o en tu navegador para ver TODOS los datos sin cortes.")