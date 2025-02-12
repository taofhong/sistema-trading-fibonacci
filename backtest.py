import pandas as pd
from strategy import detectar_patron_A  # ✅ Importa la función correcta
from data_fetcher import obtener_datos_historicos
from config import SYMBOL, START_DATE, END_DATE

def backtest_patron_A(symbol, start_date, end_date):
    """Realiza un backtest de la estrategia del patrón 'A'."""

    print("Obteniendo datos históricos...")
    data = obtener_datos_historicos(symbol, start_date, end_date)

    if data is None or data.empty:  # ✅ También verificamos si está vacío
        print("❌ Error: No se pudieron obtener los datos. El backtest no puede continuar.")
        return None

    print(f"Datos obtenidos: {len(data)} registros")
    
    print("Aplicando la estrategia...")
    resultados = []
    for i in range(len(data)):
        subset = data.iloc[:i+1]  # Datos hasta el momento actual
        decision, niveles = detectar_patron_A(subset)  # ✅ Usa la función correcta
        resultados.append((data.index[i], decision, niveles))

    print("Backtesting completado.")
    resultados_df = pd.DataFrame(resultados, columns=['Fecha', 'Decisión', 'Niveles Fibonacci'])
    return resultados_df

# Ejemplo de uso (con las fechas definidas en config.py)
if __name__ == "__main__":
    print("Iniciando backtesting...")
    resultados = backtest_patron_A(SYMBOL, START_DATE, END_DATE)  # Usa las fechas de config.py
    if resultados is not None:
        print("Resultados del backtesting:")
        print(resultados)
