print("Programa Expresso/n")
print("Cadastrar Restaurante")
print("Listar Restaurantes")
print("Ativar Restaurente")
print("Sair/n")

opcao_digitada=int input(("EScolha uma opção"))
print ("Você escolheu a opção", opcao_digitada,"\n")

if(opcao_digitada==1):
    print(' Você escolheu dse cadastrar no restaurante \n')
elif(opcao_digitada==2):
    print('Você escolheu listar os restaurantes \n')
elif(opcao_digitada==3):
    print('Você escolheu ativar um restaurante \n')
else:
    print('Fim do programa')

