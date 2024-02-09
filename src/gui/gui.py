import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, PhotoImage
import time
import threading
import numpy as np
import func
import reset
import pandas

day_list = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
task_list = ['FMC', 'Calculo', 'ITP', 'Curriculo', 'Cursos', 'Leetcode', 'Leitura']

'''
with open('tempos.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    dados = list(leitor_csv)

    arquivo_csv.close()


'''
def expand():
    global sidebar_width
    global padx

    if sidebar_width == 60:
        while sidebar_width < 100:
            sidebar_width += 7
            padx += 7
            left_sidebar_frame.pack_configure(ipadx=padx)
            root.update()
            root.after(30)
    else:
        
        while sidebar_width > 60:
            sidebar_width -= 7
            padx -= 7
            left_sidebar_frame.pack_configure(ipadx=padx)
            root.update()
            root.after(30)


def set_timer(dia, tarefa):
    global is_running
    if not is_running:
        start_timer(dia, tarefa)
    else:
        stop_timer(dia, tarefa)

def start_timer(dia, tarefa):
    global timer_thread, is_running, day, task
    day = dia
    task = tarefa
    is_running = True
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.daemon = True
    timer_thread.start()

def stop_timer(dia, tarefa):
    global tracking_time, is_running
    data = pandas.read_csv('tempos.csv')
    tempo_arm = data.iloc[dia].iloc[tarefa].split(":")
    tempo_armazenado = int(tempo_arm[0]) * 3600 + int(tempo_arm[1]) * 60 + int(tempo_arm[2])
    horas = int((tracking_time+tempo_armazenado) // 3600)
    minutos = (int((tracking_time+tempo_armazenado) % 3600)) // 60
    segundos = (int((tracking_time+tempo_armazenado) % 60))
    obj.save_time(dia, tarefa, horas, minutos, segundos)
    is_running = False
    tracking_time = 0

def update_timer():
    global tracking_time, widgets_objects, day, task
    time_list_csv = pandas.read_csv('tempos.csv')
    tempo_arm = time_list_csv.iloc[day].iloc[task].split(":")
    tempo_armazenado = int(tempo_arm[0])*3600 + int(tempo_arm[1])*60 + int(tempo_arm[2])
    start_time = time.time()
    while is_running:
        tracking_time = time.time() - start_time
        horas = int((tracking_time+tempo_armazenado) // 3600)
        minutos = (int((tracking_time+tempo_armazenado) % 3600)) // 60
        segundos = (int((tracking_time+tempo_armazenado) % 60))
        zero_esquerda_s = "" if segundos >= 10 else 0
        zero_esquerda_m = "" if minutos >= 10 else 0
        widgets_objects[day][task].configure(text=f"{horas}:{zero_esquerda_m}{minutos}:{zero_esquerda_s}{segundos}")

obj_r = reset.Reset()
obj = func.Teste()
root = ctk.CTk()

ctk.set_appearance_mode("dark")
root.config(background='black')
ctk.set_default_color_theme("green")

root.title("Scriptum")

img = Image.open("greek.png")
photo = ImageTk.PhotoImage(img)
root.tk.call('wm', 'iconphoto', root._w, photo)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width-200}x{screen_height-200}")


sidebar_width = 60
padx = 0

left_sidebar_frame = ctk.CTkFrame(master=root, width=sidebar_width, height=500, fg_color='#110F13')
left_sidebar_frame.pack(side='left', fill='y')

button_bar = Image.open("Button.png")
button_bar = button_bar.resize((20, 20))
button_bar = ImageTk.PhotoImage(button_bar)

image_graph = Image.open("graph.png")
image_graph = image_graph.resize((20, 20))
image_graph = ImageTk.PhotoImage(image_graph)

image_reset = Image.open("Reset.png")
image_reset = image_reset.resize((20, 20))
image_reset = ImageTk.PhotoImage(image_reset)

click_btn = Image.open('Play.png')
click_btn = click_btn.resize((30, 30))
click_btn = ImageTk.PhotoImage(click_btn)

image_clipboard = Image.open("clipboard-55.png")
image_clipboard = image_clipboard.resize((20, 20))
image_clipboard = ImageTk.PhotoImage(image_clipboard)

image_spreadsheet = Image.open("spread.png")
image_spreadsheet = image_spreadsheet.resize((20, 20))
image_spreadsheet = ImageTk.PhotoImage(image_spreadsheet)

button_expand = ctk.CTkButton(master=left_sidebar_frame, text="", image=button_bar, command=expand, width=8)
button_expand.place(x=15, y=10)

button_graph = ctk.CTkButton(master=left_sidebar_frame, text="", image=image_graph, width=8)
button_graph.place(x=15, y=60)

button_reset = ctk.CTkButton(master=left_sidebar_frame, text="", command=obj_r.reset(), image=image_reset, width=8)
button_reset.place(x=15, y=110)

button_clipboard = ctk.CTkButton(master=left_sidebar_frame, text="", image=image_clipboard, width=8)
button_clipboard.place(x=15, y=160)

button_spreadsheet = ctk.CTkButton(master=left_sidebar_frame, text="", image=image_spreadsheet, width=8)
button_spreadsheet.place(x=15, y=210)

right_sidebar_frame = ctk.CTkFrame(master=root, width=sidebar_width, height=500, fg_color='#110F13')
right_sidebar_frame.pack(side='right', fill='y')

content_frame = ctk.CTkScrollableFrame(master=root, width=800, height=1000, fg_color='black')
content_frame.pack(padx=5, pady=5)
content_frame.lower()

tracking_time = 0
is_running = False
timer_thread = None
time_list_csv = pandas.read_csv('tempos.csv')
widgets_objects = np.empty((7, 5), dtype=object)
day = 0
task = 0
class Create:

    def __init(self):
        pass

    def create_day(self, day_index):
        self.day_frame = ctk.CTkFrame(master=content_frame, height=300, width=1000, fg_color='#110F13')
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
        button_timer = tk.Button(master=task_frame, image=click_btn, 
                                 bg="#110F13", 
                                 border=0, command=lambda: set_timer(day_index, task_index))
        button_timer.place(x=100, y=1)
        tempo = time_list_csv.iloc[day_index].iloc[task_index]
        tracked_time = ctk.CTkLabel(master=task_frame, text=f'{tempo}', padx=5, font=('Calibri', 15, 'bold'))
        tracked_time.place(x=135, y=2.1)
        widgets_objects[day_index][task_index] = tracked_time
        self.add += 50


habitus = Create()
for i in range(0, 7):
    habitus.create_day(i)
    for j in range(0, 5):
        habitus.create_task(i, j)


root.mainloop()
