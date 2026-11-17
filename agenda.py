import datetime
from weather import dados
from codes_weather import traducao_codigo
dia_atual = datetime.date.today()

def checar_dia(dia):
    dia_tipodia = datetime.datetime.strptime(dia, '%Y-%m-%d').date()
    diferenca = dia_tipodia - dia_atual
    diferenca = diferenca.days
    if diferenca >= 0 and diferenca <= 15:
        index = dados['daily']['time'].index(dia)
        clima = dados['daily']['weather_code'][index]
        print(f'O clima do dia: {dia}, em Recife, está previsto para ser: {traducao_codigo(clima)}')
    else:
        print(f'Infelizmente o dia: {dia}, não se encaixa no período disponível de previsão.')

class Agenda:
    def __init__(self):
        self.calendario = {}

    def adicionar_evento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                print('Já existe esse evento')
            else:
                self.calendario[evento].append(dia)
        else:
            self.calendario[evento] = [dia]

    def remover_evento(self, evento, dia):
        if evento in self.calendario.keys():
            if dia in self.calendario[evento]:
                self.calendario[evento].remove(dia)
                if len(self.calendario[evento]) == 0:
                    del self.calendario[evento]
            else:
                print('O evento existe, mas não nesse dia')
        else:
            print('Esse evento não existe')

    def relatorio_dia(self, dia):
        relatorio = [x for x,y in self.calendario.items() if dia in y]
        if relatorio != []:
            print(relatorio)
        else:
            print('Não há eventos para esse dia')
        checar_dia(dia)

    def detalhe_evento(self, evento):
        dia = [y for x,y in self.calendario.items() if x == evento]
        if len(dia) == 1:
            dia = dia[0]
        if len(dia) == 0:
            print('Esse evento não tem nenhum dia')
        else:
            print(dia)
        for i in dia:
            checar_dia(i)

    def mostrar_calendario(self):
        print(self.calendario)