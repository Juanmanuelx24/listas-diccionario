contactos = {
    "Juan Manuel" : {
        "Telefono" : ["3233430819", 3235553720],
        "Correo" : ["juanmanuelx242@gmail.com","juanma42@gmail.com","manuelsanchez@gmail.com"], 
        "Direccion" : {
            "Calle" : "28#32B15",
            "Barrio" : "San Carlos",
            "Ciudad" : "Cali"

        }

    },
    "Sofia Alava": {
        "Telefono" : ["3332412345", "32234443123"],
        "Estado Civil" : "Casada",
        "Datos": {
        "Edad" : 18,
        "Año de nacimiento" : 2006,
        "Ciudad" :  "Cali"
        }
        
    },
        "Camilo": {
            "Telefono" : ["35133343410", 3303322421],
            "Correo" : ["camilo24@gmail.com","cami24@gmail.com"],
            "Ciudad" : "Cali"
}

}


print("El telefono de Sofia es: ",contactos["Sofia Alava"]["Telefono"])

print("El segundo telefono de Sofia es: ",*contactos["Sofia Alava"]["Telefono"][1])

print("La ciudad de Sofia es: ",*contactos["Sofia Alava"]["Datos"]["Ciudad"])

print("El estado civil de Sofia es: ",*contactos["Sofia Alava"]["Estado Civil"]) 


ciudadSofia = contactos["Sofia Alava"]["Datos"]["Ciudad"]
print("La ciudad de Sofia es: ",ciudadSofia)

telefonoSofia = contactos["Sofia Alava"]["Telefono"]
print(telefonoSofia)

for telefono in telefonoSofia:
    print(telefono)
for i, telefono in enumerate(telefonoSofia, start= 1):
    print(f"Telefono {i}", telefono)


correoCamilo = contactos["Camilo"]["Correo"]
print("El correo de Camilo es: ",*correoCamilo)

for i, correo in enumerate(correoCamilo, start = 1):
    print(f"Correo {i}", *correoCamilo)

contactos["Camilo"]["Cumpleaños"]= "10 de Octubre"
print("EL cumpleaños de Camilo es:  ",*contactos["Camilo"]["Cumpleaños"])

contactos["Camilo"]["Fecha de nacimiento"]=[10, "Octubre", 2004]
print("la fecha de nacimiento es: ",*contactos["Camilo"]["Fecha de nacimiento"])

anioNacimiento=contactos["Camilo"]["Fecha de nacimiento"][2];
print(anioNacimiento); 
anioActual = 2024 - anioNacimiento;
if anioActual  >= 18:
    print(f"Camilo es mayor de edad",anioNacimiento)
else:
    print(f"Camilo es menor de edad")

del contactos["Juan Manuel"]["Telefono"][0]
print(*contactos["Juan Manuel"]["Telefono"])

contactos["Juan Manuel"]["Correo"].remove("juanmanuelx242@gmail.com")
print(*contactos["Juan Manuel"]["Correo"])




