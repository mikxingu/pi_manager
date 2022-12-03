import matplotlib.pyplot as plt
import numpy as np

month_list = ['Out', 'Nov', 'Dez']

stock_list = [0, 46.84, 323.52]
fii_list = [27.6, 68.36, 26.4]

width = 0.35

    # draw figure and set an axis
    # figure = plt.figure(figsize=(4, 3.45), dpi=60)

fig, ax = plt.subplots()

x = np.arange(len(month_list))

ax.bar(month_list, stock_list, width, label="Proventos", color='#FAC02D')
ax.bar(month_list, fii_list, width, bottom=stock_list,
        label="FIIs", color='#E14B19')

# ax.set_xticks(x, month_list)

ax.set_ylabel('Ativos')
ax.set_title('Ganho Mensal')
ax.legend()
plt.show()
