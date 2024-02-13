#lista e dicionário

#estados é as vertices
#simbolos é as arestas

#estados é representado numericamente
#e simbolos são por letras a b por exemplo

N = 0 #n mapeado
estado_inicial = "" 
F = 0
estados_finais = []
S = 0 #número de simbolos do simbolos
simbolos = []
estados = []
M = [] #numero de funções de transição
transicoes = {} #dicionario de funcoes

# recebendo os dados do usuário do autômato

print("Informe o número de estados do autômato")
N = int(input())
estados = []
for i in range(N):
    estados.append(int(i + 1))
print("Estados:", estados)

print("Informe o estado inicial: ")
estado_inicial = None
while estado_inicial not in estados:
  try:
      estado_inicial = int(input().split()[0])
      if estado_inicial not in estados:
          print("Estado inicial não está na lista de estados. Por favor, insira um valor válido: ")
  except Exception as e:
      print("Estado inicial incorreto, favor inserir um valor válido: ")

print("Estado inicial válido:", estado_inicial)


print("Informe o número de estados finais")
F = int(input())

print("OS ESTADOS FINAIS SÃO INSERIDOS POR LOOP, FAVOR INSERIR UM POR VEZ")

for i in range(F):
  estado_final = None
  while estado_final not in estados:
    if F == 1:
      print(f"Informe o estado final: ")
      estado_final = (input().split()[0])
    else:
      print(f"Informe o {i + 1}º estado final:")
      estado_final = input().split()[0]

    try:
      estado_final = int(estado_final)
      if estado_final not in estados:
        print("Estado final não está na lista de estados. Por favor, insira um valor válido")
      else:
        if estado_final not in estados_finais:
          estados_finais.append(estado_final)
        else: 
          estado_final = None
          print("Estado final repetido, favor inserir outro valor.")
    except:
      print("Estado final incorreto, favor inserir um valor válido:")
    
print("Estados finais:", estados_finais)
print("Informe o número de símbolos do alfabeto:")
S = int(input())

print("Informe os simbolos de entrada: ")
simbolos = input().split()

while len(simbolos) < S:
  print("Quantidade de símbolos menor que a informada anteriormente, favor inserir a quantidade correta: ")
  simbolos = input().split()

print("Informe o número de transições:")
M = int(input())
for i in range(M):
  print(f"Insira o {i + 1}º método de transição: ")
  metodo = input().split()
  while not (metodo[0].isdigit() and metodo[2].isdigit()):
    print("Valor inserido para estado é incorreto, favor fornecer um valor numérico")
    metodo = input().split()

  chave = (int(metodo[0]), metodo[1])
  while chave in transicoes:
    print(f"Este símbolo já foi inserido para este estado, favor inserir um método diferente: ({metodo[0]} , {metodo[1]})")
    print(f"Insira o {i + 1}º método de transição: ")
    metodo = input().split()
    while not (metodo[0].isdigit() and metodo[2].isdigit()):
      print("Valor inserido para estado é incorreto, favor fornecer um valor numérico")
      print(f"Insira o {i + 1}º método de transição: ")
      metodo = input().split()
    chave = (int(metodo[0]), metodo[1])

  while metodo[1] not in simbolos:
    print("Símbolo inserido é inválido, favor inserir outro:")
    metodo = input().split()

  while int(metodo[0]) not in estados:
    print(f"método incorreto: estado inserido ({metodo[0]}) não está na lista de estados\n")
    print(f"Insira o {i + 1}º método de transição: ")
    metodo = input().split()
  while int(metodo[2]) not in estados:
    print(f"método incorreto: estado inserido ({metodo[2]}) não está na lista de estados\n")
    print(f"Insira o {i + 1}º método de transição: ")
    
    metodo = input().split()
  if metodo == ".":
    transicoes[(int(metodo[0]), metodo[1])] = None
  else:
    transicoes[(int(metodo[0]), metodo[1])] = int(metodo[2])

#reconhecendo linguagens
print("Informe a linguagem a ser reconhecida: ")
cadeia_entrada = input()

estado_atual = estado_inicial

for simbolo in cadeia_entrada:
  tempAtual = estado_atual
  print(f"Estado atual: {estado_atual}")
  print(f"Entrada atual: {simbolo}")
  try:
    print(f"Próximo estado: {transicoes[(estado_atual, simbolo)]}")
    estado_atual = transicoes[(estado_atual, simbolo)]
  except Exception as e:
    print("Erro: ", e)
    estado_atual = None
    print(f"Cadeia Rejeitada: transição não definida: ({tempAtual} , {simbolo})")
    exit()


if estado_atual in estados_finais:
  print("Cadeia aceita!")
else:
  print("Cadeia Rejeitada: não está no estado final")
