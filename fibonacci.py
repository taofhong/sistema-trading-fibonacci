# fibonacci.py

def calcular_fibonacci_retroceso(maximo, minimo):
    """
    Calcula los niveles de retroceso de Fibonacci.
    """
    diferencia = maximo - minimo
    niveles = {
        '23.6%': maximo - diferencia * 0.236,
        '38.2%': maximo - diferencia * 0.382,
        '50.0%': maximo - diferencia * 0.500,
        '61.8%': maximo - diferencia * 0.618,
        '78.6%': maximo - diferencia * 0.786,
        '127.2%': maximo - diferencia * 1.272,  # Extensión para la toma de liquidez
    }
    return niveles