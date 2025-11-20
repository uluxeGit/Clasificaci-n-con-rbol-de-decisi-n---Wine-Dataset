# Clasificacion con arbol de decision (Wine-Dataset)
## Clasificador con árbol de decisón usando sklearn en python (wine dataset)

### Opiniones de los resultados.

Complejidad del árbol:
Si max_depth es bajo se muestran pocas divisiones, las reglas son mas fáciles de interpretar, es más simple, si ese parámetro es mas alto, mas de 5, el árbol crece más profundo, y las reglas se vuelven más específicas.

max_depth=None: aunque ponga None o algún otro número, se limita a 5 niveles, comienza con la misma regla pero toma caminos diferentes para llegar al mismo resultado.

Mi base de conocimientos puede llegar a cumplir los requerimientos necesarios para utilizarse como modelo de árbol de desición, pero necesita estar bien estructurada, y reedefinir bien de nuevo las reglas.

## Si gustas probar el codigo:
### 1. Crear un entorno virtual:
```
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```
### 2. Instalar dependencias:
```
pip install scikit-learn matplotlib numpy
```
### 3. Ejecución:
```
python3 practica.py
```

Nota:
*El árbol de decisión generado exporta reglas simbólicas fáciles de interpretar, lo que lo hace ideal para entender el proceso de clasificación y validar que las decisiones del modelo sean lógicas.*

**Autor:** UluxeGit
**Dataset:** Wine Dataset de scikit-learn