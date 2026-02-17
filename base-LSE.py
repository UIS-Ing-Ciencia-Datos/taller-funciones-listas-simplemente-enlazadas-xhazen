# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza

			self.cabeza = nuevo_nodo

	# Agregar al final
	def agregarFinal(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		
        while actual.siguiente is not None:
            actual = actual.siguiente
		
        actual.siguiente = nuevo_nodo
	
    # Contar elementos de la lista
	def contar(self):
		contador = 0
		actual = self.cabeza
		while actual is not None:
			contador = contador+1
			actual = actual.siguiente
        return contador
