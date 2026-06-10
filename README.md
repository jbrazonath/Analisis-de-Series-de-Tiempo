# Análisis de Series de Tiempo - AirPassengers

Este repositorio contiene un flujo completo de análisis de series de tiempo aplicado al clásico dataset `AirPassengers`. Está estructurado paso a paso para la presentación de los conceptos, desde la descarga de datos hasta el modelado estadístico.

## Estructura del Proyecto

1. **`01_descarga_dataset.ipynb`**: Notebook que descarga el dataset de vuelos y lo guarda localmente de forma reproducible.
2. **`02_eda_basico.ipynb`**: Análisis Exploratorio de Datos (EDA). Incluye revisión de nulos, estructuración del DataFrame para series de tiempo (fechas en el índice) y gráficos de estacionalidad y tendencia usando la descomposición de la serie de tiempo.
3. **`03_modelado_sarima.ipynb`**: 
   - Prueba matemática de estacionariedad (Dickey-Fuller).
   - División de los datos respetando la línea temporal cronológica (Train y Test).
   - Entrenamiento de un modelo estadístico **SARIMA**.
   - Gráfico final comparativo y cálculo de margen de error (RMSE y MAE).

## Instalación y Ejecución

Estos archivos están en formato **Jupyter Notebook (`.ipynb`)**, por lo que son ideales para ejecutarlos en **Google Colab** o localmente con Jupyter.

**Opción A: Google Colab (Recomendado)**
Si este repositorio está en GitHub, simplemente abre los archivos y cambia la URL de `github.com` a `githubtocolab.com`.

**Opción B: Ejecución Local**
1. Clona el repositorio y crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Mac/Linux
   # .venv\Scripts\activate   # En Windows
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install pandas matplotlib seaborn statsmodels scikit-learn jupyter
   ```
3. Inicia Jupyter Notebook y abre los archivos en orden:
   ```bash
   jupyter notebook
   ```
