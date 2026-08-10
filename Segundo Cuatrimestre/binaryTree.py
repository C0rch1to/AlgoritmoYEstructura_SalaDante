from typing import Any


class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None # Defino un nodo que puede tener un valor y dos hijos, izquierdo y derecho

class BinaryTree():
    def __init__(self):
        self.root = None # Defino un arbol binario que tiene un nodo raiz

    def insert_node(self, value: Any)-> None:
        
        def __insert_node(root, value):
            if root is None:
                print('lugar vacio')
                root = node(value)
                return root
            else:
                if value < root.value:
                    print(f'ir a la izquierda de {root.value}')
                    root.left = __insert_node(root.left, value)
                else:
                    print(f'ir a la derecha de {root.value}')
                    root.right = __insert_node(root.right, value)
                return root
        
        self.root = __insert_node(self.root, value)
    
    def inorden(self):
        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)        #ordena los nodos alfabeticamente
            if root.right is not None:
                __inorden(root.right)
            print(root.value) 
        __inorden(self.root)
    
    def postorden(self):
        def __postorden(root):
            if root.left is not None:
                __postorden(root.left)
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
        __postorden(self.root)

arbol = BinaryTree()

arbol.insert_node('H')
arbol.insert_node('M')
arbol.insert_node('D')
arbol.insert_node('L')

print(arbol.root.value, arbol.root.left.value, arbol.root.right.value)

#print(nodo.value, nodo.left.value, nodo.right.value) # imprime el valor del nodo raiz y sus hijos