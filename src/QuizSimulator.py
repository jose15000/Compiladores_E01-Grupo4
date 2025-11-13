from QuizLangVisitor import QuizLangVisitor
from QuizLangParser import QuizLangParser
import time

class QuizSimulator(QuizLangVisitor):
    def __init__(self):
        self.quiz_data = {
            'titulo': '',
            'tempo': 0,
            'secoes': []
        }
        self.score = 0
        self.total_questions = 0

    def visitMetadados(self, ctx:QuizLangParser.MetadadosContext):
        self.quiz_data['titulo'] = ctx.STRING().getText().strip('"')
        self.quiz_data['tempo'] = int(ctx.NUMBER().getText())

    def visitSecao(self, ctx:QuizLangParser.SecaoContext):
        secao_nome = ctx.STRING().getText().strip('"')
        secao_data = {'nome': secao_nome, 'questoes': []}
        self.quiz_data['secoes'].append(secao_data)
        self.visitChildren(ctx)

    def visitMcq(self, ctx:QuizLangParser.McqContext):
        self.total_questions += 1
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        opcoes = [opt.getText().strip('"') for opt in ctx.opcoes().STRING()]
        resposta_correta = ctx.STRING().getText().strip('"')
        
        questao = {
            'tipo': 'mcq',
            'pergunta': pergunta,
            'opcoes': opcoes,
            'resposta': resposta_correta
        }
        self.quiz_data['secoes'][-1]['questoes'].append(questao)

    def visitDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        self.total_questions += 1
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        limite_palavras = int(ctx.NUMBER().getText())
        
        questao = {
            'tipo': 'discursiva',
            'pergunta': pergunta,
            'limite_palavras': limite_palavras
        }
        self.quiz_data['secoes'][-1]['questoes'].append(questao)

    def visitNumerica(self, ctx:QuizLangParser.NumericaContext):
        self.total_questions += 1
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        inicio = int(ctx.NUMBER(0).getText())
        fim = int(ctx.NUMBER(1).getText())
        
        questao = {
            'tipo': 'numerica',
            'pergunta': pergunta,
            'intervalo': (inicio, fim)
        }
        self.quiz_data['secoes'][-1]['questoes'].append(questao)

    def run(self):
        print("="*50)
        print(f"Bem-vindo ao Quiz: {self.quiz_data['titulo']}")
        print(f"Você tem {self.quiz_data['tempo']} minutos para concluir.")
        print("="*50)
        input("Pressione Enter para começar...")

        start_time = time.time()

        for secao in self.quiz_data['secoes']:
            print(f"\n--- Iniciando Seção: {secao['nome']} ---")
            for i, questao in enumerate(secao['questoes']):
                print(f"\nQ{i+1}: {questao['pergunta']}")
                
                if questao['tipo'] == 'mcq':
                    for j, opt in enumerate(questao['opcoes']):
                        print(f"  {j+1}. {opt}")
                    resposta_usuario = input("Sua resposta (digite o texto da opção): ")
                    if resposta_usuario.strip().lower() == questao['resposta'].lower():
                        print("Correto!")
                        self.score += 1
                    else:
                        print(f"Incorreto. A resposta era: {questao['resposta']}")

                elif questao['tipo'] == 'discursiva':
                    resposta_usuario = input(f"Sua resposta (tente usar até {questao['limite_palavras']} palavras): ")
                    contagem_palavras = len(resposta_usuario.split())
                    print(f"Resposta registrada com {contagem_palavras} palavras. (Avaliação manual necessária)")
                    self.score += 1 # Pontua pela participação

                elif questao['tipo'] == 'numerica':
                    resposta_usuario = int(input("Sua resposta (número inteiro): "))
                    inicio, fim = questao['intervalo']
                    if inicio <= resposta_usuario <= fim:
                        print("Correto!")
                        self.score += 1
                    else:
                        print(f"Incorreto. A resposta deveria estar no intervalo {inicio}-{fim}.")

        end_time = time.time()
        print("\n" + "="*50)
        print("Quiz Finalizado!")
        print(f"Sua pontuação: {self.score}/{self.total_questions}")
        print(f"Tempo total: {round(end_time - start_time, 2)} segundos.")
        print("="*50)