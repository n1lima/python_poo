class Carro:
    modelo : str
    marca : str
    cor : str
    odometro = 0.0
    motor_on = False

    def __init__(self, modelo : str, marca : str, cor : str, #metodo contructor dentro da classe
                       odometro : float, motor : bool): #parametros do constructor, ele ira receber o "modelo" atributo dentro do bloco
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor

    def ligar(self):
        if not self.motor_on:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:
            self.odometro += velocidade * tempo
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self): #todo objeto em python tem o metodo __str__
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}')
        return info





