##11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo.
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.#




pedido1 = int(input('Digite um número inteiro; '));
pedido2 = int(input('Digite outro número inteiro; '));
pedido3 = float(input('Digite um número real; '));

a = pedido1 * 2 * (pedido2 / 2);
print('O produto do dobro do primeiro com metade do segundo é igual à', a);
b = pedido1 *3 + pedido3
print('a soma do triplo do primeiro com o terceiro é igual à', b);
c = pedido3 ** 3;
print('o terceiro elevado ao cubo', c);