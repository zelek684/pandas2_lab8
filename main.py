import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

# #zadanie1
# imie = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imie, header=0)
# dziecko = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(dziecko)
# dziecko.plot()
# plt.xticks(np.arange(2000, 2018, step=1))
# plt.xticks(rotation=90)
# plt.show()
#
#zadanie2

# imie = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imie, header=0)
# dziecko = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(dziecko)
# wykres = dziecko.plot.bar()
# wykres.legend()
# plt.title('Wykres')
# plt.show()

# plt.plot([1,2,3,4])
# plt.ylabel('liczby')
# plt.show()


# plt.plot([1,2,3,4], [1,4,9,16], 'ro-')
#
# plt.axis([0,6,0,20])
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16], 'r')
# plt.plot([1,2,3,4],[1,4,9,16], 'o')
#
# plt.axis([0,6,0,20])
# plt.show()


# t = np.arange(0, 5., 0.2)
#
# plt.plot(t, t, 'r--',t, t**2, 'bs', t, t**3,'g^')
# plt.show()


# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='postać liniowa')
# plt.plot(x, x**2, label='postać kwadrotowa')
# plt.plot(x, x**3, label='postać sześcienna')
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
#
# plt.title('PROSTY WYKRES')
#
# plt.legend()
# plt.show()

# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label='sin(x)')
#
# plt.xlabel('wartosc x')
# plt.ylabel('sin(x)')
#
# plt.title('wykres sin(x)')
#
# plt.legend()
# plt.show()

# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1,y1, '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()