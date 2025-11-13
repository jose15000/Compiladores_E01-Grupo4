import sys
import os
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from QuizLangLexer import QuizLangLexer
from QuizLangParser import QuizLangParser
from QuizLangVisitor import QuizLangVisitor
from SemanticAnalyzer import SemanticAnalyzer, SymbolTable
from QuizSimulator import QuizSimulator

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"LÉXICO/SINTAXE ERRO: linha {line}:{column} {msg}")

def pretty_print_tree(node, parser, indent=""):
    if (node is None):
        return
    if isinstance(node, TerminalNode):
        print(indent + f"TOKEN: '{node.getSymbol().text}'")
    else:
        print(indent + parser.ruleNames[node.getRuleIndex()])
        if hasattr(node, 'children') and node.children is not None:
            for child in node.children:
                pretty_print_tree(child, parser, indent + "  ")

class QuizVisitor(QuizLangVisitor):
 
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
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        # Se o caminho não for absoluto, constrói um caminho a partir do diretório pai do 'src'
        if not os.path.isabs(file_path):
            # Pega o caminho do diretório onde o main.py está (/.../src)
            script_dir = os.path.dirname(os.path.realpath(__file__))
            # Sobe um nível para a raiz do projeto e junta com o caminho do arquivo
            file_path = os.path.join(script_dir, '..', file_path)
        input_stream = FileStream(file_path, encoding='utf-8')
    else:
        print("Uso: python main.py <arquivo_de_teste>")
        return
    
    # Cria o analisador léxico
    lexer = QuizLangLexer(input_stream)
    
    # Cria o fluxo de tokens
    stream = CommonTokenStream(lexer)
    
    # Cria o analisador sintático
    parser = QuizLangParser(stream)
    
    # Remove o listener padrão e adiciona o customizado
    parser.removeErrorListeners()
    error_listener = SyntaxErrorListener()
    parser.addErrorListener(error_listener)
    
    # Inicia a análise a partir da regra 'quiz'
    tree = parser.quiz()

    # Verifica se foram encontrados erros
    if error_listener.errors:
        print("\n--- Erros Encontrados ---")
        for error in error_listener.errors:
            print(error)
        print("-------------------------")
    else:
        print("\n--- Análise Concluída Sem Erros ---")
        # Se não houver erros, pode prosseguir com a visitação
        print("\n--- Árvore de Análise Sintática ---")
        pretty_print_tree(tree, parser)
        print("-------------------------------------\n")

        # Análise Semântica
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.visit(tree)

        print(semantic_analyzer.report())
        
        # Apenas executa o visitor de impressão se não houver erros.
        has_errors = any(e.startswith("Erro:") for e in semantic_analyzer.errors)
        if not has_errors:
            print("\n--- Iniciando Simulação do Quiz ---")
            simulator = QuizSimulator()
            simulator.visit(tree) # Coleta os dados do quiz
            simulator.run() # Executa a simulação

if __name__ == '__main__':
    main()
