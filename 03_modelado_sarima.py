import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import warnings

# Ignorar warnings menores de statsmodels para tener una consola más limpia
warnings.filterwarnings("ignore")

print("--- 03: PREPARACIÓN Y MODELADO (SARIMA) ---")

# 1. Cargar datos
print("\nCargando datos limpios...")
df = pd.read_csv("AirPassengers.csv")
df.rename(columns={'Month': 'fecha', '#Passengers': 'pasajeros'}, inplace=True)
df['fecha'] = pd.to_datetime(df['fecha'])
df.set_index('fecha', inplace=True)

# 2. Prueba de Estacionariedad (Dickey-Fuller)
print("\n--- PRUEBA DE ESTACIONARIEDAD (Dickey-Fuller) ---")
# Una serie es estacionaria si sus propiedades estadísticas (media, varianza) son constantes en el tiempo.
resultado_adf = adfuller(df['pasajeros'])
print(f"Estadístico ADF: {resultado_adf[0]:.4f}")
print(f"Valor p (p-value): {resultado_adf[1]:.4f}")
if resultado_adf[1] < 0.05:
    print("-> La serie es ESTACIONARIA (podemos modelar directamente).")
else:
    print("-> La serie NO es estacionaria (hay tendencia/estacionalidad). SARIMA se encargará de esto aplicando diferenciación internamente.")

# 3. División en Train y Test (Cronológica)
print("\n--- DIVISIÓN DE DATOS (TRAIN / TEST) ---")
# Dejamos los últimos 2 años (24 meses) para Test y el resto para Train
train = df.iloc[:-24]
test = df.iloc[-24:]

print(f"Datos de Entrenamiento (Train): {len(train)} meses")
print(f"Datos de Prueba (Test): {len(test)} meses")

# 4. Entrenamiento del Modelo SARIMA
print("\n--- ENTRENANDO MODELO SARIMA ---")
# SARIMA necesita dos conjuntos de parámetros:
# order = (p, d, q) -> Componentes No Estacionales (Autoregresivo, Diferenciación, Media Móvil)
# seasonal_order = (P, D, Q, s) -> Componentes Estacionales. "s=12" porque hay ciclos anuales (12 meses).
modelo = SARIMAX(train['pasajeros'], 
                 order=(1, 1, 1), 
                 seasonal_order=(1, 1, 1, 12),
                 enforce_stationarity=False,
                 enforce_invertibility=False)

resultado_modelo = modelo.fit(disp=False)
print("¡Modelo entrenado exitosamente!")
print("\nResumen de los coeficientes del modelo:")
print(resultado_modelo.summary().tables[1])

# 5. Predicciones
print("\n--- REALIZANDO PREDICCIONES ---")
# Le pedimos al modelo que prediga desde el final de Train hasta el final de Test
predicciones = resultado_modelo.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
predicciones.index = test.index

# Calcular Métricas de Error
rmse = np.sqrt(mean_squared_error(test['pasajeros'], predicciones))
mae = mean_absolute_error(test['pasajeros'], predicciones)
print(f"\nError Cuadrático Medio (RMSE): {rmse:.2f}")
print(f"Error Absoluto Medio (MAE): {mae:.2f}")

# 6. Gráfico Final (Real vs Predicción)
print("\n--- GENERANDO GRÁFICO FINAL ---")
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['pasajeros'], label='Entrenamiento (Train)', color='blue')
plt.plot(test.index, test['pasajeros'], label='Prueba Real (Test)', color='green')
plt.plot(predicciones.index, predicciones, label='Predicciones SARIMA', color='red', linestyle='--')

plt.title('Predicción de Pasajeros de Aerolíneas usando SARIMA')
plt.xlabel('Fecha')
plt.ylabel('Cantidad de Pasajeros')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
