import tkinter as tk
from tkinter import ttk, messagebox
from Usuarios import Usuarios  # Certifique-se de que o módulo Usuarios está disponível

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        # Frame para o formulário
        self.janela1 = tk.Frame(master)
        self.janela1.pack(padx=10, pady=10)

        # Título
        self.msg1 = tk.Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Frame para a busca
        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = tk.Label(self.janela2, text="Id usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = tk.Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = tk.Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["command"] = self.buscarUsuario
        self.busca.pack()

        # Frames para os campos de dados
        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = tk.Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = tk.Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = tk.Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = tk.Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = tk.Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = tk.Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = tk.Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = tk.Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = tk.Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = tk.Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela4, width=30)
        self.senha["show"] = "*"
        self.senha.pack(side="left")

        # Frame para os botões
        self.janela10 = tk.Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = tk.Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = tk.Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = tk.Button(self.janela11, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = tk.Button(self.janela11, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = tk.Button(self.janela11, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        # Frame para a tabela
        self.janela12 = tk.Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Telefone", "E-mail", "Usuário", "Senha"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.heading("Senha", text="Senha")
        self.tree.pack()

        # Evento de clique na linha da tabela
        self.tree.bind("<ButtonRelease-1>", self.selecionar_linha)

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        self.janela13 = tk.Frame(master)
        self.janela13["padx"] = 20
        self.janela13.pack(pady=10)

        self.botao4 = tk.Button(self.janela13, width=10, text="Voltar", command=self.voltarmenu)
        self.botao4.pack(side="left")

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4], u[5]))

    def selecionar_linha(self, event):
        """Preenche os campos de entrada com os dados da linha selecionada na tabela."""
        selected_item = self.tree.selection()  # Captura o item selecionado
        if selected_item:
            item = self.tree.item(selected_item[0])  # Obtém o primeiro item selecionado
            valores = item['values']  # Obtém os valores da linha selecionada

            # Verifique se a linha possui dados
            if valores:
                # Preenche os campos de entrada com os dados da linha selecionada
                self.idusuario.delete(0, tk.END)
                self.idusuario.insert(tk.END, valores[0])
                self.nome.delete(0, tk.END)
                self.nome.insert(tk.END, valores[1])
                self.telefone.delete(0, tk.END)
                self.telefone.insert(tk.END, valores[2])
                self.email.delete(0, tk.END)
                self.email.insert(tk.END, valores[3])
                self.usuario.delete(0, tk.END)
                self.usuario.insert(tk.END, valores[4])
                self.senha.delete(0, tk.END)
                self.senha.insert(tk.END, valores[5])

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        result = user.selectUser(idusuario)
        if result:
            self.autentic["text"] = "Usuário encontrado!"
            self.idusuario.delete(0, tk.END)
            self.idusuario.insert(tk.INSERT, result[0])
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.INSERT, result[1])
            self.telefone.delete(0, tk.END)
            self.telefone.insert(tk.INSERT, result[2])
            self.email.delete(0, tk.END)
            self.email.insert(tk.INSERT, result[3])
            self.usuario.delete(0, tk.END)
            self.usuario.insert(tk.INSERT, result[4])
            self.senha.delete(0, tk.END)
            self.senha.insert(tk.INSERT, result[5])
        else:
            self.autentic["text"] = "Usuário não encontrado!"

        # Atualiza a tabela com o usuário encontrado
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo("Inserir", "Usuário inserido com sucesso!")

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        user.updateUser()  # Atualiza o usuário
        messagebox.showinfo("Alterar", "Usuário alterado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.deleteUser()  # Exclui o usuário
        messagebox.showinfo("Excluir", "Usuário excluído com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.idusuario.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.telefone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.usuario.delete(0, tk.END)
        self.senha.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())

    def voltarmenu(self):
        self.master.destroy()

# Criação da janela principal e execução da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
