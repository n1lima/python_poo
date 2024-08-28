class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro = 0.0
    __motor_on = False
    __tanque = 0.0
    consumo_medio = float

    def __init__(self, modelo : str, marca : str, cor : str,
                odometro : float, motor : bool, tanque : float, consumo_medio: float): #parametros do constructor, ele ira receber o "modelo" atributo dentro do bloco
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__moto_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo_medio

    def ligar(self):
        if not self.__moto_on and self.__tanque > 0:
             self.__moto_on = True
        else:
            raise Exception("Erro: Motor já ligado ou o tanque está vazio!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__moto_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km/self.consumo_medio

            if self.__tanque >= litros:
                self.__tanque -= litros
            else:
                km = litros * self.consumo_medio
                self.__tanque = 0
                self.desligar()
            self.__odometro += km

        else:
            raise Exception('Erro: Não é possível acelerar! Motor desligado ou sem combustível!');
    def desligar(self):
        if self.__moto_on:
            self.__moto_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def get_odometro(self):
        return self.__odometro

    def __str__(self): #todo objeto em python tem o metodo __str__
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__moto_on} consumo {self.consumo_medio} km/l {self.__tanque}')
        return info





