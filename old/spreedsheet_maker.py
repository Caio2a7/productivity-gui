from data_analysis import DataAnalysis
import pandas as pd


def excel_maker():
    data_analysis = DataAnalysis()
    DataAnalysis.weight_average(data_analysis)
    DataAnalysis.median(data_analysis)
    DataAnalysis.standart_deviation(data_analysis)
    DataAnalysis.minimum(data_analysis)
    DataAnalysis.maximum(data_analysis)
    data_analysis.df.to_excel("PRODUTIVIDADE.xlsx")
