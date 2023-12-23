import random

mega_sena = []
numeros_jogados = []
numeros_certos = []
jogadas_feitas = 0
vencedor = False
sorteio = 0
check_mega = 0
check_jogador = 0
zero_certos = 0
um_certo = 0
dois_certos = 0
tres_certos = 0
quadra = 0
quina = 0

while vencedor == False:
    while check_mega != 6:
        numero_sorteado = random.randint(1, 60)

        if numero_sorteado not in (mega_sena):
            mega_sena.append(numero_sorteado)

            check_mega = len(mega_sena)

    while check_jogador != 6:
        numero_jogado = random.randint(1, 60)

        if numero_jogado not in (numeros_jogados):
            numeros_jogados.append(numero_jogado)

            check_jogador = len(numeros_jogados)

    for c in range(0, 6):
        if numeros_jogados[c] in mega_sena:
            numeros_certos.append(numeros_jogados[c])
        c += 1

    if len(numeros_certos) == 6:
        print(f'{"=" * 10} VENCEU {"=" * 10}')
        print(f'Total de Jogadas: {jogadas_feitas}')
        print('Total de jogadas com:')
        print(f'Quinas: {quina} - {round(((quina/jogadas_feitas)*100),10)}%')
        print(f'Quadras: {quadra} - {round(((quadra/jogadas_feitas)*100),8)}%')
        print(f'Três Certos: {tres_certos} - {round(((tres_certos/jogadas_feitas)*100),5)}%')
        print(f'Dois Certos: {dois_certos} - {round(((dois_certos/jogadas_feitas)*100),2)}%')
        print(f'Um certo: {um_certo} - {round(((um_certo/jogadas_feitas)*100),2)}%')
        print(f'Nenhum certo: {zero_certos} - {round(((zero_certos/jogadas_feitas)*100),2)}%')
        print(f'{"=" * 10} NÚMEROS SORTEADOS {"=" * 10}')
        print(sorted(mega_sena))
        print(f'{"=" * 10} NÚMEROS APOSTADOS {"=" * 10}')
        print(sorted(numeros_jogados))
        vencedor = True
    elif len(numeros_certos) == 5:
        print(f'Quina! {numeros_certos}')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        quina += 1
    elif len(numeros_certos) == 4:
        print(f'Quadra! {numeros_certos}')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        quadra += 1
    elif len(numeros_certos) == 3:
        print(f'Três Acertos! {numeros_certos}')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        tres_certos += 1
    elif len(numeros_certos) == 2:
        print(f'Dois Acertos! {numeros_certos}')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        dois_certos += 1
    elif len(numeros_certos) == 1:
        print(f'Um Acerto! {numeros_certos}')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        um_certo += 1
    else:
        print(f'Zero Acertos!')
        print(jogadas_feitas)
        print(sorted(mega_sena))
        print(sorted(numeros_jogados))
        zero_certos += 1

    jogadas_feitas += 1
    mega_sena = []
    numeros_jogados = []
    numeros_certos = []
    check_mega = 0
    check_jogador = 0
