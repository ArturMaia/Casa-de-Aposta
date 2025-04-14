import tkinter as tk
from tkinter import ttk
import random

# Funções de geração de números
def gerar_mega_sena():
    return sorted(random.sample(range(1, 61), 6))

def gerar_quina():
    return sorted(random.sample(range(1, 81), 5))

def gerar_lotofacil():
    return sorted(random.sample(range(1, 26), 15))

def gerar_viva_sorte():
    return sorted(random.sample(range(1, 61), 6))

def gerar_dupla_sena():
    sorteios = [sorted(random.sample(range(1, 51), 6)) for _ in range(2)]
    return sorteios

def gerar_timemania():
    numeros = sorted(random.sample(range(1, 81), 7))
    time = random.choice(range(1, 81))  # Escolhe 1 time aleatório
    return numeros, time

def gerar_loteca():
    return sorted(random.sample(range(1, 26), 14))

# Função para exibir o sorteio no label
def exibir_resultado():
    tipo = escolha_loteria.get()
    
    if tipo == "Mega-Sena":
        resultado = gerar_mega_sena()
        resultado_texto = f"Mega-Sena: {resultado}"
    elif tipo == "Quina":
        resultado = gerar_quina()
        resultado_texto = f"Quina: {resultado}"
    elif tipo == "Lotofácil":
        resultado = gerar_lotofacil()
        resultado_texto = f"Lotofácil: {resultado}"
    elif tipo == "Viva Sorte":
        resultado = gerar_viva_sorte()
        resultado_texto = f"Viva Sorte: {resultado}"
    elif tipo == "Dupla Sena":
        resultado = gerar_dupla_sena()
        resultado_texto = f"Dupla Sena: {resultado[0]} / {resultado[1]}"
    elif tipo == "Timemania":
        resultado = gerar_timemania()
        resultado_texto = f"Timemania: {resultado[0]} - Time: {resultado[1]}"
    elif tipo == "Loteca":
        resultado = gerar_loteca()
        resultado_texto = f"Loteca: {resultado}"
    else:
        resultado_texto = "Escolha uma loteria."

    texto_resultado.delete(1.0, tk.END)  # Limpar o conteúdo atual da Text box
    texto_resultado.insert(tk.END, resultado_texto)  # Inserir o novo resultado

# Criando a janela principal
janela = tk.Tk()
janela.title("Gerador de Números de Loteria")
janela.configure(bg="#2E3B47")  # Cor de fundo agradável

# Função para ajustar a geometria da janela conforme o tamanho da tela
def ajustar_tamanho():
    largura = janela.winfo_screenwidth()
    altura = janela.winfo_screenheight()

    if largura < altura:  # Modo vertical
        janela.geometry("720x1520")  # Ajustando para a resolução vertical
    else:  # Modo horizontal
        janela.geometry("1520x720")  # Ajustando para a resolução horizontal

# Ajusta o tamanho da janela ao iniciar
ajustar_tamanho()

# Título
titulo = tk.Label(janela, text="Escolha o tipo de loteria:", font=("Arial", 14), bg="#2E3B47", fg="white", anchor="center", width=40)
titulo.pack(pady=(50, 20))  # Aumentando o padding superior para garantir mais espaço

# Opções de loterias
escolha_loteria = tk.StringVar(janela)
escolha_loteria.set("Mega-Sena")  # Definindo o valor inicial

# Menu de escolha de loteria (usando ttk.Combobox para um visual mais bonito)
menu_loteria = ttk.Combobox(janela, textvariable=escolha_loteria, values=["Mega-Sena", "Quina", "Lotofácil", "Viva Sorte", "Dupla Sena", "Timemania", "Loteca"], state="readonly", font=("Arial", 12), width=15)
menu_loteria.pack(pady=10)

# Botão para gerar números
botao_gerar = tk.Button(janela, text="Gerar Números", command=exibir_resultado, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", padx=20, pady=10)
botao_gerar.pack(pady=20)

# Label para exibir os resultados com Text box que permite rolar e expandir
texto_resultado = tk.Text(janela, font=("Arial", 14), bg="#2E3B47", fg="#f1f1f1", width=40, height=6, wrap=tk.WORD, bd=2, relief="solid")
texto_resultado.pack(pady=10, fill="both", expand=True)  # Expande para ocupar mais espaço

# Criando o redimensionamento dinâmico
janela.grid_rowconfigure(0, weight=1)  # Ajuste a linha 0
janela.grid_columnconfigure(0, weight=1)  # Ajuste a coluna 0

# Rodar a interface
janela.mainloop()

