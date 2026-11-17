import datetime
from weather import dados
from codes_weather import traducao_codigo
dia_atual = datetime.date.today()

class agenda:
    def __init__(self):
        self.calendario = {}

    def adicionarEvento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                print('Já existe esse evento')
            else:
                self.calendario[evento].append(dia)
        else:
            self.calendario[evento] = [dia]

    def removerEvento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                self.calendario[evento].remove(dia)
                if len(self.calendario[evento]) == 0:
                    del self.calendario[evento]
            else:
                print('O evento existe, mas não nesse dia')
        else:
            print('Esse evento não existe')

    def relatorioDia(self, dia):
        relatorio = [x for x,y in self.calendario.items() if dia in y]
        print(relatorio)
        dia_tipodia = datetime.date.strptime(dia, '%Y-%m-%d')
        diferenca = dia_tipodia - dia_atual
        diferenca = diferenca.days
        if diferenca > 0 and diferenca <= 16:
            index = dados['daily']['time'].index(dia)
            clima = dados['daily']['weather_code'][index]
            print(f'O clima do dia: {dia}, em Recife, está previsto para ser: {traducao_codigo(clima)}')
        else:
            print('Infelizmente não se encaixa no período disponível de previsão.')

    def diaEvento(self, evento):
        dia = [y for x,y in self.calendario.items() if x == evento]
        if len(dia) == 1:
            dia = dia[0]
        print(dia)

    def mostrarCalendario(self):
        print(self.calendario)