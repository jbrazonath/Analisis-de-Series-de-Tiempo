# Integrantes 
Josmar Brazón

Carla Sabrina Espínola Hamm

Sabrina Daiana Pryszczuk


# Análisis de Series de Tiempo - AirPassengers

Este repositorio contiene un flujo completo de análisis de series de tiempo aplicado al clásico dataset `AirPassengers`. Está estructurado paso a paso para la presentación de los conceptos, desde la descarga de datos hasta el modelado estadístico.

## Estructura del Proyecto

- **`Proyecto_Series_Tiempo.ipynb`**: Un único notebook maestro que agrupa de forma lineal (para correr de arriba a abajo) los siguientes pasos:
  1. **Descarga de datos**: Obtención del dataset clásico de vuelos.
  2. **Análisis Exploratorio de Datos (EDA)**: Revisión de nulos, formateo del índice de tiempo y gráficos de estacionalidad y tendencia.
  3. **Preparación y Modelado (SARIMA)**: Prueba matemática de estacionariedad (Dickey-Fuller), división de datos respetando la línea temporal cronológica (Train/Test) y entrenamiento del modelo estadístico **SARIMA**. Gráfico final comparativo y cálculo de margen de error (RMSE y MAE).

## Instalación y Ejecución

El proyecto está en formato **Jupyter Notebook (`.ipynb`)**, por lo que es ideal para ejecutarlo en **Google Colab** o localmente con Jupyter.

**Opción A: Google Colab (Recomendado)**
Si este repositorio está en GitHub, simplemente abre el archivo `Proyecto_Series_Tiempo.ipynb` y cambia la URL de `github.com` a `githubtocolab.com`.

**Opción B: Ejecución Local**
1. Clona el repositorio y crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Mac/Linux
   # .venv\Scripts\activate   # En Windows
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install pandas numpy matplotlib seaborn statsmodels scikit-learn pmdarima kagglehub jupyter
   ```
3. Inicia Jupyter Notebook y abre el proyecto:
   ```bash
   jupyter notebook
   ```
