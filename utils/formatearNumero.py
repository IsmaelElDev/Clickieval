def formatear_numero(numero):
    if numero < 1000:
        return str(int(numero))  # aseguramos entero
    elif numero < 1_000_000:
        valor = round(numero / 1000, 1)
        return f"{valor}k".replace(".0k", "k")
    elif numero < 1_000_000_000:
        valor = round(numero / 1_000_000, 1)
        return f"{valor}M".replace(".0M", "M")
    else:
        valor = round(numero / 1_000_000_000, 1)
        return f"{valor}B".replace(".0B", "B")