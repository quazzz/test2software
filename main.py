f = open('parkla.txt', encoding='UTF-8')
parkla = []
parkija_asukoht = {}
for rida in f:
    p = []
    for sona in rida.strip():
        p.append(sona)
    parkla.append(p)
f.close()
def main():
    s = int(input('1 - uus park, 2 - leida, 3 - lõpetamine, 4-parkla seis, 5 - programmi töö lõpetamine '))
    if s == 1:
        name = str(input('Sisesta oma nimi '))
        cords = [int(x) for x in input('Sisesta koordinadid ').strip().split(',')]
        print(cords)
        if parkla[cords[0]][cords[1]] == '-' or parkla[cords[0]][cords[1]] == 'X':
            print('Sellele kohale parkida ei saa. ')
            main()
        else:
            parkija_asukoht[name] = cords
            print(parkija_asukoht)
            parkla[cords[0]][cords[1]] = 'X'
            print(parkla)
            main()
    elif s == 2:
        name = str(input('Sisesta oma nimi auto leidmiseks '))
        cords = parkija_asukoht[name]
        print(*cords)
        main()
    elif s == 3:
        name = str(input('Sisesta oma nime parkimise lõpetamiseks '))
        cords = parkija_asukoht[name]
        parkla[cords[0]][cords[1]] = 'P'
        parkija_asukoht.pop(name)
        main()
    elif s == 4:
        print(parkla)
        main()
    elif s == 5:
        print(parkla)
        with open('uus_parkla.txt','w') as file:
            for rida in parkla:
                file.write(''.join(rida) + '\n')
        print('Programm suleb ära')
        exit()

       
if __name__ == '__main__':
    main()