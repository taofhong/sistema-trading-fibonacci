# backtest.py

import pandas as pd
from estrategias.strategy import ejecutar_estrategia_patron_A
from data_fetcher import obtener_datos_historicos
from config import SYMBOL

def backtest_patron_A(symbol, start_date, end_date):
    """
    Realiza un backtest de la estrategia del patrón "A".
    """
    print("Obteniendo datos históricos...")
    data = obtener_datos_historicos(symbol, start_date, end_date)
    print(f"Datos obtenidos: {len(data)} registros")
    print("Primeras filas de los datos:")
    print(data.head())  # Imprime las primeras filas de los datos
    
    print("Aplicando la estrategia...")
    resultados = []
    for i in range(len(data)):
        subset = data.iloc[:i+1]  # Datos hasta el momento actual
        decision, niveles = ejecutar_estrategia_patron_A(subset)
        resultados.append((data.index[i], decision, niveles))
    
    print("Backtesting completado.")
    resultados_df = pd.DataFrame(resultados, columns=['Fecha', 'Decisión', 'Niveles Fibonacci'])
    return resultados_df

# Ejemplo de uso
if __name__ == "__main__":
    print("Iniciando backtesting...")
    resultados = backtest_patron_A(SYMBOL, start_date="2020-01-01", end_date="2025-02-10")
    print("Resultados del backtesting:")
    print(resultados)