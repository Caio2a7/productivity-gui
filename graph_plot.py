import matplotlib.pyplot as plt
import pandas as pd
import json
import customtkinter
import textwrap
from data_analysis import DataAnalysis

with open("productivity_data.json", 'r') as json_file:
    DATA = json.load(json_file)
df = pd.DataFrame(DATA)
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
plt.rcParams.update({
                    'font.size': 8,
                    'font.family': 'Calibri'
})

def main_productivity_graph():
    axs[0, 0].plot(df["Semana"], df["Horas totais"], color='g', marker="o")
    axs[0, 0].set_title("Horas Totais")
    axs[0, 1].plot(df["Semana"], df["FMC"], label="FMC", color="r", marker="o")
    axs[0, 1].plot(df["Semana"], df["Calculo"], label="Calculo", color="b", marker="o")
    axs[0, 1].set_title("FMC e Cálculo")
    axs[0, 1].legend(fontsize="small", loc="lower left")
    axs[1, 0].plot(df["Semana"], df["ITP"], label="ITP", color="c", marker="o")
    axs[1, 0].plot(df["Semana"], df["Leetcode"], label="Leetcode", color="m", marker="o")
    axs[1, 0].set_title("ITP e Leetcode")
    axs[1, 0].legend(fontsize="small", loc="lower left")
    axs[1, 1].plot(df["Semana"], df["Curriculo"], label="Curriculo", color="g", marker="o")
    axs[1, 1].plot(df["Semana"], df["Cursos"], label="Cursos", color="y", marker="o")
    axs[1, 1].set_title("Currículo, Cursos e Leituras")
    axs[1, 1].legend(fontsize="small", loc="lower left")
    axs[0, 2].plot(df["Semana"], df["Leituras"], label="Leituras", color="black", marker="o")
    axs[0, 2].set_title("Leitura")


def analytics_graph():
    data_analytics = DataAnalysis()
    axs[1, 2].plot(df["Semana"], data_analytics.weight_average(), label='Media Ponderada', color="purple", marker="o")
    axs[1, 2].plot(df["Semana"], data_analytics.median(), label='Mediana', color="pink", marker="o")
    axs[1, 2].plot(df["Semana"], data_analytics.standart_deviation(), label='Desvio Padrao', color="red", marker="o")
    axs[1, 2].set_title("Media Ponderada, Mediana, Desvio Padrao")
    axs[1, 2].legend(fontsize="small", loc="lower left")
    plt.show()

def observations_graph():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    root = customtkinter.CTk()
    root.title("Observacoes para semanas")
    root.geometry('720x640')

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=0, padx=0)

    for semanas, obs in enumerate(df["Observacoes"]):
        wrapped_text = textwrap.fill(obs, width=100)
        label = customtkinter.CTkLabel(master=frame, text=f'{semanas+1}ª semana: {wrapped_text}')
        label.pack(pady=20, padx=40)

    root.mainloop()
