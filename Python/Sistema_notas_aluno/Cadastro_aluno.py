import csv

class Aluno:
    def __init__(self):
        self.alunos = {}

    def formatar(self, msg):
        tamanho = len(msg)
        print('_' * tamanho)
        print(msg)
        print('_' * tamanho)

    def obter_idade(self):
        while True:
            try:
                idade = int(input('Informe a idade do aluno: '))
                if idade > 0:
                    return idade
                else:
                    self.formatar('Idade inválida. A idade deve ser maior do que zero')
            except ValueError:
                self.formatar('Entrada inválida')
    
    def obter_nota(self):
        while True:
            try:
                nota = float(input('Informe a nota do aluno: '))
                if nota > 0:
                    return nota
                else:
                    self.formatar('Nota inválida. Insira uma nota superior a zero')
            except ValueError:
                self.formatar('Entrada inválida')

    def cadastro_aluno(self):
        nome = input('Informe o nome do aluno: ').capitalize()
        if nome in self.alunos:
            self.formatar('O(a) Aluno(a) ja consta no sistema')
        else:
            idade = self.obter_idade()
            nota_final = self.obter_nota()
            self.alunos[nome] = (idade, nota_final)
            self.formatar(f'Aluno(a) {nome} foi cadastrado com sucesso')

            with open('Alunos.csv', 'a', encoding='utf-8') as arquivo:
                for nome, (idade, nota_final) in self.alunos.items():
                    status = 'aprovado' if nota_final >= 7 else 'reprovado'
                    arquivo.write(f"""Nome: {nome}\nidade: {idade}\nNota: {nota_final}\nStatus: {status}\n\n""")
        
    def procurar_aluno(self):
        busca = input('Informe o nome que deseja buscar: ')
        try:
            with open('Alunos.csv', 'r', encoding='utf-8') as arquivo:
                alunos = []
                localizado = False

                for linha in arquivo:
                    if linha.startswith('Nome: '):
                        nome = linha.split(': ')[1].strip()
                        if nome.lower() == busca.lower():
                            localizado = True
                            alunos.append(linha.strip())
                    elif localizado:
                        if linha.strip():
                            alunos.append(linha.strip())
                        else:
                            break
                    
                if localizado:
                    self.formatar('\n'.join(alunos) if alunos else "Nenhum dado encontrado.")
                else:
                    self.formatar('Aluno não consta no sistema')

        except FileNotFoundError:
            self.formatar('Arquivo inexistente ou não encontrado')
        
    
    def exibir_alunos(self):
        try:
            with open('Alunos.csv', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read().strip()
                if conteudo:
                    self.formatar(conteudo)
                else:
                    self.formatar('O arquivo está vazio')
        except FileNotFoundError:
            self.formatar('Arquivo inexistente ou não encontrado')


alunos = Aluno()

while True:
    alunos.formatar("""
    [1] - Cadastrar aluno
    [2] - Buscar aluno
    [3] - Exibir Alunos
    [4] - Sair""")

    try:
        opção = int(input('Escolha uma opção: '))

        if opção == 1:
            alunos.cadastro_aluno()
        elif opção == 2:
            alunos.procurar_aluno()
        elif opção == 3:
            alunos.exibir_alunos()
        elif opção == 4:
            alunos.formatar('Encerrando o programa')
            break
        else:
            alunos.formatar('Opção inválida')
    except ValueError:
        alunos.formatar('Dado inválido')