import customtkinter as ctk

def expand():
    global sidebar_width
    pos_y = root.winfo_screenheight()

    if sidebar_width == 150:  # Verifica se a barra lateral está totalmente recolhida
        while sidebar_width < 250:  # Expande gradualmente a barra lateral
            sidebar_width += 10
            sidebar_frame.place_configure(width=sidebar_width, height=pos_y)
            root.update()
            root.after(50)
    else:  # Caso a barra lateral já esteja expandida, recolhe
        while sidebar_width > 150:
            sidebar_width -= 10
            sidebar_frame.place_configure(width=sidebar_width, height=pos_y)
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

sidebar_width = 150

main_frame = ctk.CTkFrame(master=root)
main_frame.pack(side='right', fill='both', expand=True)

sidebar_frame = ctk.CTkFrame(master=root, width=150, fg_color='#373838')
sidebar_frame.pack(side='left', fill='both')

button_expand = ctk.CTkButton(master=sidebar_frame, text="Expansão de Domínio", command=expand)
button_expand.place(x=10, y=10)
button_expand.pack(padx=5, pady=5)

track_frame = ctk.CTkFrame(master=main_frame, height=100, width=1000, fg_color='#373838')
track_frame.pack(padx=20, pady=10)

root.mainloop()
