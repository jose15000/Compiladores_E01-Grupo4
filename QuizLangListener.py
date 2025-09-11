# Generated from QuizLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QuizLangParser import QuizLangParser
else:
    from QuizLangParser import QuizLangParser

# This class defines a complete listener for a parse tree produced by QuizLangParser.
class QuizLangListener(ParseTreeListener):

    # Enter a parse tree produced by QuizLangParser#quiz.
    def enterQuiz(self, ctx:QuizLangParser.QuizContext):
        pass

    # Exit a parse tree produced by QuizLangParser#quiz.
    def exitQuiz(self, ctx:QuizLangParser.QuizContext):
        pass


    # Enter a parse tree produced by QuizLangParser#metadados.
    def enterMetadados(self, ctx:QuizLangParser.MetadadosContext):
        pass

    # Exit a parse tree produced by QuizLangParser#metadados.
    def exitMetadados(self, ctx:QuizLangParser.MetadadosContext):
        pass


    # Enter a parse tree produced by QuizLangParser#secoes.
    def enterSecoes(self, ctx:QuizLangParser.SecoesContext):
        pass

    # Exit a parse tree produced by QuizLangParser#secoes.
    def exitSecoes(self, ctx:QuizLangParser.SecoesContext):
        pass


    # Enter a parse tree produced by QuizLangParser#secao.
    def enterSecao(self, ctx:QuizLangParser.SecaoContext):
        pass

    # Exit a parse tree produced by QuizLangParser#secao.
    def exitSecao(self, ctx:QuizLangParser.SecaoContext):
        pass


    # Enter a parse tree produced by QuizLangParser#item.
    def enterItem(self, ctx:QuizLangParser.ItemContext):
        pass

    # Exit a parse tree produced by QuizLangParser#item.
    def exitItem(self, ctx:QuizLangParser.ItemContext):
        pass


    # Enter a parse tree produced by QuizLangParser#mcq.
    def enterMcq(self, ctx:QuizLangParser.McqContext):
        pass

    # Exit a parse tree produced by QuizLangParser#mcq.
    def exitMcq(self, ctx:QuizLangParser.McqContext):
        pass


    # Enter a parse tree produced by QuizLangParser#pergunta.
    def enterPergunta(self, ctx:QuizLangParser.PerguntaContext):
        pass

    # Exit a parse tree produced by QuizLangParser#pergunta.
    def exitPergunta(self, ctx:QuizLangParser.PerguntaContext):
        pass


    # Enter a parse tree produced by QuizLangParser#opcoes.
    def enterOpcoes(self, ctx:QuizLangParser.OpcoesContext):
        pass

    # Exit a parse tree produced by QuizLangParser#opcoes.
    def exitOpcoes(self, ctx:QuizLangParser.OpcoesContext):
        pass


    # Enter a parse tree produced by QuizLangParser#discursiva.
    def enterDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        pass

    # Exit a parse tree produced by QuizLangParser#discursiva.
    def exitDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        pass


    # Enter a parse tree produced by QuizLangParser#numerica.
    def enterNumerica(self, ctx:QuizLangParser.NumericaContext):
        pass

    # Exit a parse tree produced by QuizLangParser#numerica.
    def exitNumerica(self, ctx:QuizLangParser.NumericaContext):
        pass



del QuizLangParser