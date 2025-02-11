# bot.py
from data_fetcher import obtener_datos_historicos
from strategy import ejecutar_estrategia_patron_A
from config import SYMBOL

def main():
    # Obtener datos históricos
    data = obtener_datos_historicos(SYMBOL, start_date="2020-01-01", end_date="2025-02-10")
    
    # Ejecutar la estrategia
    decision, niveles = ejecutar_estrategia_patron_A(data)
    print(f"Decisión de trading: {decision}")
    print(f"Niveles de Fibonacci: {niveles}")

if __name__ == "__main__":
    main()