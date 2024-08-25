from Models.DTODeAluno import Aluno

class OperacoesTurma:
    def __init__(this):
        this.alunos = []

    def cadastrarAluno(this, ra, nome, nota):
        aluno = Aluno(str(ra), nome, float(nota))
        this.alunos.append(aluno)
        print("Aluno cadastrado com sucesso.")
        for aluno in this.alunos:
            print(aluno.ra, aluno.nome, aluno.nota)

    def editarAluno(this, ra, novoNome, novaNota):
        aluno = this.buscarAluno(ra)
        aluno.nome = novoNome
        aluno.nota = float(novaNota)
    
    def excluirAluno(this, ra):
        aluno = this.buscarAluno(ra)
        this.alunos.remove(aluno)

    def buscarAluno(this, ra):
        for aluno in this.alunos:
            if(aluno.ra == ra):
                return aluno

    def ExisteRA(this, ra):
        for aluno in this.alunos:
            if(aluno.ra == ra):
                return True
        return False

    def getQuantidadeAlunos(this):
        return len(this.alunos)

    def getAlunoMaiorNota(this):
        if not this.alunos:
            return None
        alunoMaiorNota = max(this.alunos, key=lambda aluno: aluno.nota)
        return alunoMaiorNota

    def getAlunoMenorNota(this):
        if not this.alunos:
            return None
        alunoMenorNota = min(this.alunos, key=lambda aluno: aluno.nota)
        return alunoMenorNota
    
    def getMediaNotasTurma(this):
        if not this.alunos:
            return 0
        totalNotas = sum(aluno.nota for aluno in this.alunos)
        mediaNotas = totalNotas / len(this.alunos)
        return mediaNotas

    def exportarDados(this, nomeArquivo):
        with open(nomeArquivo, "w") as arquivo:
            for aluno in this.alunos:
                arquivo.write(f"{aluno.ra}|{aluno.nome}|{str(aluno.nota)}\n")

    def importarDados(this, nomeArquivo):
        this.alunos = []
        
        with open(nomeArquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split("|")
                ra, nome, nota = str(dados[0]), dados[1], float(dados[2])
                this.cadastrarAluno(ra, nome, nota)