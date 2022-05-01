from os import system
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
        list = []
        with open('./BDD/bankAccount.txt', 'r', encoding='utf-8') as f:
            for line in f:
                list.append(str(line))
        if list == []:
            resultado = False
        else:
            resultado = True
        return resultado

    def createAccount():
        system("cls")
        print("Procederemos a Crear una cuenta en este banco")
        print("Por Favor Ingrese los siguientes datos:")
        print("")
        id = input("Ingrese id: ")
        name = input("Ingrese Nombre: ")
        document = input("Ingrese Numero de documento: ")
        numcuenta = input("Ingrese Numero de Cuenta: ")
        
        account = {"id": id, "name": name, "document": document, "numcuenta": numcuenta}
        with open('./BDD/bankAccount.txt', 'a', encoding='utf-8') as f:
            for idd, data in account.items():
                f.write(idd + ": " + data + " \n")
            f.write("\n")

        system("cls")
        print("Cuenta Creada Exitosamente")
        system("pause")
