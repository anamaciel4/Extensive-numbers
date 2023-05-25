print ("Seja bem-vindo(a)!")

def binary_subtraction(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]
def binary_addition(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]
opcao = -5

while True:
  print ('------------------------------------------------------------------')
  print ("""Escolha um cálculo:
[1] Conversão da base decimal para as bases binário e octadecimal
[2] Conversão das bases binário e octadecimal para decimal.
[3] Calculadora aritmética de binários (Soma e subtração)
[4] Encerrar""")
  print ('------------------------------------------------------------------')
  opcao=int(input("Digite sua opção: "))
  print ('------------------------------------------------------------------')

  if opcao == 1:
    num=(int(input("Digite um número da base decimal: ")))
    print ("{} convertido para binário é igual {:b}".format(num, (num)))
  
  if opcao == 1:
    print ("{} convertido em hexadecimal é igual {:o}".format(num, (num)))
 
  if opcao == 2:
    nb=(input("Digite um número binário: "))
    try:
      b=int(nb,2)
      print (f"{nb} convertido para decimal é igual {b}")
    except:
      print("O número digitado não é binário!")

      
    print ('------------------------------------------------------------------')
  if opcao == 2:
    nb=(input("Digite um número octal: "))
    o=int(nb,8)
    print (f"{nb} convertido para decimal é igual {o}")

  elif opcao == 3:
    print("""Escolha opção desejada: 
  [1] Subtração
  [2] Soma """)
    print ('------------------------------------------------------------------')
    opccao = int(input("Digite sua opção: "))
    print ('------------------------------------------------------------------')
    if opccao == 1:
      numero_binario = input('Digite o primeiro número binário: ')
      numero_binario2 = input('Digite o segundo número binário: ')
      try:
        resultado_subtração = binary_subtraction(numero_binario, numero_binario2)
        print(' Resultado da subtração: ', resultado_subtração)
      except:
        print("Os números digitados não são binários!")
            
    if opccao == 2:
      numero_binario1 = input('Digite o primeiro número binário: ')
      numero_binario3 = input('Digite o segundo número binário: ')
      try:
        resultado_soma = binary_addition(numero_binario1, numero_binario3)
        print('Resultado da soma: ', resultado_soma)
      except:
          print("Os números digitados não são binários!")
      

  elif opcao == 4:
    print('Encerrando o programa...')
    break