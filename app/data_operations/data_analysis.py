import pandas as pd
from functools import reduce
import numpy as np
import json

with open("data/input/productivity_data.json", "r") as json_file:
    DATA = json.load(json_file)

class DataAnalysis:
    def __init__(self):
        self.columns = ['Projetos' , 'Cursos', 'AWS', 'Leituras', 'FMC2', 'ARQ', 'EDB1', 'LP1']
        self.pesos = [3, 1.5, 1.5, 1, 3, 2, 2, 2]
        self.df = pd.DataFrame(DATA)

    def weight_average(self):
        weight_product = reduce(lambda x, y: x * y, self.pesos)
        self.df['Media Ponderada'] = (self.df['Projetos'] * self.pesos[0] + self.df['Cursos'] * self.pesos[1] +
                                      self.df['AWS'] * self.pesos[2] + self.df['Leituras'] * self.pesos[3] +
                                      self.df['FMC2'] * self.pesos[4] +
                                      self.df['ARQ'] * self.pesos[5] + self.df['EDB1'] * self.pesos[6] + self.df['LP1'] * self.pesos[7]) / weight_product
        return self.df['Media Ponderada']

    def median(self):
        self.df['Mediana'] = np.median(self.df[self.columns], axis=1)
        return self.df['Mediana']

    def standart_deviation(self):  # Quanto maior o desvio padrão mais distantes as horas estarão da média
        self.df['Desvio Padrao'] = np.std(self.df[self.columns], axis=1)
        return self.df['Desvio Padrao']

    def minimum(self):
        index_min = np.argmin(self.df[self.columns], axis=1)
        min_column_names = [self.columns[i] for i in index_min]
        self.df['Minimo'] = min_column_names
        return self.df['Minimo']

    def maximum(self):
        index_max = np.argmax(self.df[self.columns], axis=1)
        max_columns_names = [self.columns[i] for i in index_max]
        self.df['Maximo'] = max_columns_names
        return self.df['Maximo']
