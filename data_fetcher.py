# data_fetcher.py
import yfinance as yf
from config import SYMBOL

def obtener_datos_historicos(symbol, start_date, end_date):
    """
    Obtiene datos históricos de Yahoo Finance.
    """
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def obtener_precio_actual(symbol):
    """
    Obtiene el precio actual de Yahoo Finance.
    """
    ticker = yf.Ticker(symbol)
    precio_actual = ticker.history(period="1d")['Close'].iloc[-1]
    return precio_actual