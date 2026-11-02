from pathlib import Path

# Si es True, todo el flujo corre con un solo año (para probar rápido)
MODO_MUESTRA = True

# Rutas relativas a la raíz del repositorio
CRUDO = Path("datos/crudo")
GEO = Path("datos/geo")
PROCESADO = Path("datos/procesado")

# Años a analizar
ANIOS = list(range(2019, 2027))
if MODO_MUESTRA:
    ANIOS = [2024]