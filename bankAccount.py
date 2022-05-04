from os import listdir, system
import random
import sys
from xml.dom.minidom import Document


class bankAccount:
    id = int
    name = str
    document = str
    email = str
    password = str

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def accountExist() -> bool:
        contenido = listdir("./BDD")
        if contenido == []:
            resultado = False
        else:
            resultado = True
        return resultado

    def createAccount():
        system("cls")
        print("Procederemos a Crear una cuenta en este banco")
        print("Por Favor Ingrese los siguientes datos:")
        print("")
        id = bankAccount.generateId()
        name = input("Ingrese Nombre: ")
        document = input("Ingrese Numero de documento: ")
        numcuenta = bankAccount.generateNum()
        money = "0"
        
        account = {"id": id, "name": name, "document": document, "numcuenta": numcuenta, "money": money}
        with open('./BDD/' + str(id) +".txt", 'w', encoding='utf-8') as f:
            for idd, data in account.items():
                f.write(idd + ": " + data + " \n")

        system("cls")
        print("Cuenta Creada Exitosamente")
        system("pause")

    def generateId():
        mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
        minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        caracteres = mayusculas + minusculas + numeros

        contrasena = []

        for i in range(10):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)

        contrasena = ''.join(contrasena) #esto unifica la lista para que no tenga espacios
        return str(contrasena)

    def generateNum():
        numRandom = str(random.randint(100000000, 999999999))
        return numRandom