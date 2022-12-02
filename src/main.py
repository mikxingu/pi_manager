from views import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image,  ImageTk

################# cores ###############
color_black = "#2e2d2b"  # Preta
color_white = "#feffff"  # branca
color_green = "#4fa882"  # verde
color_value = "#38576b"  # valor
color_text = "#403d3d"   # letra
color_profit = "#e06636"   # - profit
color_blue = "#038cfc"   # azul
color_greeny = "#3fbfb9"   # verde
color_greeeny = "#263238"   # + verde
color_greeeeny = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']


# Main Window 
window_main = Tk()
window_main.title('PI Manager')
window_main.geometry('900x650')
window_main.configure(background=color_greeeeny)
window_main.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window_main)
style.theme_use('clam')

## Frames for window division
frame_upper = Frame(window_main, width=1043, height=50, bg=color_white, relief="flat")
frame_upper.grid(row=0, column=0)

frame_middle = Frame(window_main, width=1043, height=361, bg=color_white, pady=20, relief="raised")
frame_middle.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_lower = Frame(window_main, width=1043, height=300, bg=color_white, relief="flat")
frame_lower.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)



### Upper Frame Config

# Open Logo
app_image = Image.open('./src/img/profit.png')
app_image = app_image.resize((45, 45))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(frame_upper, image=app_image, text= " PI Manager - Renda Passiva", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=color_white, fg=color_value)
app_logo.place(x=0, y=0)




window_main.mainloop()