import customtkinter as ctk
from isolacao import tipo_isolacao #tabela com os dados da NBR5410


janela = ctk.CTk() #criar a nossa janela principal


#Configurando a janela principal
janela._set_appearance_mode('light') #Mudar tema da janela para dark

#janela.geometry("500x850") #Configurando o tamanho da janela principal

janela.title("Validação de disjuntor conforme NBR5410") #Configurando o título

janela.maxsize(width=600,height=800) #máximo que o usuario pode extender manualmente
janela.minsize(width=500,height=300) #mínimo que o usuario pode extender manualmente




#Execução de códigos para deixar a janela centralizada na tela
#Define a largura e a altura da janela
largura_janela=500
altura_janela=600

#Obtem a largura e a altura da tela do COMPUTADOR
largura_tela=janela.winfo_screenwidth()
altura_tela=janela.winfo_screenheight()

#Calcula a posição da janela para centraliza-la na tela
pos_x=(largura_tela//2)-(largura_janela//2)
pos_y=(altura_tela//2)-(altura_janela//2)

#Definindo a posição da janela na tela do computador
janela.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))



#Configurações dos menus
fg_color_v="blue" #cor da parte onde aparece os dados
button_color_v="blue" #cor da parte onde seleciona os dados
button_hover_color_v="white" #cor quando se passa o mouse por cima
dropdown_fg_color_v="blue" #cor de fundo da lista do menu
dropdown_text_color_v="black" #cor do texto da lista do menu
dropdown_hover_color_v="white" #cor quando se passa o mouse por cima
anchor_v="center"



def metodo_instalacao(escolha):
    pass

def condutores_instalacao(escolha):
    pass  

def isolacao_instalacao(escolha):
    pass
    
def secao_instalacao(escolha):
    pass
   
def disjuntor_instalacao(escolha):
    pass


ctk.CTkLabel(janela, text="Validação do disjuntor para condutores de cobre \n segundo a NBR5410:2004 ", font=("arial bold",18),bg_color='#ebebeb',text_color='black').pack(pady=10)


#Método de instalação
ctk.CTkLabel(janela, text="Método de instalação: ", font=("arial bold",14),bg_color='#ebebeb',text_color='black').pack()
metodo_var=ctk.StringVar(value="")

metodo= ctk.CTkOptionMenu(janela, 
                  values=["A1","A2","B1","B2","C","D","E","F"],
                  command=metodo_instalacao,
                  variable=metodo_var,
                  width=150, #largura do botão de menu
                  height=30, #altura do botão de menu
                  corner_radius=20,#arredondamento do botão de menu
                  fg_color=fg_color_v, #cor da parte onde aparece os dados
                  button_color=button_color_v, #cor da parte onde seleciona os dados
                  button_hover_color=button_hover_color_v,#cor quando se passa o mouse por cima
                  dropdown_fg_color=dropdown_fg_color_v,#cor de fundo da lista do menu
                  dropdown_text_color=dropdown_text_color_v,#cor do texto da lista do menu
                  dropdown_font=("arial bold",15), #tipo de fonte e tamanho do menu
                  dropdown_hover_color=dropdown_hover_color_v, #cor quando se passa o mouse dentro do menu
                  font=("arial bold",15), #fonte do texto
                  anchor=anchor_v, #alinhamento do texto
                  bg_color='#ebebeb',
                  
                  ) 
metodo.pack(pady=5) #Posicionamento do menu





#Número de condutores energizados
ctk.CTkLabel(janela, text="Quantidade de condutores energizados: ", font=("arial bold",14),bg_color='#ebebeb',text_color='black').pack()
condutores_var=ctk.StringVar(value="")

condutores= ctk.CTkOptionMenu(janela, 
                  values=["2","3"],
                  command=condutores_instalacao,
                  variable=condutores_var,
                  width=150, #largura do botão de menu
                  height=30, #altura do botão de menu
                  corner_radius=20,#arredondamento do botão de menu
                  fg_color=fg_color_v, #cor da parte onde aparece os dados
                  button_color=button_color_v, #cor da parte onde seleciona os dados
                  button_hover_color=button_hover_color_v,#cor quando se passa o mouse por cima
                  dropdown_fg_color=dropdown_fg_color_v,#cor de fundo da lista do menu
                  dropdown_text_color=dropdown_text_color_v,#cor do texto da lista do menu
                  dropdown_font=("arial bold",15), #tipo de fonte e tamanho do menu
                  dropdown_hover_color=dropdown_hover_color_v, #cor quando se passa o mouse dentro do menu
                  font=("arial bold",15),
                  anchor=anchor_v,
                  bg_color='#ebebeb',
                  ) 
condutores.pack(pady=5) #Posicionamento do menu



#Tipo de isolação
ctk.CTkLabel(janela, text="Tipo de isolação: ", font=("arial bold",14),bg_color='#ebebeb',text_color='black').pack()
isolacao_var=ctk.StringVar(value="")

isolacao= ctk.CTkOptionMenu(janela, 
                  values=["PVC","XLPE"],
                  command=isolacao_instalacao,
                  variable=isolacao_var,
                  width=150, #largura do botão de menu
                  height=30, #altura do botão de menu
                  corner_radius=20,#arredondamento do botão de menu
                  fg_color=fg_color_v, #cor da parte onde aparece os dados
                  button_color=button_color_v, #cor da parte onde seleciona os dados
                  button_hover_color=button_hover_color_v,#cor quando se passa o mouse por cima
                  dropdown_fg_color=dropdown_fg_color_v,#cor de fundo da lista do menu
                  dropdown_text_color=dropdown_text_color_v,#cor do texto da lista do menu
                  dropdown_font=("arial bold",15), #tipo de fonte e tamanho do menu
                  dropdown_hover_color=dropdown_hover_color_v, #cor quando se passa o mouse dentro do menu
                  font=("arial bold",15),
                  anchor=anchor_v,
                  bg_color='#ebebeb',
                  ) 
isolacao.pack(pady=5) #Posicionamento do menu






#Seção nominal
ctk.CTkLabel(janela, text="Seção nominal: ", font=("arial bold",14),bg_color='#ebebeb',text_color='black').pack()
secao_var=ctk.StringVar(value="")

secao= ctk.CTkOptionMenu(janela, 
                  values=["0.5", "0.75", "1", "1.5", "2.5", "4", "6", "10", "16", "25", "35", "50", "70", "95", "120", "150"],
                  command=secao_instalacao,
                  variable=secao_var,
                  width=150, #largura do botão de menu
                  height=30, #altura do botão de menu
                  corner_radius=20,#arredondamento do botão de menu
                  fg_color=fg_color_v, #cor da parte onde aparece os dados
                  button_color=button_color_v, #cor da parte onde seleciona os dados
                  button_hover_color=button_hover_color_v,#cor quando se passa o mouse por cima
                  dropdown_fg_color=dropdown_fg_color_v,#cor de fundo da lista do menu
                  dropdown_text_color=dropdown_text_color_v,#cor do texto da lista do menu
                  dropdown_font=("arial bold",15), #tipo de fonte e tamanho do menu
                  dropdown_hover_color=dropdown_hover_color_v, #cor quando se passa o mouse dentro do menu
                  font=("arial bold",15),
                  anchor=anchor_v,
                  bg_color='#ebebeb',
                  ) 
secao.pack(pady=5) #Posicionamento do menu




#Disjuntor
ctk.CTkLabel(janela, text="Disjuntor: ", font=("arial bold",14),bg_color='#ebebeb',text_color='black').pack()
disjuntor_var=ctk.StringVar(value="")

disjuntor= ctk.CTkOptionMenu(janela, 
                  values=["6", "10", "16", "20", "25", "32", "40", "50", "63", "70", "80", "100", "125", "150", "160", "175","200","225","250"],
                  command=disjuntor_instalacao,
                  variable=disjuntor_var,
                  width=150, #largura do botão de menu
                  height=30, #altura do botão de menu
                  corner_radius=20,#arredondamento do botão de menu
                  fg_color=fg_color_v, #cor da parte onde aparece os dados
                  button_color=button_color_v, #cor da parte onde seleciona os dados
                  button_hover_color=button_hover_color_v,#cor quando se passa o mouse por cima
                  dropdown_fg_color=dropdown_fg_color_v,#cor de fundo da lista do menu
                  dropdown_text_color=dropdown_text_color_v,#cor do texto da lista do menu
                  dropdown_font=("arial bold",15), #tipo de fonte e tamanho do menu
                  dropdown_hover_color=dropdown_hover_color_v, #cor quando se passa o mouse dentro do menu
                  font=("arial bold",15),
                  anchor=anchor_v,
                  bg_color='#ebebeb',
                  ) 
disjuntor.pack(pady=5) #Posicionamento do menu




#Função relativa ao botão da validação
def button_event():
    
    #Realizada a aquisição do dados digitados
    metodo_v=str(metodo.get())
    condutores_v=int(condutores.get())
    isolacao_v=str(isolacao.get())
    secao_v=float(secao.get())
    disjuntor_v=str(disjuntor.get())
    
    #Chamando a lista da NBR5410
    lista=tipo_isolacao(isolacao_v)


    #Adaptação dos índices de busca de acordo com o método de instalação
    aux=100
   
    if metodo_v=="A1":
        if  condutores_v==2:
            aux=0
        else:
            aux=1
    
    if metodo_v=="A2":
        if  condutores_v==2:
            aux=2
        else:
            aux=3
    
    if metodo_v=="B1":
        if  condutores_v==2:
            aux=4
        else:
            aux=5
    
    if metodo_v=="B2":
        if  condutores_v==2:
            aux=6
        else:
            aux=7

    if metodo_v=="C":
        if  condutores_v==2:
            aux=8
        else:
            aux=9
    
    if metodo_v=="D":
        if  condutores_v==2:
            aux=10
        else:
            aux=11
    
    if metodo_v=="E":
        if  condutores_v==2:
            aux=12
        else:
            aux=13
    
    if metodo_v=="F":
        if  condutores_v==2:
            aux=14
        else:
            aux=15
       
    
    #Lógica da comparação do disjutor com a capacidade do condutor
    if lista[secao_v][aux]>=int(disjuntor_v):
        text_var.set(f"O disjuntor {disjuntor_v}A está ok \n A capacidade do condutor de {secao_v} é de: {lista[secao_v][aux]}A ")
        label.configure(fg_color="green")
    else:
        text_var.set(f"O disjuntor {disjuntor_v}A não está ok \n A capacidade do condutor de {secao_v} é de: {lista[secao_v][aux]}A ")
        label.configure(fg_color="red")


#Criação do botão da validação
button=ctk.CTkButton(janela,text="Validar", command=button_event,font=("arial bold",20),text_color="black",bg_color='#ebebeb')
button.pack(pady=20)



#Label para mostrar o resultado da análise
text_var= ctk.StringVar()
label=ctk.CTkLabel(janela,textvariable=text_var,width=150,height=50,fg_color=("yellow"),text_color="black",corner_radius=8,font=("arial bold",20),bg_color='#ebebeb')
label.pack(pady=15)






janela.mainloop()
