from views import *

from tkinter import *
from tkinter import Tk, ttk

# Import Pillow
from PIL import Image,  ImageTk

# Import Tkinter ProgressBar
from tkinter.ttk import Progressbar

#Import Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


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


# Annual Goal Bar
def show_percentage():
    annual_goal_label = Label(frame_middle, text="Meta anual", height=1, anchor=NW, font=('Verdana 12'), bg=color_white,fg=color_value)
    annual_goal_label.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background = '#CDEB8B')
    style.configure("TProgressbar", thickness = 20)
    bar = Progressbar(frame_middle, length=180, style='black.Horizontal.TProgressbar')
    
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50

    percentage_label = Label(frame_middle, text="{:,.2f} %".format(valor), anchor=NW, font=('Verdana 12'), bg=color_white,fg=color_value)
    percentage_label.place(x=200, y=35)


# Monthly Income Graphic

def show_monthly_income():
    month_list = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
    
    values_list = [0, 1.87, 117.91, 0.17, 13.99, 0.12, 238.98, 49,99, 27.6, 115.55, 320]

    #draw figure and set an axis
    figure = plt.figure(figsize=(4, 3.45), dpi=60)
    
    #add axis
    ax = figure.add_subplot(111)

    #set bars to axis
    ax.bar(month_list, values_list, color=colors, width=0.9)


    c = 0
    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5,
            str("{:,.0f}".format(values_list[c])),fontsize=17, fontstyle='italic', verticalalignment='bottom')
        c += 1

    ax.set_xticklabels(month_list, fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figure, frame_middle)
    canva.get_tk_widget().place(x=10, y=70)
     

show_percentage()
show_monthly_income()

window_main.mainloop()