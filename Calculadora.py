def calculadora():
    print("=====================")
    print("    Calculadora")
    print("=====================")

    while True:
        print("\nEscolha uma operação: ")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao=input("\nDigite sua opção: ")

        if opcao=="5":
            print("Calculadora encerrada!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            n1=float(input("Primeiro Número: "))
            n2=float(input("Segundo Número: "))
        except ValueError:
            print("Digite apenas números válidos!")
            continue

        if opcao=="1": 
            resultado = n1 + n2
        elif opcao=="2": 
            resultado = n1 - n2
        elif opcao=="3": 
            resultado = n1 * n2
        else:
            if n2==0:
                print("Erro: divisão por zero!")
                continue
            resultado = n1 / n2

        print(f"\nResultado:{resultado}")

if __name__ == "__main__":
  calculadora()
