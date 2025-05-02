import sqlite3
import pandas as pd
from pandas.io import sql

def main():
    # Configuración inicial
    input_file = 'Book2.csv'
    output_file = 'resultados_consolidados.csv'
    temp_db = ':memory:'  # Usamos base de datos en memoria

    # Leer el archivo CSV y cargarlo a SQLite
    df = pd.read_csv(input_file)
    
    # Conectar a la base de datos temporal
    conn = sqlite3.connect(temp_db)
    df.to_sql('Book2', conn, index=False, if_exists='replace')

    # Lista para almacenar todos los resultados
    resultados_completos = []

    # Generar y ejecutar consultas para field3 a field210
    for field_num in range(3, 211):
        field_name = f'field{field_num}'
        
        # Construir la consulta SQL
        query = f"""
        SELECT field1, field2, {field_name}
        FROM Book2
        WHERE {field_name} IN ('Y', 'N', 'NA')
        """
        
        # Ejecutar consulta y obtener resultados
        df_resultado = pd.read_sql_query(query, conn)
        
        # Agregar columna para identificar el campo consultado
        df_resultado['campo_consultado'] = field_name
        
        # Agregar a los resultados consolidados
        resultados_completos.append(df_resultado)

    # Cerrar conexión a la base de datos
    conn.close()

    # Combinar todos los resultados
    df_final = pd.concat(resultados_completos, ignore_index=True)

    # Guardar resultados en un nuevo CSV
    df_final.to_csv(output_file, index=False)
    print(f"Resultados guardados en {output_file}")

if __name__ == '__main__':
    main()