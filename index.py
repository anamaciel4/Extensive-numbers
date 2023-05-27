import time
import os

print ("{:^73}".format("\033[33m\033[1mSeja bem-vindo(a)!\033[0;0m"))

def binary_subtraction(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]
def binary_addition(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]
opcao = -5

#Início
while True:
  print ('\033[34m------------------------------------------------------------------\033[0;0m')
  print ("""Escolha um cálculo:
[1] Conversão da base decimal para as bases binário e octadecimal.
[2] Conversão das bases binário e octadecimal para decimal.
[3] Calculadora aritmética de binários (Soma e subtração).
[4] Encerrar""")
  print ('\033[34m------------------------------------------------------------------\033[0;0m')
  opcao=int(input("Digite sua opção: "))
  print ('\033[34m------------------------------------------------------------------\033[0;0m')
  print('')

  #Primeira opção
  if opcao == 1:
    num=(int(input("Digite um número da base decimal: ")))
    print (f"{num} convertido para binário é igual", "\033[32m\033[1m{:b}\033[0;0m".format(num, (num)))
  if opcao == 1:
    print (f"{num} convertido para octadecimal é igual", "\033[32m\033[1m{:o}\033[0;0m".format(num, (num)))
    print ('')
 
  if opcao == 2:
    nb=(input("Digite um número binário: "))
    try:
      b=int(nb,2)
      print (f"{nb} convertido para decimal é igual \033[32m\033[1m{b}\033[0;0m")
      print ('')
    except:
      print("\033[31m\033[1mO número digitado não é binário!\033[0;0m")
      print('')
    print ('\033[34m------------------------------------------------------------------\033[0;0m')
    print('')
    
  #Segunda opção
  if opcao == 2:
    try:
      nb=(input("Digite um número octal: "))
      o=int(nb,8)
      print (f"{nb} convertido para decimal é igual \033[32m\033[1m{o}\033[0;0m")
      print('')
    except:
      print("\033[31m\033[1mNúmero inválido, pois a base octaldecimal comporta apenas de 0 a 7.\033[0;0m")
      print ('')

  #Terceira opção
  elif opcao == 3:
    print ('\033[34m------------------------------------------------------------------\033[0;0m')
    print("""Escolha opção desejada: 
  [1] Subtração
  [2] Soma """)
    print ('\033[34m------------------------------------------------------------------\033[0;0m')
    opccao = int(input("Digite sua opção: "))
    print ('\033[34m------------------------------------------------------------------\033[0;0m')
    print ('')
    if opccao == 1:
      numero_binario = input('Digite o primeiro número binário: ')
      numero_binario2 = input('Digite o segundo número binário: ')
      try:
        resultado_subtração = binary_subtraction(numero_binario, numero_binario2)
        print(f'Resultado da subtração: \033[32m\033[1m{resultado_subtração}\033[0;0m')
        print ('')
      except:
        print("\033[31m\033[1mOs números digitados não são binários!\033[0;0m")
        print ('')
            
    if opccao == 2:
      numero_binario1 = input('Digite o primeiro número binário: ')
      numero_binario3 = input('Digite o segundo número binário: ')
      try:
        resultado_soma = binary_addition(numero_binario1, numero_binario3)
        print(f'Resultado da soma: \033[32m\033[1m{resultado_soma}\033[0;0m')
        print ('')
      except:
          print("\033[31m\033[1mOs números digitados não são binários!\033[31m")
          print ('')

  #Encerramento
  elif opcao == 4:
    print("F")
    time.sleep(0.2)
    os.system('clear')
    print("Fe")
    time.sleep(0.2)
    os.system('clear')
    print("Fec")
    time.sleep(0.2)
    os.system('clear')
    print("Fech")
    time.sleep(0.2)
    os.system('clear')
    print("Fecha")
    time.sleep(0.2)
    os.system('clear')
    print("Fechan")
    time.sleep(0.2)
    os.system('clear')
    print("Fechand")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o pr")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o pro")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o prog")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o progr")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o progra")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o program")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o programa")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o programa.")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o programa..")
    time.sleep(0.2)
    os.system('clear')
    print("Fechando o programa...")

    break