import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, PhotoImage
import time
import threading
import numpy as np
import grafico
import func
import reset
day_list = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
task_list = ['FMC', 'Calculo', 'ITP', 'Curriculo', 'Cursos', 'Leetcode', 'Leitura']

'''
with open('tempos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados = list(leitor_csv)

    arquivo_csv.close()


'''

obj_r = reset.Reset()
obj_g = grafico.Grafico()
obj = func.Teste()

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.config(background='black')
        ctk.set_default_color_theme("green")
        self.title("Scriptum")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width-200}x{screen_height-200}")
        self.sidebar_width = 60
        self.padx = 0
        self.left_sidebar_frame = ctk.CTkFrame(master=self, width=self.sidebar_width, height=500, fg_color='#110F13')
        self.left_sidebar_frame.pack(side='left', fill='y')
        button_bar = Image.open("Button.png")
        button_bar = button_bar.resize((20, 20))
        button_bar = ImageTk.PhotoImage(button_bar)
        image_graph = Image.open("graph.png")
        image_graph = image_graph.resize((20, 20))
        image_graph = ImageTk.PhotoImage(image_graph)

        image_reset = Image.open("Reset.png")
        image_reset = image_reset.resize((20, 20))
        image_reset = ImageTk.PhotoImage(image_reset)

        self.click_btn = Image.open('Play.png')
        self.click_btn = self.click_btn.resize((30, 30))
        self.click_btn = ImageTk.PhotoImage(self.click_btn)

        image_clipboard = Image.open("clipboard-55.png")
        image_clipboard = image_clipboard.resize((20, 20))
        image_clipboard = ImageTk.PhotoImage(image_clipboard)

        image_spreadsheet = Image.open("spread.png")
        image_spreadsheet = image_spreadsheet.resize((20, 20))
        image_spreadsheet = ImageTk.PhotoImage(image_spreadsheet)

        button_expand = ctk.CTkButton(master=self.left_sidebar_frame, text="", image=button_bar, command=self.expand, width=8)
        button_expand.place(x=15, y=10)

        button_graph = ctk.CTkButton(master=self.left_sidebar_frame, text="", command=obj_g.analytics_graph ,image=image_graph, width=8)
        button_graph.place(x=15, y=60)

        button_reset = ctk.CTkButton(master=self.left_sidebar_frame, text="", command=obj_r.res, image=image_reset, width=8)
        button_reset.place(x=15, y=110)

        button_clipboard = ctk.CTkButton(master=self.left_sidebar_frame, text="", image=image_clipboard, width=8)
        button_clipboard.place(x=15, y=160)

        button_spreadsheet = ctk.CTkButton(master=self.left_sidebar_frame, text="", image=image_spreadsheet, width=8)
        button_spreadsheet.place(x=15, y=210)

        right_sidebar_frame = ctk.CTkFrame(master=self, width=self.sidebar_width, height=500, fg_color='#110F13')
        right_sidebar_frame.pack(side='right', fill='y')

        self.content_frame = ctk.CTkScrollableFrame(master=self, width=800, height=1000, fg_color='black')
        self.content_frame.pack(padx=5, pady=5)
        self.content_frame.lower()

        self.tracking_time = 0
        self.is_running = False
        self.timer_thread = None
        self.time_list_csv = obj.read_time()
        self.widgets_objects = np.empty((7, 5), dtype=object)
        self.day = 0
        self.task = 0
        img = Image.open("greek.png")

        # Criar o objeto PhotoImage
        self.photo = ImageTk.PhotoImage(img)

        # Definir a imagem como ícone
        self.tk.call('wm', 'iconphoto', self._w, self.photo)
    def create_day(self, day_index):
        self.day_frame = ctk.CTkFrame(master=self.content_frame, height=300, width=1000, fg_color='#110F13')
        self.day_frame.pack(padx=10, pady=10)
        text = ctk.CTkLabel(master=self.day_frame, text=f"{day_list[day_index]}", font=('Calibri', 15, 'bold'),
                            padx=5, corner_radius=50, fg_color='#2CC985', text_color='#222923')
        text.place(x=5, y=0)
        self.add = 0


    def create_task(self, day_index, task_index):
        task_frame = ctk.CTkFrame(master=self.day_frame, height=35, width=760, fg_color='#110F13')
        task_frame.place(y=60 + self.add, x=390, anchor='center')
        task_name = ctk.CTkLabel(master=task_frame, text=f'{task_list[j]}', padx=5, font=('Calibri', 15, 'bold'))
        task_name.place(x=20, y=2.1)
        button_timer = tk.Button(master=task_frame, image=self.click_btn, 
                                 bg="#110F13", 
                                 border=0, command=lambda: self.set_timer(day_index, task_index))
        button_timer.place(x=100, y=1)
        tempo = self.time_list_csv.iloc[day_index].iloc[task_index]
        tracked_time = ctk.CTkLabel(master=task_frame, text=f'{tempo}', padx=5, font=('Calibri', 15, 'bold'))
        tracked_time.place(x=135, y=2.1)
        self.widgets_objects[day_index][task_index] = tracked_time
        self.add += 50

    def expand(self):
        if self.sidebar_width == 60:
            while self.sidebar_width < 100:
                self.sidebar_width += 7
                self.padx += 7
                self.left_sidebar_frame.pack_configure(ipadx=self.padx)
                self.update()
                self.after(30)
        else:

            while self.sidebar_width > 60:
                self.sidebar_width -= 7
                self.padx -= 7
                self.left_sidebar_frame.pack_configure(ipadx=self.padx)
                self.update()
                self.after(30)


    def set_timer(self, dia, tarefa):
        if not self.is_running:
            self.start_timer(dia, tarefa)
        else:
            self.stop_timer(dia, tarefa)

    def start_timer(self, dia, tarefa):
        self.day = dia
        self.task = tarefa
        self.is_running = True
        self.timer_thread = threading.Thread(target=self.update_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def stop_timer(self, dia, tarefa):
        data = obj.read_time()
        tempo_arm = data.iloc[dia].iloc[tarefa].split(":")
        tempo_armazenado = int(tempo_arm[0]) * 3600 + int(tempo_arm[1]) * 60 + int(tempo_arm[2])
        horas = int((self.tracking_time+tempo_armazenado) // 3600)
        minutos = (int((self.tracking_time+tempo_armazenado) % 3600)) // 60
        segundos = (int((self.tracking_time+tempo_armazenado) % 60))
        obj.save_time(dia, tarefa, horas, minutos, segundos)
        self.is_running = False
        self.tracking_time = 0

    def update_timer(self):
        time_list_csv = obj.read_time()
        tempo_arm = time_list_csv.iloc[self.day].iloc[self.task].split(":")
        tempo_armazenado = int(tempo_arm[0])*3600 + int(tempo_arm[1])*60 + int(tempo_arm[2])
        start_time = time.time()
        while self.is_running:
            self.tracking_time = time.time() - start_time
            horas = int((self.tracking_time+tempo_armazenado) // 3600)
            minutos = (int((self.tracking_time+tempo_armazenado) % 3600)) // 60
            segundos = (int((self.tracking_time+tempo_armazenado) % 60))
            zero_esquerda_s = "" if segundos >= 10 else 0
            zero_esquerda_m = "" if minutos >= 10 else 0
            self.widgets_objects[self.day][self.task].configure(text=f"{horas}:{zero_esquerda_m}{minutos}:{zero_esquerda_s}{segundos}")

app = MyApp()
for i in range(0, 7):
    app.create_day(i)
    for j in range(0, 5):
        app.create_task(i, j)
app.mainloop()