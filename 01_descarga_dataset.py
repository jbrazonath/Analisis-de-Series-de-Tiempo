import kagglehub
import shutil
import os

print("Iniciando la descarga del dataset 'Air Passengers'...")

# 1. Descargar la última versión desde Kaggle (se descarga en una carpeta caché del sistema)
path_cache = kagglehub.dataset_download("chirag19/air-passengers")

print(f"Dataset descargado en caché: {path_cache}")

# 2. Encontrar el archivo CSV dentro de esa carpeta
archivo_csv = "AirPassengers.csv" # Nombre clásico de este archivo en Kaggle
ruta_origen = os.path.join(path_cache, archivo_csv)

# 3. Moverlo a nuestra carpeta de trabajo actual
ruta_destino = os.path.join(os.getcwd(), archivo_csv)

if os.path.exists(ruta_origen):
    shutil.copy(ruta_origen, ruta_destino)
    print(f"\n¡Éxito! El archivo se ha copiado a tu carpeta actual:")
    print(f"-> {ruta_destino}")
else:
    print(f"\nNo se encontró el archivo {archivo_csv} en la ruta descargada.")
    print("Revisa la carpeta caché manualmente.")
