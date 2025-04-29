import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calcular_diferenca():
    try:
        data1 = datetime.strptime(entrada_data1.get(), "%d/%m/%Y")
        data2 = datetime.strptime(entrada_data2.get(), "%d/%m/%Y")
        dias = abs((data2 - data1).days)
        resultado.set(f"Diferenças: {dias} dias")
    except:
        messagebox.showerror("Erro", "Digite as datas no formato dd/mm/aaaa")

def somar_dias():
    try:
        data = datetime.strptime(entrada_data_somar.get(), "%d/%m/%Y")
        dias = int(entrada_qtd_somar.get())
        nova_data = data + timedelta(days=dias)
        resultado.set(f"Nova data: {nova_data.strftime('%d/%m/%Y')}")
    except:
        messagebox.showerror("Erro", "Verifique os campos e tente novamente")

def subtrair_dias():
    try:
        data = datetime.strptime(entrada_data_subtrair.get(), "%d/%m/%Y")
        dias = int(entrada_qtd_subtrair.get())
        nova_data = data - timedelta(days=dias)
        resultado.set(f"Nova data: {nova_data.strftime('%d/%m/%Y')}")
    except:
        messagebox.showerror("Error", "Verifique os campos e tente novamente.")

def dia_da_semana():
    try:
        data = datetime.strptime(entrada_data_semana.get(), "%d/%m/%Y")
        dia_semana = data.strftime("%A")
        dias_pt = {
            "Monday": "Segunda-feira",
            "Tuesday": "Terça-feira",
            "Wednesday": "Quarta-feira",
            "Thursday": "Quinta-feira",
            "Friday": "Sexta-feira",
            "Saturday": "Sabádo",
            "Sunday": "Domingo",
        }

        resultado.set(f"Dia da semana: {dias_pt[dia_semana]}")
    except:
        messagebox.showerror("Erro", "Digite a data no formato dd/mm/aaaa")

janela = tk.Tk()
janela.title("Calculadora de Datas")
janela.geometry("400x600")

resultado = tk.StringVar()

tk.Label(janela, text="Diferença entre datas").pack()
entrada_data1 = tk.Entry(janela)
entrada_data1.pack()
entrada_data1.insert(0, "dd/mm/aaaa")
entrada_data2 = tk.Entry(janela)
entrada_data2.pack()
entrada_data2.insert(0, "dd/mm/aaaa")
tk.Button(janela, text="Calcular Diferença", command=calcular_diferenca).pack(pady=5)

tk.Label(janela, text="Somar Dias").pack()
entrada_data_somar = tk.Entry(janela)
entrada_data_somar.pack()
entrada_data_somar.insert(0, "dd/mm/aaaa")
entrada_qtd_somar = tk.Entry(janela)
entrada_qtd_somar.pack()
entrada_qtd_somar.insert(0, "Quantos dias")
tk.Button(janela, text="Somar Dias", command=somar_dias).pack(pady=5)

tk.Label(janela, text="Subtrair Dias").pack()
entrada_data_subtrair = tk.Entry(janela)
entrada_data_subtrair.pack()
entrada_data_subtrair.insert(0, "dd/mm/aaaa")
entrada_qtd_subtrair = tk.Entry(janela)
entrada_qtd_subtrair.pack()
entrada_qtd_subtrair.insert(0, "Quantos dias")
tk.Button(janela, text="Subtrair Dias", command=subtrair_dias).pack(pady=5)

tk.Label(janela, text="Descobrir dia da semana").pack()
entrada_data_semana = tk.Entry(janela)
entrada_data_semana.pack()
entrada_data_semana.insert(0, "dd/mm/aaaa")
tk.Button(janela, text="Ver Dia da Semana", command=dia_da_semana).pack(pady=5)

tk.Label(janela, textvariable=resultado, font=("Arial", 12), fg="blue").pack(pady=5)

janela.mainloop()
