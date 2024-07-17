# Importando a biblioteca tkinter
from tkinter import * # Importando todos os componentes do módulo Tkinter para o namespace atual
from tkinter import ttk # Importando o submódulo ttk (conjunto de widgets) do pacote tkinter

# Configurando uma janela do tkinter
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#4065a1"  # vermelha

janela = Tk() # Criando uma instância da classe Tk (que representa a janela principal da aplicação Tkinter)
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co1)

# Dividindo a janela em dois frames
# Criando um frame dentro da janela principal da aplicação (janela) e configurando a sua largura, altura, cor de fundo, padding e estilo da borda
frame_cima = Frame(janela, width=295, height=50, bg=co1, pady=0, padx=0, relief="flat")
# Posicionando o frame na janela principal usando o grid, colocando-o na linha 0 e coluna 0 e expandindo-o em todas as direções (NSEW) para preencher a célula
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=200, bg=co1, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)

style = ttk.Style(janela) # Criando uma instância da classe Style da biblioteca ttk e associando à janela principal (janela)
style.theme_use("clam")

# Frame de cima
# Criando o label dentro do frame_cima com configurações adicionais como a definição do texto do rótulo (text), o alinhamento do texto (anchor), a definição da fonte (font) e da cor do texto (fg)
app_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 16 bold'), bg=co1, fg=co0)
# Posicionando o label nas coordenadas (0,2) dentro do contêiner pai utilizando o método place
app_nome.place(x=0, y=2)

app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# Frame de baixo
l_peso = Label(frame_baixo, text="Insira seu peso", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_peso.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text="Insira sua altura", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_altura.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=85)

# Função para realizar o cálculo
def calcular():
    try:
        # Obtendo o valor do campo de entrada (e_peso), convertendo para float e armazenando na variável peso
        peso = float(e_peso.get())
        # Obtendo o valor do campo de entrada (e_altura), convertendo para float, elevando ao quadrado e armazenando na variável altura
        altura = float(e_altura.get()) ** 2
        resultado = peso / altura

        if resultado < 18.6:
            l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
        elif resultado >= 18.5 and resultado < 24.9:
            l_resultado_texto['text'] = "Seu IMC é: Normal"
        elif resultado >= 25 and resultado < 29.9:
            l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
        else:
            l_resultado_texto['text'] = "Seu IMC é: Obesidade"

        l_resultado['text'] = "{:.2f}".format(resultado)
    except ValueError:
        l_resultado_texto['text'] = "Entrada inválida"

# Botão calcular
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=34, height=1, overrelief=SOLID, bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

# Iniciando o loop principal da janela
janela.mainloop()

# Projeto de estudo!
