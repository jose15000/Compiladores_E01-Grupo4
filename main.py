import sys
from antlr4 import *
from QuizLangLexer import QuizLangLexer
from QuizLangParser import QuizLangParser
from QuizLangVisitor import QuizLangVisitor

# Exemplo de um quiz escrito na linguagem QuizLang
# Coloque este conteúdo em um arquivo, por ex. "exemplo.quiz"
quiz_de_exemplo = """
quiz Compiladores_Quiz_1 {
    titulo "Questionário de Compiladores"
    tempo 60

    secao "Análise Léxica" {
        mcq Q1:
            pergunta "O que faz um analisador léxico?"
            opcoes ["Agrupar caracteres em tokens", "Verificar a sintaxe", "Gerar código"]
            resposta "Agrupar caracteres em tokens"

        discursiva Q2:
            pergunta "Descreva o conceito de token."
            palavras 50
    }

    secao "Análise Sintática" {
        numerica Q3:
            pergunta "Qual o intervalo de portas para FTP?"
            intervalo 20 - 21
    }
}
"""

class QuizVisitor(QuizLangVisitor):
    """
    Esta classe visitor percorre a árvore sintática gerada pelo ANTLR
    e extrai as informações do quiz de forma estruturada.
    """
    def visitQuiz(self, ctx:QuizLangParser.QuizContext):
        quiz_id = ctx.ID().getText()
        print(f"Iniciando análise do Quiz: {quiz_id}")
        
        # Visita os nós filhos (metadados e secoes)
        self.visit(ctx.metadados())
        self.visit(ctx.secoes())
        print(f"\nAnálise do Quiz '{quiz_id}' concluída com sucesso!")

    def visitMetadados(self, ctx:QuizLangParser.MetadadosContext):
        titulo = ctx.STRING().getText().strip('"')
        tempo = ctx.NUMBER().getText()
        print(f"\nTítulo: {titulo}")
        print(f"Tempo Limite: {tempo} minutos")

    def visitSecao(self, ctx:QuizLangParser.SecaoContext):
        nome_secao = ctx.STRING().getText().strip('"')
        print(f"\n--- Seção: {nome_secao} ---")
        # Itera sobre cada item (questão) dentro da seção
        for item_ctx in ctx.item():
            self.visit(item_ctx)

    def visitMcq(self, ctx:QuizLangParser.McqContext):
        question_id = ctx.ID().getText()
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        
        # Extrai as opções da lista
        opcoes = [opt.getText().strip('"') for opt in ctx.opcoes().STRING()]
        
        resposta = ctx.STRING().getText().strip('"')
        
        print(f"  [Múltipla Escolha - {question_id}] {pergunta}")
        print(f"    Opções: {opcoes}")
        print(f"    Resposta Correta: {resposta}")

    def visitDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        question_id = ctx.ID().getText()
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        palavras = ctx.NUMBER().getText()
        
        print(f"  [Discursiva - {question_id}] {pergunta}")
        print(f"    Limite de palavras: {palavras}")

    def visitNumerica(self, ctx:QuizLangParser.NumericaContext):
        question_id = ctx.ID().getText()
        pergunta = ctx.pergunta().STRING().getText().strip('"')
        
        # Pega os dois números do intervalo
        inicio_intervalo = ctx.NUMBER(0).getText()
        fim_intervalo = ctx.NUMBER(1).getText()

        print(f"  [Numérica - {question_id}] {pergunta}")
        print(f"    Resposta no intervalo: {inicio_intervalo}-{fim_intervalo}")


def main():
    # Cria o fluxo de entrada a partir da string de exemplo
    input_stream = InputStream(quiz_de_exemplo)
    
    # Cria o analisador léxico
    lexer = QuizLangLexer(input_stream)
    
    # Cria o fluxo de tokens
    stream = CommonTokenStream(lexer)
    
    # Cria o analisador sintático
    parser = QuizLangParser(stream)
    
    # Define um tratador de erros customizado (opcional, mas recomendado)
    # parser.removeErrorListeners() # Descomente se quiser remover os listeners padrão
    # parser.addErrorListener(MyErrorListener())
    
    try:
        # Inicia a análise a partir da regra 'quiz'
        tree = parser.quiz()
        
        # Cria o visitor e inicia a visitação da árvore
        visitor = QuizVisitor()
        visitor.visit(tree)

    except Exception as e:
        print(f"Ocorreu um erro durante a análise: {e}")

if __name__ == '__main__':
    main()