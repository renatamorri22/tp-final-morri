# Socios comerciales de Argentina: ¿quién ganó peso en las importaciones con el cambio de régimen frente al mercado externo?

**Autora:** Renata Morri · **Curso:** Herramientas computacionales para Economistas, UNLP · **Fecha:** noviembre de 2026

## Pregunta
¿Qué socios comerciales ganaron (o perdieron) participación en las importaciones argentinas desde 2024, en comparación con 2019–2023?

- **Unidad de análisis:** país socio (país de origen de las importaciones) por año.
- **Período:** 2019–2025.
- **Por qué importa:** desde 2024 cambió la política hacia el comercio exterior, con menos restricciones a las importaciones. Ver qué socios ganaron o perdieron peso ayuda a entender a qué mercados se abrió la economía argentina. Es un punto de partida para lo que me gustaría investigar en mi tesis, sobre todo el efecto en mercados más específicos.

## Fuentes
| Fuente | Quién la produce | URL | Fecha de descarga | Licencia o condiciones | Cómo se obtiene |
| --- | --- | --- | --- | --- | --- |
| Bases anuales de importaciones 2019–2025 | INDEC | `https://comex.indec.gob.ar/files/zips/imports_{año}_Y.zip` | 04/11/2026 | Datos públicos del INDEC; se cita la fuente | Descarga con `requests` (`01_obtencion.ipynb`) |
| Nomenclador de países | INDEC | https://comex.indec.gob.ar/#/ (pestaña Nomencladores) | [completar] | Datos públicos del INDEC; se cita la fuente | Descarga manual: el sitio genera el archivo en el navegador y no ofrece un link directo |
| Mapa de países del mundo (escala 1:110m) | Natural Earth | https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson | 04/11/2026 | Dominio público | Descarga con `requests` (`01_obtencion.ipynb`) |

**Qué contiene cada fuente:**
- **Bases de importaciones:** un zip por año con el valor importado por producto (NCM a 8 dígitos) y país de origen, en kilos y en dólares (FOB, flete, seguro y CIF). Incluye un archivo de control (`itota`) con la cantidad de registros y los totales, y un `Leame` con la descripción de las columnas.
- **Nomenclador de países:** el código de país del INDEC, el código ISO de dos letras y el nombre.
- **Mapa:** la geometría de cada país, con sus códigos ISO.

## Cómo ejecutar
1. Crear el entorno: `python -m venv .venv` e instalar con `pip install -r requirements.txt`.
2. No hace falta clave de API.
3. En `config.py`, dejar `MODO_MUESTRA = True` para una corrida rápida con un solo año (unos [N] minutos) o `False` para todo el período (unos [N] minutos).
4. Ejecutar en orden: `01_obtencion.ipynb`, `02_limpieza.ipynb`, `03_analisis.ipynb`.

## Estructura
- `config.py`: rutas, años a analizar y `MODO_MUESTRA`.
- `01_obtencion.ipynb`: descarga las bases del INDEC y el mapa, y descomprime los zips.
- `02_limpieza.ipynb`: lectura, verificación contra los totales del INDEC, expresiones regulares y unión con el nomenclador y el mapa.
- `03_analisis.ipynb`: gráficos, mapas y conclusiones.
- `datos/crudo/`: lo descargado tal cual (zips del INDEC y nomenclador). Las carpetas descomprimidas no se suben: se regeneran con `01_obtencion.ipynb`.
- `datos/geo/`: el mapa de países.
- `datos/procesado/`: las bases finales.
- `figuras/`: gráficos y mapas guardados.

## Principales resultados
[Completar al final.]

## Qué verifiqué y qué no
[Completar al final. Por ahora: la cantidad de filas y el total CIF de cada año coinciden con los archivos de control del INDEC; los nombres de columnas cambian entre 2021 (u$s) y 2022 (USD) y se unificaron con código; no hay filas repetidas por año, producto y país; no hay montos negativos; todos los códigos de país de la base están en el nomenclador.]

## Bitácora de uso de IA
| Herramienta | Para qué | Qué pedí | Qué hice con la respuesta |
| --- | --- | --- | --- |
| [completar] | | | |

**Un caso en que la IA se equivocó:** [completar].
