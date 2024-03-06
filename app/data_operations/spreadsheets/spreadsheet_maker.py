import pandas as pd
from app.data_operations.data_analysis import DataAnalysis

class Spreadsheet:
    def __init__(self):
        pass

    def excel_maker(self):
        data_analysis = DataAnalysis()
        DataAnalysis.weight_average(data_analysis)
        DataAnalysis.median(data_analysis)
        DataAnalysis.standart_deviation(data_analysis)
        DataAnalysis.minimum(data_analysis)
        DataAnalysis.maximum(data_analysis)
        data_analysis.df.to_excel("data/output/PRODUTIVIDADE.xlsx")
