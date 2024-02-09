import pandas

class Teste:

    def __init__(self):
        pass

    def save_time(self, dia, tarefa, horas, minutos, segundos):
        data = pandas.read_csv('../../data/input/tempos.csv')
        zero_esquerda_s = "" if segundos >= 10 else 0
        zero_esquerda_m = "" if minutos >= 10 else 0
        data.iloc[dia, tarefa] = f'{horas}:{zero_esquerda_m}{minutos}:{zero_esquerda_s}{segundos}'
        data.to_csv('../../data/input/tempos.csv', index=False)

    def read_time(self):
        return pandas.read_csv('../../data/input/tempos.csv')