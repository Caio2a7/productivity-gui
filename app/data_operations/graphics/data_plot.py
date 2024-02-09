import matplotlib.pyplot as plt
import pandas as pd
import json
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, "../.."))
sys.path.append(project_dir)

from app.data_operations.data_analysis import DataAnalysis

with open("../../data/input/productivity_data.json", 'r') as json_file:
    DATA = json.load(json_file)
df = pd.DataFrame(DATA)

plt.rcParams.update({
    'font.size': 8
})

class Grafico:

    def __init__(self):
        pass

    def main_productivity_graph(self):
        self.axs[0, 0].plot(df["Semana"], df["Horas totais"], color='g', marker="o")
        self.axs[0, 0].set_title("Horas Totais")
        self.axs[0, 1].plot(df["Semana"], df["FMC"], label="FMC", color="r", marker="o")
        self.axs[0, 1].plot(df["Semana"], df["Calculo"], label="Calculo", color="b", marker="o")
        self.axs[0, 1].set_title("FMC e Cálculo")
        self.axs[0, 1].legend(fontsize="small", loc="lower left")
        self.axs[1, 0].plot(df["Semana"], df["ITP"], label="ITP", color="c", marker="o")
        self.axs[1, 0].plot(df["Semana"], df["Leetcode"], label="Leetcode", color="m", marker="o")
        self.axs[1, 0].set_title("ITP e Leetcode")
        self.axs[1, 0].legend(fontsize="small", loc="lower left")
        self.axs[1, 1].plot(df["Semana"], df["Curriculo"], label="Curriculo", color="g", marker="o")
        self.axs[1, 1].plot(df["Semana"], df["Cursos"], label="Cursos", color="y", marker="o")
        self.axs[1, 1].set_title("Currículo, Cursos e Leituras")
        self.axs[1, 1].legend(fontsize="small", loc="lower left")
        self.axs[0, 2].plot(df["Semana"], df["Leituras"], label="Leituras", color="black", marker="o")
        self.axs[0, 2].set_title("Leitura")

    def analytics_graph(self):
        self.fig, self.axs = plt.subplots(2, 3, figsize=(15, 10))
        self.main_productivity_graph()
        data_analytics = DataAnalysis()
        self.axs[1, 2].plot(df["Semana"], data_analytics.weight_average(), label='Media Ponderada', color="purple", marker="o")
        self.axs[1, 2].plot(df["Semana"], data_analytics.median(), label='Mediana', color="pink", marker="o")
        self.axs[1, 2].plot(df["Semana"], data_analytics.standart_deviation(), label='Desvio Padrao', color="red", marker="o")
        self.axs[1, 2].set_title("Media Ponderada, Mediana, Desvio Padrao")
        self.axs[1, 2].legend(fontsize="small", loc="lower left")
        # Salvar a imagem do gráfico
        plt.savefig('../../data/output/grafico_produtividade.png')