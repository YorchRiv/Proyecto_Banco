from operator import truediv
from os import system
from bankAccount import bankAccount

def run():
    system("cls")
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
        if bankAccount.accountExist() == True: #Comprueba si hay una Cuenta de Banco
            bankAccount.createAccount()
        else:
            print("No existe ninguna cuenta, desea crear una?: Si:1 No:0 ")
            op = int(input("Seleccione: "))
            if op == 1:
                bankAccount.createAccount()
        run()


if __name__ == '__main__':
    run()