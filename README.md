# mi-ide-cloud
Test Gestión datos IA
# Pipeline de Datos 

## Descripción
Pipeline automatizado de ingesta, limpieza y transformación de datos usando Python y pandas.

## Estructura del proyecto
ingestion/          → módulos de lectura de datos
lectura_csv.py    → lee Titanic.csv
leer_batch.py     → descarga libros desde Open Library API
fuente_realtime.py → obtiene clima de Santiago en tiempo real
procesamiento/      → módulos de transformación
transformacion.py → aplica las 4 transformaciones sobre almacen_datos
pipeline.py         → orquestador principal

## Cómo ejecutar
```bash
pip install -r requirements.txt
python pipeline.py
```

## Transformaciones aplicadas

### 1. Resumen de supervivencia - Titanic
Conteo de pasajeros que sobrevivieron (1) y no sobrevivieron (0).
Resultado almacenado en almacen_datos['resumen_supervivencia'].

### 2. UniqueKey - Librería
Se creó una columna UniqueKey en el dataset de libros extrayendo
el identificador único desde la columna 'key' de Open Library.
Entrada Libros actualizada en almacen_datos.

### 3. Promedio de temperatura - Clima
Se calculó el promedio de temperatura de Santiago de Chile
a partir de lecturas en tiempo real desde la API open-meteo.
Resultado almacenado en almacen_datos['resumen_clima'].

### 4. Filtro de edad - Titanic
Se eliminaron todos los pasajeros menores de 10 años del dataset Titanic.
Dataset limpio guardado en data/processed/titanic_limpio.csv.

## Tecnologías
- Python 3.11
- pandas
- requests
- GitHub Codespaces
EOF