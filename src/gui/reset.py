import csv

class Reset:
    def __init__(self):
        pass
    
    def reset(self):
    # Dados a serem escritos no arquivo CSV
        widgets_list = [
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'},
        {'FMC': '0:00:00', 'Calculo': '0:00:00', 'ITP': '0:00:00', 'Curriculo': '0:00:00', 'Cursos': '0:00:00', 'Leetcode': '0:00:00', 'Leitura': '0:00:00'}]


        # Abrir um arquivo CSV para escrita
        with open('tempos.csv', 'w', newline='') as csvfile:
            fieldnames = widgets_list[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for widget in widgets_list:
                writer.writerow(widget)


