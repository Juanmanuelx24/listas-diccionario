#Crea una lista llamada nombres que contenga los siguientes elementos: "Juan", "Ana",
#"Luis", "Pedro". Luego, realiza las siguientes tareas
nombres = ["Juan", "Ana", "Luis", "Pedro"]

#Modifica el tercer elemento de la lista para que ahora sea "Carlos".
nombres [2] = "Carlos"
print(*nombres)

#Agrega un nuevo nombre "Lucía" al final de la lista.
nombres.append("Lucia")
print(*nombres)

#Elimina el primer nombre de la lista
nombres.pop(0)
print(*nombres)

#Muestra todos los elementos de la lista en una sola línea sin corchetes ni comas.
elementos = "q".join(nombres)
print(elementos)

#Imprime la cantidad total de nombres en la lista
cantnombres = len(nombres)
print(cantnombres)
