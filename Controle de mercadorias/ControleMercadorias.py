import pyodbc
from tkinter import *
from tkinter import ttk

#--------------------------------------------------------------------------
#2º - Função dos botões da Tela de Login

#Função que verifica se as credenciais do usuario estão corretas
def verifica_credenciais():
    
    #Configuração do banco de dados
    #Driver - Drive
    #Server - Servidor (localhost se o banco está na nossa própria máquina)
    #Database - Nome do banco de dados

    #Se o banco de senha possuir login e senha
    #UID - Login 
    #PWD - Senha

    dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db")

    #Criando a conexão e verificando se o python está conectando corretamente com o banco de dados
    conexao=pyodbc.connect(dadosConexao)
    print("Conectado com sucesso!")


    cursor=conexao.cursor()


    #Selecionando a tabela usuários do banco de dados e comparando com a digitada pelo usuario
    cursor.execute("SELECT * FROM Usuarios WHERE Nome=? AND Senha=?",(nome_usuario_entry.get(),senha_usuario_entry.get()))
    #Primeiro ? é preenchido por nome_usuario_entry.get()
    #Segundo ? é preenchido por senha_usuario_entry.get()


    #Recebe os dados da execução acima
    #True/False
    usuario=cursor.fetchone()


    if usuario: #se o usuário existir
        
        #Fechando a janela de login
        janela_principal.destroy()

        #Conexão com o banco de dados
        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projetos_Compras.db")
        conexao=pyodbc.connect(dadosConexao)
        cursor=conexao.cursor()
        conexao.execute("SELECT * FROM Produtos")



        def listar_dados():

            #Limpa os valores da treeview
            for i in treeview.get_children():

                treeview.delete(i)
            
            #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
            cursor.execute("SELECT * FROM Produtos")
            
            #Armazena os valores retornados pelo comando SQL em uma variável
            valores=cursor.fetchall()

            #Adiciona os valores na TreeView
            for valor in valores:

                #Popular linha por linha
                treeview.insert("","end",values=(valor[0],valor[1],valor[2],valor[3],valor[4]))


        #Criando uma janela tkinter com o titulo "Cadastro de Produtos"
        janela=Tk()
        janela.title("Cadastro de Produtos")
        janela.configure(bg="#F5F5F5")


        #Deixando a janela em tela cheia
        janela.attributes("-fullscreen",True)

        #Captura do nome do produto a ser buscado
        Label(janela,text="Nome do Produto: ",font="Arial 16",bg="#F5F5F5").grid(row=0,column=2,padx=10,pady=10)
        nome_produto=Entry(janela,font="Arial 16")
        nome_produto.grid(row=0,column=3,padx=10,pady=10)

        #Captura da descrição do produto a ser buscado
        Label(janela,text="Descrição do Produto: ",font="Arial 16",bg="#F5F5F5").grid(row=0,column=5,padx=10,pady=10)
        descricao_produto=Entry(janela,font="Arial 16")
        descricao_produto.grid(row=0,column=6,padx=10,pady=10)

        #Título treeview
        Label(janela,text="Produtos cadastrados",font="Arial 20 italic",fg="black",bg="#F5F5F5").grid(row=2,column=0,columnspan=10,padx=10,pady=10)




        #Função para cadastrar o produto
        def cadastrar():
        
            #Toplevel é para gerar a janela de cadastro como uma janela secundaria
            #em cima da janela principal
            janela_cadastrar = Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")

            #Definindo a cor de fundo da janela
            janela_cadastrar.configure(bg="#FFFFFF")

            #Execução de códigos para deixar a janela centralizada na tela
            #Define a largura e a altura da janela
            largura_janela=450
            altura_janela=300

            #Obtem a largura e a altura da tela do COMPUTADOR
            largura_tela=janela_cadastrar.winfo_screenwidth()
            altura_tela=janela_cadastrar.winfo_screenheight()

            #Calcula a posição da janela para centraliza-la na tela
            pos_x=(largura_tela//2)-(largura_janela//2)
            pos_y=(altura_tela//2)-(altura_janela//2)

            #Definindo a posição da janela na tela do computador
            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))

            #Centralizando os elementos
            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i,weight=1)

            
            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i,weight=1)


        
            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth":2,"relief":"groove"}


            #Label nome do produto
            nome_produto_lbl=Label(janela_cadastrar, text="Nome do Produto:", font=("Arial",12),bg="#FFFFFF")
            nome_produto_lbl.grid(row=0,column=0,padx=10,pady=10,stick="W")

            nome_produto_cadastrar=Entry(janela_cadastrar,font=("Arial",12),**estilo_borda)
            nome_produto_cadastrar.grid(row=0,column=1,padx=10,pady=10)


            #Label descrição do produto
            descricao_produto_lbl=Label(janela_cadastrar, text="Descrição do Produto:", font=("Arial",12),bg="#FFFFFF")
            descricao_produto_lbl.grid(row=1,column=0,padx=10,pady=10,stick="W")

            descricao_produto_cadastrar=Entry(janela_cadastrar,font=("Arial",12),**estilo_borda)
            descricao_produto_cadastrar.grid(row=1,column=1,padx=10,pady=10)


            #Label preço do produto
            preco_produto_lbl=Label(janela_cadastrar, text="Preço do Produto:", font=("Arial",12),bg="#FFFFFF")
            preco_produto_lbl.grid(row=2,column=0,padx=10,pady=10,stick="W")

            preco_produto_cadastrar=Entry(janela_cadastrar,font=("Arial",12),**estilo_borda)
            preco_produto_cadastrar.grid(row=2,column=1,padx=10,pady=10)


            #Quantidade do produto
            quantidade_produto_lbl=Label(janela_cadastrar, text="Quantidade do Produto:", font=("Arial",12),bg="#FFFFFF")
            quantidade_produto_lbl.grid(row=3,column=0,padx=10,pady=10,stick="W")

            quantidade_produto_cadastrar=Entry(janela_cadastrar,font=("Arial",12),**estilo_borda)
            quantidade_produto_cadastrar.grid(row=3,column=1,padx=10,pady=10)


            #cria uma função para salvar os dados no BD
            def salvar_dados():
                
                #Cria uma tupla com os valores dos campos de texto
                novo_produto_cadastrar=(nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get(),quantidade_produto_cadastrar.get())
                
                #Executa um comando SQL para inserir os dados na tabela Produtos no BD
                cursor.execute("INSERT INTO Produtos (NomeProduto,Descricao,Preco,Quantidade) Values (?,?,?,?)",novo_produto_cadastrar)
                conexao.commit()#Gravando no BD 

                #Fecha a janela de cadastro
                janela_cadastrar.destroy()

                #Listar dados na treeview
                listar_dados()


            botao_salvar_dados=Button(janela_cadastrar, text="Salvar", font=("Arial",12),command=salvar_dados)
            botao_salvar_dados.grid(row=4,column=0,columnspan=2,padx=10,pady=10,stick="NSEW")


            botao_cancelar=Button(janela_cadastrar, text="Cancelar", font=("Arial",12),command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=5,column=0,columnspan=2,padx=10,pady=10,stick="NSEW")


        #Criar um botão para gravar os dados na tabela Produtos do banco de dados
        botao_gravar=Button(janela,text="Novo",command=cadastrar,font="Arial 26")
        botao_gravar.grid(row=4,column=0,columnspan=4,stick="NSEW",pady=5,padx=20)


        #Deleta o registro
        def deletar():

                #Recupera o id do registro selecionado na treeview
                selected_item=treeview.selection()[0]
                id=treeview.item(selected_item)['values'][0]
                
                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id =?",(id))
                
                conexao.commit()

                #Recarrregar os dados sem o novo registro
                listar_dados()

        #Criar um botão para deletar os dados na tabela Produtos do banco de dados
        botao_deletar=Button(janela,text="Deletar",command=deletar,font="Arial 26")
        botao_deletar.grid(row=4,column=4,columnspan=4,stick="NSEW",pady=5,padx=20)



        #Define o estilo da Treeview
        style=ttk.Style(janela)

        #Criando a TreeView
        treeview=ttk.Treeview(janela,style="mystyle.Treeview")

        style.theme_use("default")

        #Configurando
        style.configure("mystyle.Treeview",font=("Arial",14))

        treeview=ttk.Treeview(janela,style="mystyle.Treeview",columns=("ID","NomeProduto","Descricao","Preco","Quantidade"),show="headings",height=20)

        treeview.heading("ID",text="ID")
        treeview.heading("NomeProduto",text="Nome do Produto")
        treeview.heading("Descricao",text="Descrição do Produto")
        treeview.heading("Preco",text="Preço do Produto")
        treeview.heading("Quantidade",text="Quantidade do Produto")

        #A primeira coluna, identificada como "#0"
        #A opção "stretch=NO" indica que a coluna não deve esticar para preencher o espaço disponível.
        treeview.column("#0",width=0,stretch=NO)
        treeview.column("ID",width=100,stretch=NO)
        treeview.column("NomeProduto",width=300,stretch=NO)
        treeview.column("Descricao",width=350,stretch=NO)
        treeview.column("Preco",width=200,stretch=NO)
        treeview.column("Quantidade",width=350,stretch=NO)

        treeview.grid(row=3,column=0,columnspan=10,stick="NSEW")

        #Chama a função para listar os valores do banco de dados na treeview
        listar_dados()


        #Edição dos dados com duplo clique na treeview
        def editar_dados(event):

            #Obtém o item selecionado na Treeview
            item_selecionado=treeview.selection()[0]

            #Obtém os valores do item selecionado
            valores_selecionados=treeview.item(item_selecionado)['values']

            
            #Toplevel é para gerar a janela de cadastro como uma janela secundaria
            #em cima da janela principal
            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Produto")

            #Definindo a cor de fundo da janela
            janela_edicao.configure(bg="#FFFFFF")

            #Execução de códigos para deixar a janela centralizada na tela
            #Define a largura e a altura da janela
            largura_janela=500
            altura_janela=350

            #Obtem a largura e a altura da tela do COMPUTADOR
            largura_tela=janela_edicao.winfo_screenwidth()
            altura_tela=janela_edicao.winfo_screenheight()

            #Calcula a posição da janela para centraliza-la na tela
            pos_x=(largura_tela//2)-(largura_janela//2)
            pos_y=(altura_tela//2)-(altura_janela//2)

            #Definindo a posição da janela na tela do computador
            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))

            #Centralizando os elementos
            for i in range(7):
                janela_edicao.grid_rowconfigure(i,weight=1)

            #2 pois foram 2 colunas que utilizamos para forma a janela de LOGIN
            for i in range(2):
                janela_edicao.grid_columnconfigure(i,weight=1)


        
            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth":2,"relief":"groove"}


            #Label nome do produto
            nome_produto_lbl=Label(janela_edicao, text="Nome do Produto:", font=("Arial",16),bg="#FFFFFF")
            nome_produto_lbl.grid(row=0,column=0,padx=10,pady=10,stick="W")

            nome_produto_edicao=Entry(janela_edicao,font=("Arial",16),**estilo_borda,bg="#FFFFFF",textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0,column=1,padx=10,pady=10)


            #Label descrição do produto
            descricao_produto_lbl=Label(janela_edicao, text="Descrição do Produto:", font=("Arial",16),bg="#FFFFFF")
            descricao_produto_lbl.grid(row=1,column=0,padx=10,pady=10,stick="W")

            descricao_produto_edicao=Entry(janela_edicao,font=("Arial",16),**estilo_borda,bg="#FFFFFF",textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1,column=1,padx=10,pady=10)


            #Label preço do produto
            preco_produto_lbl=Label(janela_edicao, text="Preço do Produto:", font=("Arial",16),bg="#FFFFFF")
            preco_produto_lbl.grid(row=2,column=0,padx=10,pady=10,stick="W")

            preco_produto_edicao=Entry(janela_edicao,font=("Arial",16),**estilo_borda,bg="#FFFFFF",textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2,column=1,padx=10,pady=10)


            #Label quantidade do produto
            quantidade_produto_lbl=Label(janela_edicao, text="Quantidade do Produto:", font=("Arial",16),bg="#FFFFFF")
            quantidade_produto_lbl.grid(row=3,column=0,padx=10,pady=10,stick="W")

            quantidade_produto_edicao=Entry(janela_edicao,font=("Arial",16),**estilo_borda,bg="#FFFFFF",textvariable=StringVar(value=valores_selecionados[4]))
            quantidade_produto_edicao.grid(row=3,column=1,padx=10,pady=10)





            #cria uma função para salvar os dados no BD
            def salvar_edicao():
                
                #Cria uma tupla com os valores dos campos de texto
                novo_produto=nome_produto_edicao.get()
                nova_descricao=descricao_produto_edicao.get()
                novo_preco=preco_produto_edicao.get()
                nova_quantidade=quantidade_produto_edicao.get()
                

                #Atualiza os valores do item selecionado
                treeview.item(item_selecionado,values=(valores_selecionados[0],novo_produto,nova_descricao,novo_preco,nova_quantidade))

                
                #Executa um comando SQL para inserir os dados na tabela Produtos no BD
                cursor.execute("UPDATE Produtos SET NomeProduto=?, Descricao=?, Preco=?, Quantidade=? WHERE ID = ?" , novo_produto, nova_descricao, novo_preco, nova_quantidade, valores_selecionados[0])
                conexao.commit()#Gravando no BD 

                #Fecha a janela de cadastro
                janela_edicao.destroy()

                #Listar dados na treeview
                #listar_dados()


            botao_salvar_edicao=Button(janela_edicao, text="Alterar", font=("Arial",16),bg="#008000",fg="#FFFFFF",command=salvar_edicao)
            botao_salvar_edicao.grid(row=5,column=0,padx=20,pady=20)


            def deletar_registro():

                #Recupera o id do registro selecionado na treeview
                selected_item=treeview.selection()[0]
                id=treeview.item(selected_item)['values'][0]
                
                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id =?",(id))
                
                conexao.commit()

                #Fecha a janela de edição
                janela_edicao.destroy()

                #Recarrregar os dados sem o novo registro
                listar_dados()
        
        
            botao_deletar_edicao=Button(janela_edicao, text="Deletar", font=("Arial",16),bg="#FF0000",fg="#FFFFFF",command=deletar_registro)
            botao_deletar_edicao.grid(row=5,column=1,padx=20,pady=20)



        #Adiciona o evento de duplo clique na TreeView para editar os dados do produto
        treeview.bind("<Double-1>",editar_dados)


        #Criação do filtro

        #Limpar os dados da treeview
        def limparDados():

            #limpando os valores da treeview
            for i in treeview.get_children():
                
                #Deleta linha por linha
                treeview.delete(i)


        def filtrar_dados(nome_produto,descricao_produto):
            
            #Verificar se os campos de filtro estão vazios
            if not nome_produto.get() and not descricao_produto.get():

                listar_dados()

                #Se ambos os campos estiverem vazios, não faz nada
                return
            
            
            sql="SELECT * From Produtos"

            params=[]


            #Utilizado para filtrar resultados de uma consulta de BD
            #com base em um padrão de correspondência de texto
            if nome_produto.get():

                sql += " WHERE NomeProduto LIKE ?"
                params.append('%' + nome_produto.get()+'%')

            
            if descricao_produto.get():
                
                if nome_produto.get():
                    
                    sql += " AND"
                
                else:

                    sql += " WHERE"

                sql+=" Descricao LIKE ?"

                params.append('%'+ descricao_produto.get()+'%')

            cursor.execute(sql,tuple(params))

            produtos=cursor.fetchall()

            #Limpar dados da treeview
            limparDados()

            #Preenche treeview com os dados filtrados
            for dado in produtos:
                treeview.insert('','end',values=(dado[0],dado[1],dado[2],dado[3],dado[4]))




        #Cada vez que digitar ele irá chamar o evento KeyRelease
        nome_produto.bind('<KeyRelease>',lambda e: filtrar_dados(nome_produto,descricao_produto))
        descricao_produto.bind('<KeyRelease>',lambda e: filtrar_dados(nome_produto,descricao_produto))


        #Configura a janela para utilizar a barra de menus criada
        menu_barra=Menu(janela)
        janela.configure(menu=menu_barra)

        #Cria o menu chamado arquivo
        menu_arquivo=Menu(menu_barra,tearoff=0)
        #tearoff - a linha pontilhada não será exibida e o menu ficará fixo na janela
        menu_barra.add_cascade(label="Arquivo",menu=menu_arquivo)


        #Criando a opção no menu "Arquivo" chamada "Cadastrar"
        menu_arquivo.add_command(label="Cadastrar",command=cadastrar)

        #Criando a opção no menu "Arquivo" chamada "Sair"
        menu_arquivo.add_command(label="Sair",command=janela.destroy)









        #Inicia a janela do Tkinter
        janela.mainloop()

        #Fechar o cursor e a conexao
        cursor.close()
        conexao.close()

       

    else:#se o usuário não existir

        mensagem_lbl=Label(janela_principal,text="Nome de usuário ou senha incorretos",fg="red")
        mensagem_lbl.grid(row=3,column=0,columnspan=2)



#--------------------------------------------------------------------------
#1º Criação da janela de LOGIN

#Criando a janela principal para a tela de login
janela_principal=Tk()
janela_principal.title("Tela de Login")

#Definindo a cor de fundo da janela
janela_principal.configure(bg="#F5F5F5")



#Execução de códigos para deixar a janela centralizada na tela
#Define a largura e a altura da janela
largura_janela=450
altura_janela=450

#Obtem a largura e a altura da tela do COMPUTADOR
largura_tela=janela_principal.winfo_screenwidth()
altura_tela=janela_principal.winfo_screenheight()

#Calcula a posição da janela para centraliza-la na tela
pos_x=(largura_tela//2)-(largura_janela//2)
pos_y=(altura_tela//2)-(altura_janela//2)

#Definindo a posição da janela na tela do computador
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela,altura_janela,pos_x,pos_y))




#Criação de um label de título
titulo_lbl=Label(janela_principal,text=("Tela de login"),font="Arial 20 italic", fg="black",bg="#F5F5F5")
titulo_lbl.grid(row=0,column=0,columnspan=2,pady=20) 
#columnspan - quantas colunas ele ira ocupar
#pady - espaçamento


#Criação de um label para nome de usuário
nome_usuario_lbl= Label(janela_principal,text="Nome de usuário",font="Arial 14 bold",bg="#F5F5F5")
nome_usuario_lbl.grid(row=1,column=0,sticky="e") 
#stick - onde vamos deixar ele alinhado (N-norte, S-sul,E-Leste,W-Oeste)


#Criação de um label para a senha
senha_usuario_lbl= Label(janela_principal,text="Senha",font="Arial 14 bold",bg="#F5F5F5")
senha_usuario_lbl.grid(row=2,column=0,sticky="e") 
#stick - onde vamos deixar ele alinhado (N-norte, S-sul,E-Leste,W-Oeste)


#Criando um entry para o campo Nome de usuário
nome_usuario_entry= Entry(janela_principal,font="Arial 14")
nome_usuario_entry.grid(row=1,column=1,pady=10)


#Criando um entry para o campo Senha
senha_usuario_entry= Entry(janela_principal,show="*",font="Arial 14")
#o show faz a senha digitada ficar da forma ***
senha_usuario_entry.grid(row=2,column=1,pady=10)


#Botão de entrada
entrar_btn=Button(janela_principal,text="Entrar",font="Arial 14",command=verifica_credenciais)
#command - executa a respectiva função quando o botão é clicado
entrar_btn.grid(row=4,column=0,columnspan=2,padx=20,pady=10,stick="NSEW")
#stick NSEW - preenche as laterais


#Botão de saída
saida_btn=Button(janela_principal,text="Sair",font="Arial 14",command=janela_principal.destroy)
#command - executa a respectiva função quando o botão é clicado
#janela.destroy - fecha a janela
saida_btn.grid(row=5,column=0,columnspan=2,padx=20,pady=10,stick="NSEW")
#stick NSEW - preenche as laterais

#Label informativo
informativo_lbl=Label(janela_principal,text=("Usuário para teste: \n Usuário: Aluno \n Senha: 123"),font="Arial 14 italic", fg="black",bg="#F5F5F5")
informativo_lbl.grid(row=6,column=0,columnspan=2,pady=20)


#Centralizando os elementos
for i in range(5):
    janela_principal.grid_rowconfigure(i,weight=1)


for i in range(2):
    janela_principal.grid_columnconfigure(i,weight=1)




#Inicia a janela do Tkinter
janela_principal.mainloop()