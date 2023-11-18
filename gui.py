import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading
import csv

day_list = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
task_list = ['FMC', 'Cálculo', 'ITP', 'Currículo', 'Cursos', 'Leetcode', 'Leitura']
time_list = [f'00:00:00', '0:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00']

def expand():
    global sidebar_width
    global padx

    if sidebar_width == 100:
        while sidebar_width < 150:
            sidebar_width += 10
            padx += 10
            left_sidebar_frame.pack_configure(ipadx=padx)
            root.update()
            root.after(50)
    else:
        while sidebar_width > 100:
            sidebar_width -= 10
            padx -= 10
            left_sidebar_frame.pack_configure(ipadx=padx)
            root.update()
            root.after(50)

def save_time(dia, tarefa, horas, minutos, segundos):
    global dias
    dias[dia].configure(text=f"{horas}:{minutos}:{segundos}")

def set_timer(dia, tarefa):
    print(f"{dia} {tarefa}")
    global is_running, j, i
    if not is_running:
        start_timer()
    else:
        stop_timer(dia, tarefa)

def start_timer():
    global timer_thread, is_running
    is_running = True
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.daemon = True
    timer_thread.start()

def stop_timer(dia, tarefa):
    global tracking_time, is_running
    horas = int(tracking_time // 3600)
    minutos = (int(tracking_time % 3600)) // 60
    segundos = (int(tracking_time % 60))
    save_time(dia, tarefa, horas, minutos, segundos)
    is_running = False
    tracking_time = 0
    print(f'{horas} horas | {minutos} minutos | {segundos} segundos')

def update_timer():
    global tracking_time
    start_time = time.time()
    while is_running:
        tracking_time = time.time() - start_time
        time.sleep(1)


root = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root.title("Productivity Management")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width-200}x{screen_height-200}")

caminho_icone = '.\greek-column_48051.ico'
root.iconbitmap(caminho_icone)

sidebar_width = 100
padx = 0

left_sidebar_frame = ctk.CTkFrame(master=root, width=sidebar_width, height=500, fg_color='#373838')
left_sidebar_frame.pack(side='left', fill='y')

button_expand = ctk.CTkButton(master=left_sidebar_frame, text="Open", command=expand, width=75, fg_color='#00DF24')
button_expand.place(x=10, y=10)

right_sidebar_frame = ctk.CTkFrame(master=root, width=sidebar_width, height=500, fg_color='#373838')
right_sidebar_frame.pack(side='right', fill='y')

click_btn = Image.open('D:\Python_Projetos\Productivity_Analyser-main\Group 5.png')
click_btn = click_btn.resize((30, 30))
click_btn = ImageTk.PhotoImage(click_btn)

content_frame = ctk.CTkScrollableFrame(master=root, width=800, height=1000)
content_frame.pack(padx=5, pady=5)
content_frame.lower()

tracking_time = 0
is_running = False
timer_thread = None
lista_tempos = []
class Create:

    def __init(self):
        pass

    def create_day(self, day_index):
        self.day_frame = ctk.CTkFrame(master=content_frame, height=300, width=1000, fg_color='#373838')
        self.day_frame.pack(padx=10, pady=10)
        text = ctk.CTkLabel(master=self.day_frame, text=f"{day_list[day_index]}", font=('Calibri', 15, 'bold'),
                            padx=5, corner_radius=50, fg_color='green')
        text.place(x=5, y=0)
        self.add = 0

    def create_task(self, day_index, task_index):
        task_frame = ctk.CTkFrame(master=self.day_frame, height=35, width=760, fg_color='#110F13')
        task_frame.place(y=60 + self.add, x=390, anchor='center')
        task_name = ctk.CTkLabel(master=task_frame, text=f'{task_list[j]}', padx=5, font=('Calibri', 15, 'bold'))
        task_name.place(x=20, y=2.1)
        button_timer = tk.Button(master=task_frame, image=click_btn, borderwidth=0,
                                 bg="#110F13", activebackground='#110F13',
                                 border=0, command=lambda: set_timer(day_index, task_index))
        button_timer.place(x=100, y=1)
        tracked_time = ctk.CTkLabel(master=task_frame, text=f'{time_list[j]}', padx=5, font=('Calibri', 15, 'bold'))
        tracked_time.place(x=135, y=2.1)
        lista_tempos.append(tracked_time)
        # x=40 e y=5
        self.add += 50


habitus = Create()
for i in range(0, 7):
    habitus.create_day(i)
    for j in range(0, 5):
        habitus.create_task(i, j)


root.mainloop()
