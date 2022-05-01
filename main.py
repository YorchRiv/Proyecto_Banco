from operator import truediv
from os import system

def accountExist() -> bool:
    list = []
    with open('./BDD/bankAccount.txt', 'r', encoding='utf-8') as f:
        for line in f:
            list.append(str(line))
    if list == []:
        print(list)
        return False
    else:
        print(list)
        return True


def run():
    print("Bienvenido al Banco de Guatemala")
    print("1.) Manejo de Cuentas Personales:")
    print("2.) Cuentas de Terceros:")
    print("3.) Ver Cuenta Actual:")
    print("4.) Realizar Deposito:")
    print("5.) Realizar Retiro:")
    print("")
    option: int = int(input("Seleecione una Opcion: "))
    
    if option == 1:
        system("cls")
        if accountExist() == True:
            print("Cuenta Existe")
        else:
            print("Cuenta no Existe")



if __name__ == '__main__':
    run()