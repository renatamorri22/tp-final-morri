from pathlib import Path

# Si es True, todo el flujo corre con un solo año (para probar rápido)
MODO_MUESTRA = False

# Rutas relativas a la raíz del repositorio
CRUDO = Path("datos/crudo")
GEO = Path("datos/geo")
PROCESADO = Path("datos/procesado")

# Años a analizar
ANIOS = list(range(2019, 2026))
if MODO_MUESTRA:
    ANIOS = [2024]