import customtkinter as ctk
from tkinter import ttk
import math
import numpy as np
from padrao import padrao_cemig #Base de dados da CEMIG


# Função para centralizar a janela
def centralize_window(janela, largura_janela, altura_janela):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))



class TreeViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CEMIG")


        # Configuração da janela principal
        self.root._set_appearance_mode('light')
        self.root.maxsize(width=2000, height=2000)
        self.root.minsize(width=500, height=300)
        centralize_window(self.root, 1350, 600)

        
        # Configura o frame principal
        main_frame = ctk.CTkFrame(root)
        main_frame.pack(fill=ctk.BOTH, expand=True)
        

        # Frame para TreeView
        tree_frame = ctk.CTkFrame(main_frame)
        tree_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        #Configuração da TreeView
        style = ttk.Style()
        style.configure("Custom.Treeview.Heading", font=('Arial Bold', 10), padding=[10,15])
        style.configure("Custom.Treeview", font=('Arial', 10))


        # Configura os elementos da Treeview
        self.tree = ttk.Treeview(tree_frame, columns=("Classificacao", "PotenciaMinima", "PotenciaMaxima", "RamalEntrada", "Aterramento", "Caixa", "Disjuntor"), show="headings",height=20, style="Custom.Treeview")
        self.tree.heading("Classificacao", text="Classificação")
        self.tree.heading("PotenciaMinima", text="Potência mínima\n           (kVA)")
        self.tree.heading("PotenciaMaxima", text="Potência máxima \n          (kVA)")
        self.tree.heading("RamalEntrada", text="Ramal de entrada\n         (mm²)")
        self.tree.heading("Aterramento", text="Aterramento\n      (mm²)")
        self.tree.heading("Caixa", text="Tipo de caixa", anchor='center')
        self.tree.heading("Disjuntor", text="Disjuntor\n    (A)")
        self.tree.column("Classificacao", width=80, anchor='center')
        self.tree.column("Aterramento", width=90, anchor='center')
        self.tree.column("PotenciaMinima", width=100, anchor='center')
        self.tree.column("PotenciaMaxima", width=110, anchor='center')
        self.tree.column("RamalEntrada", width=120, anchor='center')
        self.tree.column("Caixa", width=80, anchor='center')
        self.tree.column("Disjuntor", width=60, anchor='center')
        self.tree.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        
        # Adiciona uma barra de rolagem vertical na TreeView
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=ctk.LEFT, fill=ctk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        
        # Frame para seleção de dados
        selection_frame = ctk.CTkFrame(main_frame)
        selection_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
        ctk.CTkLabel(selection_frame, text="Preencha os seguintes dados: ", font=("arial bold", 18), bg_color='#cfcfcf', text_color='black').pack(pady=10)

       
        #Criação do label e do menu de opções para classe de instalação
        ctk.CTkLabel(selection_frame, text="Classe da instalação: ", font=("arial bold", 14), bg_color='#cfcfcf', text_color='black').pack()
        classe_instalacao_var = ctk.StringVar(value="")
        classe_instalacao = ctk.CTkOptionMenu(selection_frame, 
                                              values=["Monofásico", "Monofásico Rural", "Bifásico", "Trifásico"],
                                              variable=classe_instalacao_var,
                                              width=150, height=30, corner_radius=20,
                                              fg_color="#ebebeb", button_color="#ebebeb", button_hover_color="white",
                                              dropdown_fg_color="#ebebeb", dropdown_text_color="black", dropdown_hover_color="blue",
                                              font=("arial bold", 15), anchor="center", bg_color='#cfcfcf', text_color="black")
        classe_instalacao.pack(pady=5, padx=5)

        
        #Criação do label e menu de opções para a tensão da instalação
        ctk.CTkLabel(selection_frame, text="Tensão fase-fase da rede: ", font=("arial bold", 14), bg_color='#cfcfcf', text_color='black').pack()
        tensao_var = ctk.StringVar(value="")
        tensao = ctk.CTkOptionMenu(selection_frame, 
                                    values=["127", "220"],
                                    variable=tensao_var,
                                    width=150, height=30, corner_radius=20,
                                    fg_color="#ebebeb", button_color="#ebebeb", button_hover_color="white",
                                    dropdown_fg_color="#ebebeb", dropdown_text_color="black", dropdown_hover_color="blue",
                                    font=("arial bold", 15), anchor="center", bg_color='#cfcfcf', text_color="black")
        tensao.pack(pady=5)

        
        # Criação do label e campo de entrada para o fator de sobrecarga
        ctk.CTkLabel(selection_frame, text="Fator de sobrecarga: ", font=("arial bold", 14), bg_color='#cfcfcf', text_color='black').pack()
        fator = ctk.CTkEntry(selection_frame, placeholder_text="1.X", width=150, height=30, border_width=2, corner_radius=10)
        fator.pack(pady=5)

        
        #Criação do label e do menu de opções para o tipo de inversor
        ctk.CTkLabel(selection_frame, text="Tipo de inversor: ", font=("arial bold", 14), bg_color='#cfcfcf', text_color='black').pack()
        inversor_var = ctk.StringVar(value="")
        inversor = ctk.CTkOptionMenu(selection_frame, 
                                      values=["Microinversor", "Inversor central"],
                                      variable=inversor_var,
                                      width=150, height=30, corner_radius=20,
                                      fg_color="#ebebeb", button_color="#ebebeb", button_hover_color="white",
                                      dropdown_fg_color="#ebebeb", dropdown_text_color="black", dropdown_hover_color="blue",
                                      font=("arial bold", 15), anchor="center", bg_color='#cfcfcf', text_color="black")
        inversor.pack(pady=5)


        # Função de validação do tipo de inversor setado na janela principal
        def button_event():
            
            classe_instalacao_get=classe_instalacao.get()
            tensao_get=tensao.get()
            inversor_get=inversor.get()
            fator_get=fator.get()
            
            
            #Verificando se todos os dados necessários foram setados
            if classe_instalacao_get!="" and tensao_get!="" and inversor_get!="" and fator_get!="":
                
                #Verifica se a classe e a tensão são compatíveis
                if (classe_instalacao_get=="Monofásico" and tensao_get=='220') or (classe_instalacao_get=="Bifásico" and tensao_get=='127') or (classe_instalacao_get=="Monofásico Rural" and tensao_get=='127') or (classe_instalacao_get=="Trifásico" and tensao_get=='127') or (classe_instalacao_get=="Bifásico" and tensao_get=='380') or (classe_instalacao_get=="Monofásico Rural" and tensao_get=='380') or (classe_instalacao_get=="Monofásico" and tensao_get=='380'):
                    
                    mensagem="Classe incompatível com o nível de tensão \n Por favor, tente novamente"
                    se_erro(mensagem)
                
                else:  
                    try: 
                        #O try verifica se o número digitado é um float
                        fator_get=float(fator_get)
                        if isinstance(fator_get,float):

                            #Controle do tipo de inversor
                            if inversor_get=="Inversor central":
                                se_inversor()
                            elif inversor_get=="Microinversor":
                                se_micro()
                    
                    except ValueError:
                        mensagem="Não foi digitado um número válido \n Por favor, tente novamente"
                        se_erro(mensagem)                   
            
            else:
                mensagem="Não foi setado todos os dados \n Por favor, tente novamente"
                se_erro(mensagem)



        #Função para abrir nova janela se for microinversor
        def se_micro():
        
            new_window = ctk.CTkToplevel()
            new_window.title("Dados dos Microinversores")
            new_window.resizable(False, False) #Impedir que o usuário redimensione a janela

            centralize_window(new_window, 400, 500) #Centralizando a janela do microinversor

            
            
            # Função de validação dos dados setados na tela de microinversor
            def button_event2():
                potencia_microinversor_get=potencia_microinversor.get()
                classe_microinversor_get=classe_microinversor.get()
                tensao_microinversor_get=tensao_microinversor.get()
                classe_instalacao_get=classe_instalacao.get()
                fator_get=fator.get()
                fator_get=float(fator_get)
                
                #Variáveis auxiliares para receberem a quantidade de microinversores
                quantidade_microinversorAB_get=""
                quantidade_microinversorBC_get=""
                quantidade_microinversorCA_get=""
                quantidade_microinversorAN_get=""
                quantidade_microinversorBN_get=""
                quantidade_microinversorCN_get=""

                #Conversão da quantidade de inversores para tipo int
                if quantidade_microinversorAB.get()!="":
                    quantidade_microinversorAB_get=int(quantidade_microinversorAB.get())
                if quantidade_microinversorBC.get()!="":
                    quantidade_microinversorBC_get=int(quantidade_microinversorBC.get())
                if quantidade_microinversorCA.get()!="":
                    quantidade_microinversorCA_get=int(quantidade_microinversorCA.get())
                if quantidade_microinversorAN.get()!="":
                    quantidade_microinversorAN_get=int(quantidade_microinversorAN.get())
                if quantidade_microinversorBN.get()!="":
                    quantidade_microinversorBN_get=int(quantidade_microinversorBN.get())
                if quantidade_microinversorCN.get()!="":
                    quantidade_microinversorCN_get=int(quantidade_microinversorCN.get())


                aux1= (quantidade_microinversorAB_get!="" or quantidade_microinversorBC_get!="" or quantidade_microinversorCA_get!="")
                aux2 = (quantidade_microinversorAN_get!="" or quantidade_microinversorBN_get!="" or quantidade_microinversorCN_get!="")

                #Verificando se a quantidade de inversores foi inserida de forma correta
                if not ((aux1 and aux2) or ((not aux1 and not aux2))):

                    #Verificando se todos os dados necessários foram setados
                    if potencia_microinversor_get!="" and classe_microinversor_get!="" and tensao_microinversor_get!="":
                        
                        #Verifica se a classe e a tensão são compatíveis
                        if (classe_microinversor_get=="Monofásico" and tensao_microinversor_get=='220') or (classe_microinversor_get=="Bifásico" and tensao_microinversor_get=='127') or (classe_microinversor_get=="Trifásico" and tensao_microinversor_get=='127'):
                            
                            mensagem="Classe incompatível com o nível de \n tensão de operação \n Por favor, tente novamente"
                            se_erro(mensagem)
                        
                        else:  
                            
                            if (classe_microinversor_get=="Monofásico" and classe_instalacao_get=="Monofásico" ) or (classe_microinversor_get=="Monofásico" and classe_instalacao_get=="Monofásico Rural") or (classe_microinversor_get=="Monofásico" and classe_instalacao_get=="Bifásico") or (classe_microinversor_get=="Monofásico" and classe_instalacao_get=="Trifásico") or (classe_microinversor_get=="Bifásico" and classe_instalacao_get=="Monofásico Rural") or (classe_microinversor_get=="Bifásico" and classe_instalacao_get=="Bifásico") or (classe_microinversor_get=="Bifásico" and classe_instalacao_get=="Trifásico") or (classe_microinversor_get=="Trifásico" and classe_instalacao_get=="Trifásico"):
                                try: 
                                    #O try verifica se o número digitado é um float
                                    potencia_microinversor_get=float(potencia_microinversor_get)
                                    if isinstance(potencia_microinversor_get,float):
                                        tensao_microinversor_get=float(tensao_microinversor_get)

                                        #Calculo das correntes
                                        if (classe_microinversor_get=="Trifásico" and  classe_instalacao_get=="Trifásico"):
                                            Corrente = (potencia_microinversor_get*fator_get*1000)/((math.sqrt(3))*tensao_microinversor_get)                                                              
                                        elif (classe_microinversor_get=="Monofásico") or (classe_microinversor_get=="Monofásico Rural") or (classe_microinversor_get=="Bifásico" or (classe_microinversor_get=="Trifásico")):
                                            Corrente = (potencia_microinversor_get*fator_get*1000)/(tensao_microinversor_get)
                                        elif (classe_microinversor_get=="Monofásico Rural") or (classe_microinversor_get=="Bifásico") or (classe_microinversor_get=="Trifásico"):
                                            Corrente = (potencia_microinversor_get*fator_get*1000)/(tensao_microinversor_get)
                                        
                                        
                                        self.tree.delete(*self.tree.get_children()) #Limpa dos dados presentes na treeview

                                        lista=padrao_cemig() #Chama a função onde está armazenados os dados da CEMIG
                                        
                                        #Variáveis auxiliares
                                        A=0
                                        B=0
                                        C=0
                                        Quantidade_inversores=0
                                    
                                        #Lógica para encontrar a quantidade de inversores por fase e total
                                        if quantidade_microinversorAB_get!="":
                                            A+=quantidade_microinversorAB_get
                                            B+=quantidade_microinversorAB_get
                                            Quantidade_inversores+=quantidade_microinversorAB_get

                                        if quantidade_microinversorBC_get!="":
                                            B+=quantidade_microinversorBC_get
                                            C+=quantidade_microinversorBC_get
                                            Quantidade_inversores+=quantidade_microinversorBC_get

                                        if quantidade_microinversorCA_get!="":
                                            A+=quantidade_microinversorCA_get
                                            C+=quantidade_microinversorCA_get
                                            Quantidade_inversores+=quantidade_microinversorCA_get
                                        
                                        if quantidade_microinversorAN_get!="":
                                            A+=quantidade_microinversorAN_get
                                            Quantidade_inversores+=quantidade_microinversorAN_get
                                        
                                        if quantidade_microinversorBN_get!="":
                                            B+=quantidade_microinversorBN_get
                                            Quantidade_inversores+=quantidade_microinversorBN_get
                                        
                                        if quantidade_microinversorCN_get!="":
                                            C+=quantidade_microinversorCN_get
                                            Quantidade_inversores+=quantidade_microinversorCN_get

                                        
                                        #Variáveis auxiliares
                                        correnteA=0
                                        correnteB=0
                                        correnteC=0
                                    
                                        #Lógica para encontrar a corrente total por fase
                                        if A!=0:
                                            correnteA=Corrente*A
                                        if B!=0:
                                            correnteB=Corrente*B
                                        if C!=0:
                                            correnteC=Corrente*C

                                        
                                        #Verifica qual das fases possui a maior corrente
                                        Corrente_Resultante=np.max([correnteA, correnteB, correnteC])

                                        
                                        #Lógica para comparação do inversor com a classe de instalação
                                        aux_mono=[1]
                                        aux_bi=[2]
                                        aux_tri=[3,4,5,6,7,8,14,15,16,17,18,19,20,21,22,23,24,25]
                                        aux_mono_rural=[9,10,11,12,13]
                                        
                                            
                                        #Classe instalação Monofásica / Classe inversor Monofásico    
                                        if classe_instalacao_get=="Monofásico"and classe_microinversor_get=="Monofásico":
                                            for i in aux_mono:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                    self.tree.insert('', 'end', values=lista[i])
                                                    

                                        #Classe instalação Bifásico / Classe inversor Monofásico
                                        if classe_instalacao_get=="Bifásico"and classe_microinversor_get=="Monofásico":
                                            for i in aux_bi:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                    self.tree.insert('', 'end', values=lista[i])
                                                    

                                        #Classe instalação Bifásico / Classe inversor Bifásico
                                        if classe_instalacao_get=="Bifásico"and classe_microinversor_get=="Bifásico":
                                            for i in aux_bi:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                    self.tree.insert('', 'end', values=lista[i])

                                        
                                        #Classe instalação Trifásico / Classe inversor Monofásico
                                        if classe_instalacao_get=="Trifásico"and classe_microinversor_get=="Monofásico":
                                            for i in aux_tri:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                  self.tree.insert('', 'end', values=lista[i])

                                        
                                        #Classe instalação Trifásico / Classe inversor Bifásico
                                        if classe_instalacao_get=="Trifásico"and classe_microinversor_get=="Bifásico":
                                            for i in aux_tri:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                    self.tree.insert('', 'end', values=lista[i])

                                        
                                        #Classe instalação Trifásico / Classe inversor Trifásico
                                        if classe_instalacao_get=="Trifásico"and classe_microinversor_get=="Trifásico":
                                            for i in aux_tri:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                 self.tree.insert('', 'end', values=lista[i])

                                    
                                        #Classe instalação Mono Rural / Classe inversor Monofásico
                                        if classe_instalacao_get=="Monofásico Rural" and classe_microinversor_get=="Monofásico":
                                            for i in aux_mono_rural:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                 self.tree.insert('', 'end', values=lista[i])

                                        
                                        #Classe instalação Mono Rural / Classe inversor Bifásico
                                        if classe_instalacao_get=="Monofásico Rural"and classe_microinversor_get=="Bifásico":
                                            for i in aux_mono_rural:
                                                if (lista[i][6]>=Corrente_Resultante) and ((Quantidade_inversores*potencia_microinversor_get)<=lista[i][2]):
                                                 self.tree.insert('', 'end', values=lista[i])
                                                                                    
                                                                                                                                                                                
                                        #Atualiza o label na tela principal com os dados dos microinversores
                                        text_var.set(f"Potência do inversor (kW): {potencia_microinversor_get} \n Corrente (A): {Corrente:.2f} \n Classe de instalação: {classe_microinversor_get} \n Tensão do inversor (V): {tensao_microinversor_get} ")
                                        
                                        
                                        #Fecha a janela de configuração dos microinversores 
                                        new_window.destroy()
                                        
                                                                
                                except ValueError:
                                    mensagem="Não foi digitado um número válido. \n Por favor, tente novamente."
                                    se_erro(mensagem)  

                            else:
                                mensagem="Inversor não compatível com a \n classe de tensão. \n Por favor, tente novamente."
                                se_erro(mensagem)               
                        
                    else:
                        mensagem="Não foi setado todos os dados. \n Por favor, tente novamente."
                        se_erro(mensagem)
           
                else:
                    new_window.attributes("-topmost", False)
                    mensagem="A quantidade de inversor não foi \n inserida de forma correta. \n Por favor, tente novamente."
                    se_erro(mensagem)
    
           
            #Criação do label e da entrada de dados para potência de cada microinversor
            potencia_microinversor_label=ctk.CTkLabel(new_window, text="Potência de cada microinversor (em kW): ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black')
            potencia_microinversor_label.pack()
            potencia_microinversor = ctk.CTkEntry(new_window, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10)
            potencia_microinversor.pack(pady=5, padx=5)
            
        
            #Criação do label e do menu de opções para a classe de instalação do microinversor
            classe_microinversor_label=ctk.CTkLabel(new_window, text="Classe de instalação do microinversor: ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black')
            classe_microinversor_label.pack()
            classe_microinversor_var = ctk.StringVar(value="")
            classe_microinversor = ctk.CTkOptionMenu(new_window, 
                                                values=["Monofásico", "Bifásico", "Trifásico"],
                                                variable=classe_microinversor_var,
                                                width=150, height=30, corner_radius=20,
                                                fg_color="#cfcfcf", button_color="#cfcfcf", button_hover_color="white",
                                                dropdown_fg_color="#cfcfcf", dropdown_text_color="black", dropdown_hover_color="blue",
                                                font=("arial bold", 15), anchor="center", bg_color='#ebebeb', text_color="black")
            classe_microinversor.pack(pady=5, padx=5)

            
            #Criação do label e do menu de opções para a tensão de operação do microinversor
            tensao_microinversor_label=ctk.CTkLabel(new_window, text="Tensão de operação do microinversor: ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black')
            tensao_microinversor_label.pack()
            tensao_microinversor_var = ctk.StringVar(value="")
            tensao_microinversor = ctk.CTkOptionMenu(new_window, 
                                                values=["127", "220"],
                                                variable=tensao_microinversor_var,
                                                width=150, height=30, corner_radius=20,
                                                fg_color="#cfcfcf", button_color="#cfcfcf", button_hover_color="white",
                                                dropdown_fg_color="#cfcfcf", dropdown_text_color="black", dropdown_hover_color="blue",
                                                font=("arial bold", 15), anchor="center", bg_color='#ebebeb', text_color="black")
            tensao_microinversor.pack(pady=5, padx=5)
                    
            

            #Quantidade de microinversores
            quantidade_microinversor_label=ctk.CTkLabel(new_window, text="Quantidade de microinversores", font=("arial bold", 14), bg_color='#ebebeb', text_color='black')
            quantidade_microinversor_label.pack()


            # Primeiro frame principal para agrupar todos os elementos
            input_frame = ctk.CTkFrame(new_window,bg_color='#ebebeb',fg_color='#ebebeb')
            input_frame.pack(pady=5, padx=5, fill='x')

            # Frame para o primeiro par (AB)
            frame_ab = ctk.CTkFrame(input_frame,bg_color='#ebebeb',fg_color='#ebebeb')
            frame_ab.pack(side='left', pady=5)

            quantidade_microinversor_labelAB = ctk.CTkLabel(frame_ab, text="AB", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelAB.pack(side='left')

            quantidade_microinversorAB = ctk.CTkEntry(frame_ab, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10,bg_color='#ebebeb',fg_color='#ebebeb')
            quantidade_microinversorAB.pack(side='left', padx=5)

            # Espaço entre os pares
            spacer_frame = ctk.CTkFrame(input_frame, width=20, height=30,bg_color='#ebebeb',fg_color='#ebebeb')
            spacer_frame.pack(side='left')

            # Frame para o segundo par (AN)
            frame_an = ctk.CTkFrame(input_frame,bg_color='#ebebeb',fg_color='#ebebeb')
            frame_an.pack(side='left', pady=5)

            quantidade_microinversor_labelAN = ctk.CTkLabel(frame_an, text="AN", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelAN.pack(side='left')

            quantidade_microinversorAN = ctk.CTkEntry(frame_an, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10,bg_color='#ebebeb',fg_color='white')
            quantidade_microinversorAN.pack(side='left', padx=5)



            # Segundo frame principal para agrupar todos os elementos
            input_frame2 = ctk.CTkFrame(new_window,bg_color='#ebebeb',fg_color='#ebebeb')
            input_frame2.pack(pady=5, padx=5, fill='x')

            # Frame para o primeiro par (BC)
            frame_bc = ctk.CTkFrame(input_frame2,bg_color='#ebebeb',fg_color='#ebebeb')
            frame_bc.pack(side='left', pady=5)

            quantidade_microinversor_labelBC = ctk.CTkLabel(frame_bc, text="BC", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelBC.pack(side='left')

            quantidade_microinversorBC = ctk.CTkEntry(frame_bc, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10,bg_color='#ebebeb',fg_color='white')
            quantidade_microinversorBC.pack(side='left', padx=5)

            # Espaço entre os pares
            spacer_frame = ctk.CTkFrame(input_frame2, width=20, height=30,bg_color='#ebebeb',fg_color='#ebebeb')
            spacer_frame.pack(side='left')

            # Frame para o segundo par (BN)
            frame_bn = ctk.CTkFrame(input_frame2,bg_color='#ebebeb',fg_color='#ebebeb')
            frame_bn.pack(side='left', pady=5)

            quantidade_microinversor_labelBN = ctk.CTkLabel(frame_bn, text="BN", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelBN.pack(side='left')

            quantidade_microinversorBN = ctk.CTkEntry(frame_bn, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10,bg_color='#ebebeb',fg_color='white')
            quantidade_microinversorBN.pack(side='left', padx=5)



            #Terceiro frame principal para agrupar todos os elementos
            input_frame3 = ctk.CTkFrame(new_window, bg_color='#ebebeb',fg_color='#ebebeb')
            input_frame3.pack(pady=5, padx=5, fill='x')

            # Frame para o primeiro par (CA)
            frame_ca = ctk.CTkFrame(input_frame3, bg_color='#ebebeb',fg_color='#ebebeb')
            frame_ca.pack(side='left', pady=5)

            quantidade_microinversor_labelCA = ctk.CTkLabel(frame_ca, text="CA", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelCA.pack(side='left')

            quantidade_microinversorCA = ctk.CTkEntry(frame_ca, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10, bg_color='#ebebeb',fg_color='white')
            quantidade_microinversorCA.pack(side='left', padx=5)

            # Espaço entre os pares
            spacer_frame = ctk.CTkFrame(input_frame3, width=20, height=30, bg_color='#ebebeb',fg_color='#ebebeb')
            spacer_frame.pack(side='left')

            # Frame para o segundo par (CN)
            frame_cn = ctk.CTkFrame(input_frame3, bg_color='#ebebeb',fg_color='#ebebeb')
            frame_cn.pack(side='left', pady=5)

            quantidade_microinversor_labelCN = ctk.CTkLabel(frame_cn, text="CN", font=("arial bold", 14), bg_color='#ebebeb', text_color='black',fg_color='#ebebeb')
            quantidade_microinversor_labelCN.pack(side='left')

            quantidade_microinversorCN = ctk.CTkEntry(frame_cn, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10, bg_color='#ebebeb',fg_color='white')
            quantidade_microinversorCN.pack(side='left', padx=5)


            # Botão de validação
            button2 = ctk.CTkButton(new_window, text="Calcular", command=button_event2, font=("arial bold", 20), text_color="black", bg_color='#ebebeb')
            button2.pack(pady=20)

            new_window.lift()

            new_window.focus_force()
            new_window.attributes("-topmost", True)
            #new_window.after(10, lambda: new_window.attributes("-topmost", False))



        # Função para abrir nova janela se inversor
        def se_inversor():
        
            new_window = ctk.CTkToplevel()
            new_window.configure(bg='#ed1c24')
            new_window.title("Dados do inversor")
            centralize_window(new_window, 400, 300)
            
            # Função de validação
            def button_event2():
                
                potencia_inversor_get=potencia_inversor.get()
                classe_inversor_get=classe_inversor.get()
                tensao_inversor_get=tensao_inversor.get()
                classe_instalacao_get=classe_instalacao.get()
                fator_get=fator.get()
                fator_get=float(fator_get)

                #Verificando se todos os dados necessários foram setados
                if potencia_inversor_get!="" and classe_inversor_get!="" and tensao_inversor_get!="":
                    
                    #Verifica se a classe e a tensão são compatíveis
                    if (classe_inversor_get=="Monofásico" and tensao_inversor_get=='220') or (classe_inversor_get=="Bifásico" and tensao_inversor_get=='127') or (classe_inversor_get=="Trifásico" and tensao_inversor_get=='127') :
                        
                        mensagem="Classe incompatível com o nível de \n tensão de operação \n Por favor, tente novamente"
                        se_erro(mensagem)
                    
                    else:  
                        
                        if (classe_inversor_get=="Monofásico" and classe_instalacao_get=="Monofásico" ) or (classe_inversor_get=="Monofásico" and classe_instalacao_get=="Monofásico Rural") or (classe_inversor_get=="Monofásico" and classe_instalacao_get=="Bifásico") or (classe_inversor_get=="Monofásico" and classe_instalacao_get=="Trifásico") or (classe_inversor_get=="Bifásico" and classe_instalacao_get=="Monofásico Rural") or (classe_inversor_get=="Bifásico" and classe_instalacao_get=="Bifásico") or (classe_inversor_get=="Bifásico" and classe_instalacao_get=="Trifásico") or (classe_inversor_get=="Trifásico" and classe_instalacao_get=="Trifásico"):
                            try: 
                                #O try verifica se o número digitado é um float
                                potencia_inversor_get=float(potencia_inversor_get)
                                
                                if isinstance(potencia_inversor_get,float):
                                    
                                    tensao_inversor_get=float(tensao_inversor_get)

                                    #Controle do tipo de inversor
                                    if (classe_inversor_get=="Trifásico" and  classe_instalacao_get=="Trifásico"):
                                        Corrente = (potencia_inversor_get*fator_get*1000)/((math.sqrt(3))*tensao_inversor_get)                                                              
                                    elif (classe_inversor_get=="Monofásico") or (classe_inversor_get=="Monofásico Rural") or (classe_inversor_get=="Bifásico" or (classe_inversor_get=="Trifásico")):
                                        Corrente = (potencia_inversor_get*fator_get*1000)/(tensao_inversor_get)
                                    elif (classe_inversor_get=="Monofásico Rural") or (classe_inversor_get=="Bifásico") or (classe_inversor_get=="Trifásico"):
                                        Corrente = (potencia_inversor_get*fator_get*1000)/(tensao_inversor_get)
                                    
                                    #Limpa os dados da treeview
                                    self.tree.delete(*self.tree.get_children())
                                    
                                    #Chama a função com os dados da CEMIG
                                    lista=padrao_cemig()
                                    
                                    
                                    aux_mono=[1]
                                    aux_bi=[2]
                                    aux_tri=[3,4,5,6,7,8,14,15,16,17,18,19,20,21,22,23,24,25]
                                    aux_mono_rural=[9,10,11,12,13]
                                    
                                    #Classe de instalação Monofásico / Classe do inversor Monofásico    
                                    if classe_instalacao_get=="Monofásico" and classe_inversor_get=="Monofásico":
                                        for i in aux_mono:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])

                                    
                                    #Classe de instalação Bifásico / Classe do inversor Monofásico    
                                    if classe_instalacao_get=="Bifásico" and classe_inversor_get=="Monofásico":
                                        for i in aux_bi:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])
                                                

                                    #Classe de instalação Bifásico / Classe do inversor Bifásico    
                                    if classe_instalacao_get=="Bifásico" and classe_inversor_get=="Bifásico":
                                        for i in aux_bi:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])


                                    #Classe de instalação Trifásico / Classe do inversor Monofásico   
                                    if classe_instalacao_get=="Trifásico" and classe_inversor_get=="Monofásico":
                                        for i in aux_tri:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])

                                    
                                    #Classe de instalação Trifásico / Classe do inversor Bifásico 
                                    if classe_instalacao_get=="Trifásico" and classe_inversor_get=="Bifásico":
                                        for i in aux_tri:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])

                                    
                                    #Classe de instalação Trifásico / Classe do inversor Trifásico
                                    if classe_instalacao_get=="Trifásico" and classe_inversor_get=="Trifásico":
                                        for i in aux_tri:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])

                                    
                                    #Classe de instalação Monofásico Rural / Classe do inversor Monofásico
                                    if classe_instalacao_get=="Monofásico Rural" and classe_inversor_get=="Monofásico":
                                        for i in aux_mono_rural:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])

                                   
                                    #Classe de instalação Monofásico Rural / Classe do inversor Bifásico
                                    if classe_instalacao_get=="Monofásico Rural" and classe_inversor_get=="Bifásico":
                                        for i in aux_mono_rural:
                                            if (lista[i][6]>=Corrente) and (potencia_inversor_get<=lista[i][2]):
                                                self.tree.insert('', 'end', values=lista[i])
                                                                                    
                                                                                                           
                                    #Atualiza a label na janela principal com os dados do inversor
                                    text_var.set(f"Potência do inversor (kW): {potencia_inversor_get} \n Corrente (A): {Corrente:.2f} \n Classe de instalação: {classe_inversor_get} \n Tensão do inversor (V): {tensao_inversor_get} ")
                                    
                                    new_window.destroy() #Fecha a janela de dados do  inversor
                                    
                                                                
                            except ValueError:
                                mensagem="Não foi digitado um número válido \n Por favor, tente novamente"
                                se_erro(mensagem)  

                        else:
                            mensagem="Inversor não compatível com a \n classe de tensão \n Por favor, tente novamente"
                            se_erro(mensagem)               
                    
                else:
                    mensagem="Não foi setado todos os dados \n Por favor, tente novamente"
                    se_erro(mensagem)

                

            #Criar label e entrada de dados para a potência do inversor
            ctk.CTkLabel(new_window, text="Potência do inversor (em kW): ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black').pack()
            potencia_inversor = ctk.CTkEntry(new_window, placeholder_text="", width=150, height=30, border_width=2, corner_radius=10)
            potencia_inversor.pack(pady=5)
            
        
            #Criar label e botão de menu de opções para a classe de instalação do microinversor
            ctk.CTkLabel(new_window, text="Classe de instalação do microinversor: ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black').pack()
            classe_inversor_var = ctk.StringVar(value="")
            classe_inversor = ctk.CTkOptionMenu(new_window, 
                                                values=["Monofásico", "Bifásico", "Trifásico"],
                                                variable=classe_inversor_var,
                                                width=150, height=30, corner_radius=20,
                                                fg_color="#cfcfcf", button_color="#cfcfcf", button_hover_color="white",
                                                dropdown_fg_color="#cfcfcf", dropdown_text_color="black", dropdown_hover_color="blue",
                                                font=("arial bold", 15), anchor="center", bg_color='#ebebeb', text_color="black")
            classe_inversor.pack(pady=5, padx=5)

            
            #Criar label e menu de opções para a tensão de operação do microinversor
            ctk.CTkLabel(new_window, text="Tensão de operação: ", font=("arial bold", 14), bg_color='#ebebeb', text_color='black').pack()
            tensao_inversor_var = ctk.StringVar(value="")
            tensao_inversor = ctk.CTkOptionMenu(new_window, 
                                                values=["127", "220"],
                                                variable=tensao_inversor_var,
                                                width=150, height=30, corner_radius=20,
                                                fg_color="#cfcfcf", button_color="#cfcfcf", button_hover_color="white",
                                                dropdown_fg_color="#cfcfcf", dropdown_text_color="black", dropdown_hover_color="blue",
                                                font=("arial bold", 15), anchor="center", bg_color='#ebebeb', text_color="black")
            tensao_inversor.pack(pady=5, padx=5)

                             
            #Botão de validação do inversor setado
            button2 = ctk.CTkButton(new_window, text="Calcular", command=button_event2, font=("arial bold", 20), text_color="black", bg_color='#ebebeb')
            button2.pack(pady=20)

            
            #Força a janela de cadastro a ficar na frente da janela principal
            new_window.lift()
            new_window.focus_force()
            new_window.attributes("-topmost", True)
            new_window.after(10, lambda: new_window.attributes("-topmost", False))

        
        # Função para abrir nova janela se algum dado estiver errado
        def se_erro(mensagem):
        
            erro_window = ctk.CTkToplevel()
            erro_window.title("Dados incompatíveis")
            centralize_window(erro_window, 400, 200)
            erro_window.lift()
            erro_window.focus_force()
            erro_window.attributes("-topmost", True)
                                    
           
            #Adiciona conteúdo à nova janela
            label = ctk.CTkLabel(erro_window, text=mensagem, font=("arial bold", 20))
            label.pack(pady=20)
                    
           
            #Botão para fechar janela de erro
            button2 = ctk.CTkButton(erro_window, text="Fechar", command=erro_window.destroy, font=("arial bold", 20), text_color="black", bg_color='#ebebeb')
            button2.pack(pady=20)

        
        #Função para fechar a janela principal
        def button_fechar_event():
            root.destroy()


        # Frame para os botões
        button_frame = ctk.CTkFrame(selection_frame,bg_color="#cfcfcf",fg_color="#cfcfcf")
        button_frame.pack()


        # Botão para passar para etapa de cadastro dos dados de inversor
        button = ctk.CTkButton(button_frame, text="Próximo", command=button_event, font=("Arial Bold", 20), text_color="black", bg_color='#cfcfcf')
        button.pack(side="left", padx=(0, 10), pady=20)  # Espaço à direita

        
        # Botão para fechar a janela
        button_fechar = ctk.CTkButton(button_frame, text="Fechar", command=button_fechar_event, font=("Arial Bold", 20), text_color="black", bg_color='#cfcfcf',fg_color="red")
        button_fechar.pack(side="left", padx=(10, 0), pady=20)  # Espaço à esquerda


        #Label para mostrar os valores do inversor
        text_var= ctk.StringVar(value="")
        label_inversor=ctk.CTkLabel(selection_frame,textvariable=text_var,width=150,height=50,fg_color=("#ebebeb"),text_color="black",corner_radius=8).pack(pady=10) 


        # Label das normas técnicas
        ctk.CTkLabel(selection_frame, text="Normas técnicas: \n PEC11 - CEMIG \n ND5.1-Ver.DEZ/2022 ", font=("arial bold", 10), bg_color='#cfcfcf', text_color='black').pack(pady=25) 



if __name__ == "__main__":
    root = ctk.CTk()
    app = TreeViewApp(root)
    root.mainloop()
