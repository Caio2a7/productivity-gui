import csv

# Dados a serem escritos no arquivo CSV
widgets_list = [
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},
        {'Projetos': '0:00:00', 'Cursos': '0:00:00', 'AWS': '0:00:00', 'Leituras': '0:00:00', 'FMC2': '0:00:00', 'ARQ': '0:00:00', 'EDB1': '0:00:00', 'LP1': '0:00:00'},]


class Reset:
    def __init__(self):
        pass
    
    def res(self):
        # Abrir um arquivo CSV para escrita
        with open('data/input/tempos.csv', 'w', newline='') as csvfile:
            fieldnames = widgets_list[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for widget in widgets_list:
                writer.writerow(widget)


