import pandas as pd

print("--- INICIANDO EDA: AIR PASSENGERS ---")

# 1. Cargar el dataset
try:
    df = pd.read_csv("AirPassengers.csv")
    print("\nDataset cargado exitosamente.")
except FileNotFoundError:
    print("Error: No se encontró 'AirPassengers.csv'. Asegúrate de haber ejecutado el script 01.")
    exit()

# 2. Vistazo general
print("\n--- PRIMERAS 5 FILAS ---")
print(df.head())

print("\n--- INFORMACIÓN GENERAL ---")
df.info()

# 3. Revisión de Nulos y Duplicados
print("\n--- REVISIÓN DE NULOS ---")
nulos = df.isnull().sum()
print(nulos)

if nulos.sum() == 0:
    print("-> ¡Excelente! El dataset está limpio, no hay valores nulos.")
else:
    print("-> ¡Atención! Se encontraron valores nulos.")

print("\n--- REVISIÓN DE DUPLICADOS ---")
duplicados = df.duplicated().sum()
print(f"Filas duplicadas encontradas: {duplicados}")

# 4. Preparación clave para Series de Tiempo
print("\n--- TRANSFORMACIÓN DE FECHAS ---")

# Renombramos las columnas para que no tengan caracteres raros como '#'
df.rename(columns={'Month': 'fecha', '#Passengers': 'pasajeros'}, inplace=True)

# Convertimos el texto (ej: '1949-01') a un formato de tiempo matemático
df['fecha'] = pd.to_datetime(df['fecha'])

# En Series de Tiempo, la fecha SIEMPRE debe ser el índice del DataFrame
df.set_index('fecha', inplace=True)

print("\n--- ESTRUCTURA FINAL (LISTA PARA MODELOS) ---")
print(df.head())
print(f"\nTipo de índice actual: {type(df.index)}")

import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

print("\n--- EDA ESPECÍFICO PARA SERIES DE TIEMPO ---")

# 1. Gráfico principal (Para ver Tendencia a ojo)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['pasajeros'], color='blue')
plt.title('Evolución de Pasajeros de Aerolíneas (1949-1960)')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Pasajeros')
plt.grid(True, alpha=0.3)
plt.show()

# 2. Análisis de "Outliers" Estacionales (Boxplot por Mes)
# Queremos ver si los meses de verano siempre tienen picos o si hubo un verano atípico.
df['mes'] = df.index.month
plt.figure(figsize=(10, 5))
sns.boxplot(x='mes', y='pasajeros', data=df, palette='viridis')
plt.title('Distribución de pasajeros por mes (Patrón Estacional)')
plt.xlabel('Mes del año')
plt.ylabel('Pasajeros')
plt.show()

# 3. Descomposición de la Serie de Tiempo
# Magia matemática: separa la gráfica en Tendencia, Estacionalidad y Residuos (Ruido)
print("\nGenerando gráfica de descomposición. Cierra la ventana del gráfico anterior para ver esta.")
descomposicion = seasonal_decompose(df['pasajeros'], model='multiplicative')

fig = descomposicion.plot()
fig.set_size_inches(10, 8)
plt.show()

# Limpiamos la columna extra que creamos solo para graficar
df.drop(columns=['mes'], inplace=True)
