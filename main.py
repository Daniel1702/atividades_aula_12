#print("---------------Atividade 02----------------")#
print("---------------Atividade 02----------------")
print("\n=============== MÉDIA DE 4 NOTAS ============\n")
a = float(input("Digite a primeira nota: ").replace(',','.'))
b = float(input("Digite a segunda nota: ").replace(',','.'))
c = float(input("Digite a terceira nota: ").replace(',','.'))
d = float(input("Digite a quarta nota: ").replace(',','.'))

med = (a+b+c+d)/4 
média = med 

print("\nA média das notas digitadas é: {:.2f} ".format(média))

#------------------Atividade 01-----------------------#
print('\n\n')
print("---------------Atividade 01----------------")
print("\n============ CONVERSOR DE METROS PARA CENTÍMETROS ========\n")

metros = float(input("Digite a quantidade de metros para converter em centímetros: \n").replace(',','.'))

cent = metros *100
a = cent

print("A Quantidade de metros digitada será convertida em: {:.2f} centímetros".format(a))
