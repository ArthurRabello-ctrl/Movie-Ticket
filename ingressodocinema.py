preco_base = 15
final_de_semana = True
idade_minima = int(input('Digite a idade do visitante: '))
socio_premium = str(input('Digite se o visitante é sócio Premium (sim/não): '))
socio_gold = str(input('Digite se o visitante é sócio Gold (sim/não): '))
pipoca_e_refri = str(input('Digite se o visitante deseja comprar pipoca e refrigerante (sim/não): '))
if idade_minima >= 18:
    print('O visitante está habilitado para assistir ao show!')
else:
    print('O visitante é menor de idade, portanto não pode assistir ao show')

if final_de_semana:
    preco_base += 5
    print('O preço base do ingresso no final de semana é de R$' + str(round(preco_base, 2)))
else:
    print('O preço base do ingresso durante a semana é de R$' + str(round(preco_base, 2)))

if socio_premium == 'sim':
    desconto_premium = preco_base * 0.2
    preco_premium = preco_base - desconto_premium
    print('O visitante é sócio Premium e tem direito a um desconto de R$' + str(round(desconto_premium, 2)))
else:
    print('O visitante não é sócio Premium e não tem direito a desconto')

if socio_gold == 'sim':
    desconto_gold = preco_base * 0.1
    preco_gold = preco_base - desconto_gold
    print('O visitante é sócio Gold e tem direito a um desconto de R$' + str(round(desconto_gold, 2)))
else:
    print('O visitante não é sócio Gold e não tem direito a desconto')

if pipoca_e_refri == 'sim':
    preco_base += 10
    print('O visitante optou por comprar pipoca e refrigerante, adicionando R$10 ao preço final do ingresso')

if socio_premium == 'sim':
    preco_final = preco_premium + 10
    print('O preço final do ingresso para o sócio Premium é de R$' + str(round(preco_final, 2)))
elif socio_gold == 'sim':
    preco_final = preco_gold + 10
    print('O preço final do ingresso para o sócio Gold é de R$' + str(round(preco_final, 2)))
else:
    preco_final = preco_base
    print('O preço final do ingresso para o visitante é de R$' + str(round(preco_final, 2)))

