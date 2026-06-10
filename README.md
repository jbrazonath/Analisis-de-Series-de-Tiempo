# Análisis de Series de Tiempo - AirPassengers

Este repositorio contiene un flujo completo de análisis de series de tiempo aplicado al clásico dataset `AirPassengers`. Está estructurado paso a paso para la presentación de los conceptos, desde la descarga de datos hasta el modelado estadístico.

## Estructura del Proyecto

1. **`01_descarga_dataset.py`**: Script que descarga el dataset de vuelos y lo guarda localmente de forma reproducible.
2. **`02_eda_basico.py`**: Análisis Exploratorio de Datos (EDA). Incluye revisión de nulos, estructuración del DataFrame para series de tiempo (fechas en el índice) y gráficos de estacionalidad y tendencia usando la descomposición de la serie de tiempo.
3. **`03_modelado_sarima.py`**: 
   - Prueba matemática de estacionariedad (Dickey-Fuller).
   - División de los datos respetando la línea temporal cronológica (Train y Test).
   - Entrenamiento de un modelo estadístico **SARIMA**.
   - Gráfico final comparativo y cálculo de margen de error (RMSE y MAE).

## Instalación y Ejecución

Para replicar este proyecto localmente, tus compañeras deben seguir estos pasos:

1. Clonar el repositorio y entrar en la carpeta.
2. Crear un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Mac/Linux
   # .venv\Scripts\activate   # En Windows
   ```
3. Instalar las dependencias necesarias:
   ```bash
   pip install pandas matplotlib seaborn statsmodels scikit-learn
   ```
4. Ejecutar los scripts en orden:
   ```bash
   python 01_descarga_dataset.py
   python 02_eda_basico.py
   python 03_modelado_sarima.py
   ```
