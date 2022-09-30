sexo = float(input('Digite seu sexo: (1) para homem e (2) para mulher: '));
if sexo == 1:
    homem = float(input('Digite sua altura:'));
    pesoh = (72.7*homem) - 58;
    print('Seu peso ideal é ', pesoh,'Kgs.');
    round(pesoh);
elif sexo == 2:
    mulher = float(input('Digite sua altura: '));
    pesom = (62.1*mulher) - 44.7;
    print('Seu meso ideal é ', pesom,'Kgs.');
    round(pesom);





