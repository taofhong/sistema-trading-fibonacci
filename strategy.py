# strategy.py
from fibonacci import calcular_fibonacci_retroceso

def detectar_patron_A(data):
    """
    Detecta el patrón "A" en los datos históricos.
    """
    # Identificar máximo y mínimo reciente
    maximo = data['High'].max()  # Techo de la A
    minimo = data['Low'].min()   # Piso de la A
    
    # Calcular niveles de Fibonacci
    niveles_fib = calcular_fibonacci_retroceso(maximo, minimo)
    
    # Precio actual (último precio de cierre)
    precio_actual = data['Close'].iloc[-1]
    
    # Detectar toma de liquidez (precio cae al 127.2%)
    if precio_actual <= niveles_fib['127.2%']:
        return True, niveles_fib
    else:
        return False, niveles_fib

def ejecutar_estrategia_patron_A(data):
    """
    Ejecuta la estrategia basada en el patrón "A".
    """
    # Detectar el patrón "A"
    patron_detectado, niveles_fib = detectar_patron_A(data)
    
    # Precio actual
    precio_actual = data['Close'].iloc[-1]
    
    # Lógica de trading
    if patron_detectado and precio_actual >= niveles_fib['100.0%']:  # Retroceso al piso de la A
        return "Comprar", niveles_fib
    else:
        return "Esperar", niveles_fib