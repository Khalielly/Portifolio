# distancia = float(input("Qual a distancia em Km você deseja percorrer? "))
# bandeira = int(input("Digite a n° da bandeira: "))

# if distancia <= 200 and bandeira == 1 or bandeira == 2:
#     preco_total = distancia * 2.0
#     if bandeira == 1:
#         preco_total * bandeira
#         print(preco_total)
#     else: 
#         preco_total * bandeira
#         print(preco_total)

# else:
#     preco_total = distancia * 1.75
#     if bandeira == 1:
#         preco_total * bandeira
#         print(preco_total)
#     else:
#         preco_total * bandeira
#         print(preco_total)

# semana = int(input("Digite o número do dia da semana que deseja: "))

# if semana == 1:
#     print("Domingo")
# elif semana == 2:
#     print = ("Segunda")
# elif semana == 3:
#     print("Terça")
# elif semana == 4:
#     print("Quarta")
# elif semana == 5:
#     print("Quinta")
# elif semana == 6:
#     print("Sexta")
# elif semana == 7:
#     print("Sábado")
# else:
#     print(f"Meu nobre uma semana tem 7 dias e não {semana}")


# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite um número: "))
# operacao = input("Qual das seguintes operações deseja realizar (*, /, -, +): ")

# if operacao == '+' or operacao == "soma":
#     soma = n1 + n2
#     print(soma)
# elif operacao == '-' or operacao == "subtração":
#     soma = n1 - n2
#     print(soma)
# elif operacao == '*' or operacao == "multiplicação":
#     soma = n1 * n2
#     print(soma)
# elif operacao == '/' or operacao == "divisão":
#     soma = n1/n2
#     print(soma)

# casa = float(input("Digite o valor da casa: "))
# salario = float(input("Digite o valor do seu sálario: "))
# quant_anos = int(input("Digite a quantidade de anos para pagar: "))
# quant_anos *= 12

# prestacao = casa/quant_anos

# if prestacao > 0.3 * salario:
#     print("Invalido")
# else:
#     print(f"Ficou esse valor R${prestacao: .2f}")

quant_kwh = float(input("Qual a quant de kWh consumida: "))
instalacao= input("Qual tipo de instlação deseja: ")

if instalacao == 'R':
    if quant_kwh <= 500:
        quant_kwh *= 0.40
        print(quant_kwh)
    else:
        quant_kwh *= 0.65
        print(quant_kwh)
elif instalacao == 'I':
    if quant_kwh <= 1000:
        quant_kwh *= 0.55
        print(quant_kwh)
    else:
        quant_kwh *= 0.60
        print(quant_kwh)
elif instalacao == 'C':
    if quant_kwh <= 5000:
        quant_kwh *= 0.55 
        print(quant_kwh)
    else:
        quant_kwh *= 0.60
        print(quant_kwh)