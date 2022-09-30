#8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.#
horas = float(input('Digite a quantidade de horas trabalhadas ao mês;'))
ganha = float(input('Digite o seu salário por hora trabalhada; ' ));
total = horas * ganha

print('Você ganha por hora', ganha, 'reais, e trabalha ganhando por dia', horas, 'seu salário mensal é de', total, 'reais');

