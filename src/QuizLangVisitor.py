# Generated from QuizLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QuizLangParser import QuizLangParser
else:
    from QuizLangParser import QuizLangParser

# This class defines a complete generic visitor for a parse tree produced by QuizLangParser.

class QuizLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuizLangParser#quiz.
    def visitQuiz(self, ctx:QuizLangParser.QuizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#metadados.
    def visitMetadados(self, ctx:QuizLangParser.MetadadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#secoes.
    def visitSecoes(self, ctx:QuizLangParser.SecoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#secao.
    def visitSecao(self, ctx:QuizLangParser.SecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#item.
    def visitItem(self, ctx:QuizLangParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#mcq.
    def visitMcq(self, ctx:QuizLangParser.McqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#pergunta.
    def visitPergunta(self, ctx:QuizLangParser.PerguntaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#opcoes.
    def visitOpcoes(self, ctx:QuizLangParser.OpcoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#discursiva.
    def visitDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuizLangParser#numerica.
    def visitNumerica(self, ctx:QuizLangParser.NumericaContext):
        return self.visitChildren(ctx)



del QuizLangParser