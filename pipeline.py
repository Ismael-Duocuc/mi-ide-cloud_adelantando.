import pandas as pd
import time

from ingestion.lectura_csv import leer_datos_csv
from ingestion.leer_batch import leer_datos_batch
from ingestion.fuente_realtime import leer_clima_tiempo_real

def run_orchestator():

    almacen_datos = {}

    print("--- Lectura de csv")
    almacen_datos['Titanic']=leer_datos_csv()

    print("--- Lectura de titulos libros")
    almacen_datos['Libros']=leer_datos_batch('scifi')

    print("--- Lectura del clima en tiempo real")
    total_lecturas=[]

    for i in range(2):
        df_lectura=leer_clima_tiempo_real()
        if not df_lectura.empty:
            total_lecturas.append(df_lectura)
        time.sleep(2)
    
    if total_lecturas:
        almacen_datos['clima']=pd.concat(total_lecturas,ignore_index=True)

    return almacen_datos

if __name__ == "__main__":
    results=run_orchestator()

