from frota import *
def operar_carro(carro:Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    tanque = float(input('Nivel do tanque: '))
    consumoMedio = float(input('Consumo Medio: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, tanque, consumoMedio)
    #ele vai gerar os atributos da classe carro e atribuir ao objeto carro1

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    tanque = float(input('Nivel do tanque: '))
    consumoMedio = float(input('Consumo Medio: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, tanque, consumoMedio)
    '''
    Controlando 2 carros até ele atingir 600 Km
    '''
    while carro1.get_odometro() < 600 and carro2.get_odometro() < 600 and (carro1.get_tanque() > 0 or carro2.get_tanque() > 0) :
        try:
            op = 0
            while op not in (1,2):
                op = int(input('Qual carro você vai operar[1 ou 2]?'))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)

    if carro1.odometro > carro2.odometro:
        print('Carro 1 do modelo '+carro1.modelo+ 'ganhou')
    else:
        print('Carro 2 do modelo' + carro2.modelo + 'ganhou')



