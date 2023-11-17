import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

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

main_frame = ctk.CTkScrollableFrame(master=root)
main_frame.pack(fill='both', expand=True)

left_sidebar_frame = ctk.CTkFrame(master=main_frame, width=sidebar_width, height=500, fg_color='#373838')
left_sidebar_frame.pack(side='left', fill='y')

button_expand = ctk.CTkButton(master=left_sidebar_frame, text="Open", command=expand, width=75, fg_color='#00DF24')
button_expand.place(x=10, y=10)

right_sidebar_frame = ctk.CTkFrame(master=main_frame, width=sidebar_width, height=500, fg_color='#373838')
right_sidebar_frame.pack(side='right', fill='y')

click_btn = Image.open('D:\Python_Projetos\Productivity_Analyser-main\Group 5.png')
click_btn = click_btn.resize((30, 30))
click_btn = ImageTk.PhotoImage(click_btn)

day_list = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
task_list = ['FMC', 'Cálculo', 'ITP', 'Currículo', 'Cursos', 'Leetcode', 'Leitura']

day_frame = ctk.CTkFrame(master=main_frame, height=300, width=1000, fg_color='#373838')
day_frame.lower()
day_frame.pack(padx=10, pady=10)
text = ctk.CTkLabel(master=day_frame, text="Segunda", font=('Calibri', 15, 'bold'),
                    padx=5, corner_radius=50,fg_color='green')
text.place(x=5, y=0)

add = 0
for i in range(0, 5):
    task_frame = ctk.CTkFrame(master=day_frame, height=35, width=800, fg_color='#110F13')
    task_frame.place(y=60+add, x=420, anchor='center')

    task_name = ctk.CTkLabel(master=task_frame, text='FMC', padx=5, font=('Calibri', 15, 'bold'))
    task_name.place(x=20, y=2.1)

    button_timer = tk.Button(master=task_frame, image=click_btn, borderwidth=0,
                       bg="#110F13", activebackground='#110F13',
                       border=0)
    button_timer.place(x=100, y=1)

    tracked_time = ctk.CTkLabel(master=task_frame, text='6:10:00', padx=5, font=('Calibri', 15, 'bold'))
    tracked_time.place(x=135, y=2.1)
    #x=40 e y=5
    add += 50

"""
"""

root.mainloop()
