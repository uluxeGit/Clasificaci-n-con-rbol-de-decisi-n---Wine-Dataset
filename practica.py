#   INSTRUCCIONES PASO A PASO   #

# IMPORTAR LIBRERIAS NECESARIAS
from sklearn.datasets import load_wine
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# CARGAR EL DATASET DEL VINO
wine = load_wine()
# x son las caracteristicas químicas
x = wine.data
# y es la clase del vino (0,1,2 corresponden a los tipos de vino)
y = wine.target

# DIVIDIR LOS DATOS DE ENTRENAMIENTO Y PRUEBA (80% de los datos se usan para entrenar y 20% son para precisión)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=77)

# CREAR Y ENTRENAR EL CLASIFICADOR max_depth = 2
desicion_tree = DecisionTreeClassifier(max_depth=5)
desicion_tree = desicion_tree.fit(x_train, y_train) # usar solo los datos de train !!!!

# EXPORTAR Y VISUALIZAR LAS REGLAS SIMBÓLICAS
rules = export_text(desicion_tree, feature_names=wine['feature_names'])
print(rules)
print("Presicion de datos de prueba: ", desicion_tree.score(x_test, y_test))

plt.figure(figsize=(10, 10))  # ancho, alto en pulgadas
tree.plot_tree(desicion_tree, feature_names=wine.feature_names, class_names=wine.target_names, filled=True)
plt.show()