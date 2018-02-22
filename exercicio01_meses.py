meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
data_nasc = input('Insira a data de nascimento no formato DD-MM-AAAA: ')
cd_mes = int(data_nasc[3:5])-1
mes = meses[cd_mes]
print('Você nasceu no mês de:', mes)
input('Aperte enter para sair')
