class Estudante:
    def __init__(self, nome, idade, notas, id_unico):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        self.id_unico = id_unico

    def __str__(self):
        return f"\tNome: {self.nome} \n\tIdade: {self.idade} \n\tID: {self.id_unico}\n"

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota

class TurmaEstudantes:
    def __init__(self):
        self.estudantes = []

    def __str__(self):
        return f"A turma contém {len(self.estudantes)} alunos! \n"

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, id):
        for aluno in self.estudantes:
            if aluno.id_unico == id:
                self.estudantes.remove(aluno)
                return f"Id: {id}, '{aluno.nome}' removido da turma! "
        return f"ID: {id}, não encontrada na turma! "

    def media_da_turma(self, disciplina):
        nota_parcial = 0
        divisor_media = 0
        for aluno in self.estudantes:
            if disciplina in aluno.notas:
                divisor_media += 1
                nota_parcial += aluno.notas[disciplina]
        if divisor_media == 0:
            return f"Nenhuma nota encontrada para a disciplina '{disciplina}'."
        else:
            nota_media = nota_parcial / divisor_media
            return f"A média de notas dos {divisor_media} alunos em '{disciplina}' é: {nota_media:.1f}"

    def melhor_estudante(self, disciplina):
        melhor_aluno = None
        maior_nota = -1
        for aluno in self.estudantes:
            if disciplina in aluno.notas and aluno.notas[disciplina] > maior_nota:
                melhor_aluno = aluno
                maior_nota = aluno.notas[disciplina]
        if melhor_aluno:
            return f"Aluno: {melhor_aluno.nome}, tem a maior nota em '{disciplina}': {maior_nota:.1f}"
        else:
            return f"Nenhum aluno possui nota em '{disciplina}'."

    def informacoes(self, estudante):
        return f"Informações do estudante: \n{estudante}"


joao = Estudante("João", 19, {"Matemática": 7.9, "História": 8.5}, "001")
Goku = Estudante("Goku", 30, {"Matemática": 9, "História": 8.8}, "002")
Bolsonaro = Estudante("Bolsonaro", 16, {"Matemática": 9.1, "História": 7.5}, "003")
lula = Estudante("lula", 20, {"Matemática": 8, "História": 9.2}, "004")

turma_ltp1 = TurmaEstudantes()

turma_ltp1.adicionar_estudante(joao)
turma_ltp1.adicionar_estudante(lula) 
turma_ltp1.adicionar_estudante(Bolsonaro)
turma_ltp1.adicionar_estudante(Goku)

print(turma_ltp1.media_da_turma("História"))
print(turma_ltp1.melhor_estudante("Matemática"))
print(turma_ltp1.remover_estudante("001"))

print(turma_ltp1.media_da_turma("História"))
print(turma_ltp1.informacoes(Goku))
joao.adicionar_nota("Geografia", 9.5)
print(turma_ltp1.informacoes(Bolsonaro))
print(turma_ltp1.melhor_estudante("Geografia"))
