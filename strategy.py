from fibonacci import calcular_fibonacci_retroceso


def detectar_patron_A(data):
    """
    Detecta el patrón "A" en los datos históricos.
    """
    if data.empty:
        print("⚠️ Advertencia: Los datos están vacíos.")
        return False, None

    # Identificar máximo y mínimo reciente
    maximo = data['High'].max()  # Techo de la A
    minimo = data['Low'].min()  # Piso de la A

    # Calcular niveles de Fibonacci
    niveles_fib = calcular_fibonacci_retroceso(maximo, minimo)

    if niveles_fib is None:
        print("⚠️ Advertencia: No se pudieron calcular los niveles de Fibonacci.")
        return False, None

    # Precio actual (último precio de cierre)
    precio_actual = data['Close'].iloc[-1]

    # Diagnóstico
    print(f"Precio actual: {precio_actual} ({type(precio_actual)})")
    print(f"Nivel 127.2%: {niveles_fib['127.2%']} ({type(niveles_fib['127.2%'])})")

    # Asegurar que ambos valores son float
    try:
        precio_actual_valor = float(precio_actual)  # Ya es un escalar, solo lo convertimos
        nivel_fib_valor = float(niveles_fib['127.2%'])  # Convertir a float por seguridad
    except (ValueError, KeyError) as e:
        print(f"⚠️ Error al convertir valores: {e}")
        return False, niveles_fib

    # Detectar toma de liquidez (precio cae al 127.2%)
    if precio_actual_valor <= nivel_fib_valor:
        return True, niveles_fib
    else:
        return False, niveles_fib
