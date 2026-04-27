import pandas as pd

def transformar(almacen_datos):

    # --- 1. Tabla resumen sobrevivientes Titanic ---
    df_titanic = almacen_datos['Titanic']
    resumen_supervivencia = df_titanic['2urvived'].value_counts().rename({0: 'No sobrevivió', 1: 'Sobrevivió'})
    almacen_datos['resumen_supervivencia'] = resumen_supervivencia
    print("\n📊 Resumen supervivencia Titanic:")
    print(resumen_supervivencia.to_string())

    # --- 2. Crear columna UniqueKey en Librería ---
    df_libros = almacen_datos['Libros']
    df_libros['UniqueKey'] = df_libros['key'].str.replace('/works/', '', regex=False)
    almacen_datos['Libros'] = df_libros
    print("\n📚 Columna UniqueKey agregada a Libros:")
    print(df_libros[['title', 'UniqueKey']].to_string(index=False))

    # --- 3. Promedio de temperatura Clima ---
    df_clima = almacen_datos['clima']
    promedio_temp = df_clima['temperature'].mean()
    almacen_datos['resumen_clima'] = pd.DataFrame([{'promedio_temperatura': round(promedio_temp, 2)}])
    print(f"\n🌡️  Promedio de temperatura en Santiago: {promedio_temp:.2f} °C")

    # --- 4. Eliminar pasajeros menores de 10 años en Titanic ---
    antes = len(df_titanic)
    df_titanic = df_titanic[df_titanic['Age'] >= 10]
    almacen_datos['Titanic'] = df_titanic
    despues = len(df_titanic)
    print(f"\n🗑️  Pasajeros menores de 10 años eliminados: {antes - despues} filas removidas")
    print(f"   Pasajeros restantes: {despues}")

    # --- Guardar dataset limpio ---
    import os
    os.makedirs("data/processed", exist_ok=True)
    df_titanic.to_csv("data/processed/titanic_limpio.csv", index=False)
    print("\n💾 Dataset limpio guardado en data/processed/titanic_limpio.csv")

    return almacen_datos
