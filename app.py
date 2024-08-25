import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Controllers.TurmaController import OperacoesTurma

class ControleTurmasApp:
    def __init__(this, root):
        this.root = root
        this.root.title("Controle de Turmas")
        this.operacoesTurma = OperacoesTurma()

        this.tela_atual = None

        this.telaPrincipal = tk.Frame(root)
        this.telaPrincipal.pack(fill=tk.BOTH, expand=True)
        this.root.geometry("750x450")
        this.root.resizable(False, False)

        menu_frame = tk.Frame(this.telaPrincipal, width=200, bg="#303b27")
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        this.menu_buttons = {
            "CADASTRAR ALUNO": this.chamaTelaCadastro,
            "EDITAR ALUNO": this.chamaTelaEdicao,
            "EXCLUIR ALUNO": this.chamaTelaExclusao,
            "LISTAR ALUNOS": this.chamaTelaListarAlunos,
            "RESUMO ESTATÍSTICO": this.chamaTelaResumoEstatistico,
            "EXPORTAR DADOS": this.chamaTelaExportarDados,
            "IMPORTAR DADOS": this.chamaTelaImportarDados,
            "SAIR": this.sair
        }

        for label, func in this.menu_buttons.items():
            button = tk.Button(menu_frame, text=label, command=func, height=2, width=20, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 10, "bold"), cursor="hand2")
            button.pack(fill=tk.X, padx=10, pady=5, anchor="w")
      
        this.chamaTelaCadastro() # Coloquei para que já inicie na tela de cadastro

    def mostrarTela(this, tela):
        if this.tela_atual:
            this.tela_atual.destroy()

        this.tela_atual = tela
        this.tela_atual.pack(fill=tk.BOTH, expand=True)


# 1 - Cadastro de Aluno
    def chamaTelaCadastro(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="CADASTRO DE ALUNO", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)

        labelRA = tk.Label(tela, text="RA:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelRA.pack()
        valorRA = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorRA.pack()

        labelNome = tk.Label(tela, text="Nome:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelNome.pack()
        valorNome = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorNome.pack()

        labelNota = tk.Label(tela, text="Nota:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelNota.pack()
        valorNota = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorNota.pack()

        def cadastrar():
            ra = valorRA.get()
            nome = valorNome.get()
            nota = valorNota.get()

            if ra != '' and nome != '' and nota != '': 
                if not this.operacoesTurma.ExisteRA(ra):
                    this.operacoesTurma.cadastrarAluno(ra, nome, nota)
                    msg.config(text="Aluno cadastrado com sucesso.", fg="green", font=("Helvetica", 10, "bold"))
                else:
                    msg.config(text="RA já está em uso. Não foi possível cadastrar o aluno.", fg="red", font=("Helvetica", 10, "bold"))
            else:
                msg.config(text="Todos os campos são obrigatórios.", fg="red", font=("Helvetica", 10, "bold"))

        btnCadastrarAluno = tk.Button(tela, text="Cadastrar", command=cadastrar, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 12, "bold"), cursor="hand2")
        btnCadastrarAluno.pack(pady=20, anchor="center")

        msg = tk.Label(tela, text="", fg="black")
        msg.pack()

        this.mostrarTela(tela)


# 2 - Edição de Aluno
    def chamaTelaEdicao(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="EDIÇÃO DE ALUNO", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)
        
        labelRA = tk.Label(tela, text="RA:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelRA.pack()
        valorRA = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorRA.pack()
        this.raParaEdicao = ""

        def buscarAluno():
            ra = valorRA.get()
            this.raParaEdicao = ra

            if this.raParaEdicao != '': 
                if this.operacoesTurma.ExisteRA(ra):
                    aluno = this.operacoesTurma.buscarAluno(ra)
                    valorNome.delete(0, tk.END)
                    valorNome.insert(0, aluno.nome)
                    valorNota.delete(0, tk.END)
                    valorNota.insert(0, aluno.nota)
                    msg.config(text="", fg="black")
                else:
                    valorNome.delete(0, tk.END)
                    valorNota.delete(0, tk.END)
                    msg.config(text="Informe um RA existente.", fg="red", font=("Helvetica", 10, "bold"))                 
            else:
                msg.config(text="Informe o RA do aluno.", fg="red", font=("Helvetica", 10, "bold"))

        btnBuscarAluno = tk.Button(tela, text="Buscar Aluno", command=buscarAluno, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 10, "bold"), cursor="hand2")
        btnBuscarAluno.pack(pady=20, anchor="center")

        labelNome = tk.Label(tela, text="Nome:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelNome.pack()
        valorNome = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorNome.pack()

        labelNota = tk.Label(tela, text="Nota:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelNota.pack()
        valorNota = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorNota.pack()

        def editarAluno():
            novoNome = valorNome.get()
            novaNota = valorNota.get()
            if this.raParaEdicao != '':
                if novoNome != '' and novaNota != '':
                    this.operacoesTurma.editarAluno(this.raParaEdicao, novoNome, novaNota)
                    msg.config(text="Aluno editado com sucesso.", fg="green", font=("Helvetica", 10, "bold"))
                else:
                    msg.config(text="Os campos para edição não podem estar vazios.", fg="red", font=("Helvetica", 10, "bold"))
            else: 
                msg.config(text="Necessário buscar o aluno para edição.", fg="red", font=("Helvetica", 10, "bold"))

        btnEditarAluno = tk.Button(tela, text="Salvar", command=editarAluno, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 12, "bold"), cursor="hand2")
        btnEditarAluno.pack(pady=20, anchor="center")

        msg = tk.Label(tela, text="", fg="black")
        msg.pack()

        this.mostrarTela(tela)


# 3 - Exclusão de Aluno
    def chamaTelaExclusao(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="EXCLUSÃO DE ALUNO", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)

        labelInstrucao = tk.LabelFrame(tela, text="Informe o RA do aluno a ser excluído:")
        labelInstrucao.pack()

        labelRA = tk.Label(tela, text="RA:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelRA.pack()
        valorRA = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorRA.pack()

        def excluirAluno():
            ra = valorRA.get()
            if this.operacoesTurma.ExisteRA(ra):
                aluno = this.operacoesTurma.buscarAluno(ra)
                if messagebox.askokcancel("Exclusão de aluno", f"O aluno {aluno.nome} (RA: {ra}) será excluído, deseja continuar?"):
                    this.operacoesTurma.excluirAluno(ra)
                    msg.config(text="Aluno excluído com sucesso.", fg="green", font=("Helvetica", 10, "bold"))
            else: 
                msg.config(text="Informe um RA existente para exclusão do aluno.", fg="red", font=("Helvetica", 10, "bold"))

        btnExcluirAluno = tk.Button(tela, text="Excluir", command=excluirAluno, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 12, "bold"), cursor="hand2")
        btnExcluirAluno.pack(pady=20, anchor="center")

        msg = tk.Label(tela, text="", fg="black")
        msg.pack()

        this.mostrarTela(tela)


# 4 - Lista de Alunos
    def chamaTelaListarAlunos(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="ALUNOS", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=20)

        columns = ("RA", "Nome", "Nota")
        treeview = ttk.Treeview(tela, columns=columns, show="headings")
        treeview.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            treeview.heading(col, text=col, anchor=tk.W)
            treeview.column(col, width=100)

        alunos = this.operacoesTurma.alunos
        for aluno in alunos:
            treeview.insert("", "end", values=(aluno.ra, aluno.nome, aluno.nota))

        this.mostrarTela(tela)


# 5 - Resumo Estatístico
    def chamaTelaResumoEstatistico(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="RESUMO ESTATÍSTICO", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)
        
        labelQtdeAlunos = tk.Label(tela, text="Quantidade de alunos da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelQtdeAlunos.pack()
        qtdeAlunos = this.operacoesTurma.getQuantidadeAlunos()
        msgQtdeAlunos = tk.Label(tela, text=f"{qtdeAlunos}", fg="darkgreen", font=("Helvetica", 12, "bold"))
        msgQtdeAlunos.pack(pady=15)
        
        alunoMaiorNota = this.operacoesTurma.getAlunoMaiorNota()
        if alunoMaiorNota is not None:
            labelMaiorNota = tk.Label(tela, text="Maior nota da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
            labelMaiorNota.pack()
            msgAlunoMaiorNota = tk.Label(tela, text=f"{alunoMaiorNota.nota} | {alunoMaiorNota.nome}", fg="green", font=("Helvetica", 12, "bold"))
            msgAlunoMaiorNota.pack(pady=15)
        else:
            labelMaiorNota = tk.Label(tela, text="Maior nota da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
            labelMaiorNota.pack()
            msgAlunoMaiorNota = tk.Label(tela, text="Nenhum aluno encontrado", fg="green", font=("Helvetica", 12, "bold"))
            msgAlunoMaiorNota.pack(pady=15)

        alunoMenorNota = this.operacoesTurma.getAlunoMenorNota()
        if alunoMenorNota is not None:
            labelMenorNota = tk.Label(tela, text="Menor nota da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
            labelMenorNota.pack()
            msgAlunoMenorNota = tk.Label(tela, text=f"{alunoMenorNota.nota} | {alunoMenorNota.nome}", fg="red", font=("Helvetica", 12, "bold"))
            msgAlunoMenorNota.pack(pady=15)
        else:
            labelMenorNota = tk.Label(tela, text="Menor nota da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
            labelMenorNota.pack()
            msgAlunoMenorNota = tk.Label(tela, text="Nenhum aluno encontrado", fg="red", font=("Helvetica", 12, "bold"))
            msgAlunoMenorNota.pack(pady=15)
        
        labelMediaNotasTurma = tk.Label(tela, text="Média de notas da turma: ", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelMediaNotasTurma.pack()
        mediaNotas = this.operacoesTurma.getMediaNotasTurma()
        msgMediaNotas = tk.Label(tela, text=f"{mediaNotas:.1f}", font=("Helvetica", 12, "bold"))
        msgMediaNotas.pack(pady=15)

        this.mostrarTela(tela)


 # 6 - Exportação de Dados
    def chamaTelaExportarDados(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="EXPORTAR DADOS", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)
        
        labelArquivo = tk.Label(tela, text="Informe um nome para o arquivo:", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelArquivo.pack()
        valorArquivo = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorArquivo.pack()

        def exportarDados():
            nomeArquivo = valorArquivo.get()
            if(nomeArquivo != ''):
                this.operacoesTurma.exportarDados(nomeArquivo)
                msg.config(text="Arquivo exportado com sucesso.", fg="green", font=("Helvetica", 10, "bold"))
            else:
                msg.config(text="Informe um nome para o arquivo.", fg="red", font=("Helvetica", 10, "bold"))

        btnExportarDados = tk.Button(tela, text="Exportar", command=exportarDados, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 12, "bold"), cursor="hand2")
        btnExportarDados.pack(pady=20, anchor="center")

        msg = tk.Label(tela, text="", fg="black")
        msg.pack()

        this.mostrarTela(tela)


 # 7 - Importação de Dados
    def chamaTelaImportarDados(this):
        tela = tk.Frame(this.telaPrincipal)
        tituloTela = tk.Label(tela, text="IMPORTAR DADOS", font=("Helvetica", 14, "bold"), fg="green")
        tituloTela.pack(pady=40)
        
        labelArquivo = tk.Label(tela, text="Informe o nome do arquivo (Ex: 'Resources/alunos.txt'):", font=("Helvetica", 12, "bold"), fg="#303b27")
        labelArquivo.pack()
        valorArquivo = tk.Entry(tela, width=40, font=("Helvetica", 10, "bold"), fg="darkgreen", borderwidth=2)
        valorArquivo.pack()

        def importarDados():
            nomeArquivo = valorArquivo.get()
            if(nomeArquivo != ''):
                try:
                    this.operacoesTurma.importarDados(nomeArquivo)
                    msg.config(text="Arquivo importado com sucesso.", fg="green", font=("Helvetica", 10, "bold"))
                except FileNotFoundError:
                    msg.config(text="Arquivo não foi encontrado.", fg="red", font=("Helvetica", 10, "bold"))
                except:
                    msg.config(text="Erro ao importar arquivo.", fg="red", font=("Helvetica", 10, "bold"))
            else:
                msg.config(text="Informe o nome do arquivo.", fg="red", font=("Helvetica", 10, "bold"))

        btnExportarDados = tk.Button(tela, text="Importar", command=importarDados, height=1, width=12, bg="darkgreen", fg="#ffffff", relief=tk.FLAT, font=("Helvetica", 12, "bold"), cursor="hand2")
        btnExportarDados.pack(pady=20, anchor="center")

        msg = tk.Label(tela, text="", fg="black")
        msg.pack()

        this.mostrarTela(tela)
    

 # 8 - Encerra a execução   
    def sair(this):
        if messagebox.askokcancel("Sair", "Deseja realmente sair da aplicação?"):
            this.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ControleTurmasApp(root)
    root.mainloop()
