# Importando as Biblíotecas
import tkinter as tk
import math

# Configurando os botões
botao_config = {
    "bg": "#242742",
    "fg": "#D1D2DE",
    "font": ("Consolas bold", 12),
    "height": "2",
    "width": "7",
    "relief": "flat",
    "activebackground": "#313454"
}

digitos = ["√", "x²", "sin", "cos", "sin-¹", "cos-¹", "tan", "tan-¹", "n!", "π", "C"]

deg = 1
inversa_deg = 1
cnt = 0


class Calculadora:
    def __init__(self, master):

        self.botoes = [
            ["√", "x²", "**", "(", ")", "/"],
            ["sin", "cos", "7", "8", "9", "+"],
            ["sin-¹", "cos-¹", "4", "5", "6", "-"],
            ["tan", "tan-¹", "1", "2", "3", "*"],
            ["n!", "π", ".", "0", "=", "C"],
        ]
        self.master = master

        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()

        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()

        self.output = tk.Entry(self.displayFrame, width=37, relief="sunken", bd=3, font=("Consolas bold", 17),
                               fg="#c9c9c5", bg="#242742")
        self.output.grid(row=0, column=0)

        self.converte = tk.Button(self.displayFrame, botao_config, width=3, height=0, text="DEG", bg="#E35124",
                                  command=self.degreesradians)
        self.converte.grid(row=0, column=1)

        self.criarbotoes()

    def criarbotoes(self):

        for linha in self.botoes:
            for texto in linha:
                b = tk.Button(self.buttonsFrame, botao_config, text=texto, command=lambda x=texto: self.acao_botoes(x))
                b.grid(row=self.botoes.index(linha), column=linha.index(texto))

    def acao_botoes(self, texto):
        global deg
        global inversa_deg
        if texto != "=":
            if texto not in digitos:
                self.output.insert('end', texto)
            else:
                if texto == "√":
                    self.add_valor(math.sqrt(eval(self.output.get())))
                elif texto == "n!":
                    self.add_valor(math.factorial(eval(self.output.get())))
                elif texto == "π":
                    self.add_valor(3.1415926535897932)
                elif texto == "C":
                    self.add_valor("")
                elif texto == "sin":
                    self.add_valor(math.sin(eval(self.output.get()) * deg))
                elif texto == "cos":
                    self.add_valor(math.cos(eval(self.output.get()) * deg))
                elif texto == "tan":
                    self.add_valor(math.tan(eval(self.output.get()) * deg))
                elif texto == "x²":
                    self.add_valor(eval(self.output.get()) ** 2)
                elif texto == "sin-¹":
                    self.add_valor(math.asin(eval(self.output.get())) * inversa_deg)
                elif texto == "cos-¹":
                    self.add_valor(math.acos(eval(self.output.get())) * inversa_deg)
                elif texto == "tan-¹":
                    self.add_valor(math.atan(eval(self.output.get())) * inversa_deg)
        else:
            self.add_valor(eval(self.output.get()))

    def add_valor(self, valor):
        self.output.delete(0, 'end')
        self.output.insert('end', valor)

    def degreesradians(self):
        global deg
        global inversa_deg
        global cnt

        if cnt == 0:
            deg = math.pi / 180
            inversa_deg = 180 / math.pi
            self.converte['text'] = "RAD"
            cnt = 1
        else:
            deg = 1
            inversa_deg = 1
            self.converte['text'] = "DEG"
            cnt = 0


raiz = tk.Tk()

Calculadora(raiz)

raiz.mainloop()
