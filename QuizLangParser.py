# Generated from QuizLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,2,4,2,35,8,2,11,2,12,2,36,1,3,1,3,1,3,1,3,5,3,43,
        8,3,10,3,12,3,46,9,3,1,3,1,3,1,4,1,4,1,4,3,4,53,8,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,71,8,7,10,
        7,12,7,74,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,88,
        0,20,1,0,0,0,2,28,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,52,1,0,0,0,
        10,54,1,0,0,0,12,62,1,0,0,0,14,65,1,0,0,0,16,77,1,0,0,0,18,84,1,
        0,0,0,20,21,5,1,0,0,21,22,5,14,0,0,22,23,5,17,0,0,23,24,3,2,1,0,
        24,25,3,4,2,0,25,26,5,18,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,
        2,0,0,29,30,5,15,0,0,30,31,5,3,0,0,31,32,5,16,0,0,32,3,1,0,0,0,33,
        35,3,6,3,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,
        0,37,5,1,0,0,0,38,39,5,5,0,0,39,40,5,15,0,0,40,44,5,17,0,0,41,43,
        3,8,4,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,18,0,0,48,7,1,0,0,0,49,53,3,
        10,5,0,50,53,3,16,8,0,51,53,3,18,9,0,52,49,1,0,0,0,52,50,1,0,0,0,
        52,51,1,0,0,0,53,9,1,0,0,0,54,55,5,6,0,0,55,56,5,14,0,0,56,57,5,
        21,0,0,57,58,3,12,6,0,58,59,3,14,7,0,59,60,5,9,0,0,60,61,5,15,0,
        0,61,11,1,0,0,0,62,63,5,7,0,0,63,64,5,15,0,0,64,13,1,0,0,0,65,66,
        5,8,0,0,66,67,5,19,0,0,67,72,5,15,0,0,68,69,5,22,0,0,69,71,5,15,
        0,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,
        1,0,0,0,74,72,1,0,0,0,75,76,5,20,0,0,76,15,1,0,0,0,77,78,5,10,0,
        0,78,79,5,14,0,0,79,80,5,21,0,0,80,81,3,12,6,0,81,82,5,11,0,0,82,
        83,5,16,0,0,83,17,1,0,0,0,84,85,5,12,0,0,85,86,5,14,0,0,86,87,5,
        21,0,0,87,88,3,12,6,0,88,89,5,13,0,0,89,90,5,16,0,0,90,91,5,23,0,
        0,91,92,5,16,0,0,92,19,1,0,0,0,4,36,44,52,72
    ]

class QuizLangParser ( Parser ):

    grammarFileName = "QuizLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'quiz'", "'titulo'", "'tempo'", "'secoes'", 
                     "'secao'", "'mcq'", "'pergunta'", "'opcoes'", "'resposta'", 
                     "'discursiva'", "'palavras'", "'numerica'", "'intervalo'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{'", "'}'", 
                     "'['", "']'", "':'", "','", "'-'" ]

    symbolicNames = [ "<INVALID>", "QUIZ", "TITULO", "TEMPO", "SECOES", 
                      "SECAO", "MCQ", "PERGUNTA", "OPCOES", "RESPOSTA", 
                      "DISCURSIVA", "PALAVRAS", "NUMERICA", "INTERVALO", 
                      "ID", "STRING", "NUMBER", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COLON", "COMMA", "HYPHEN", "COMMENT", "WS" ]

    RULE_quiz = 0
    RULE_metadados = 1
    RULE_secoes = 2
    RULE_secao = 3
    RULE_item = 4
    RULE_mcq = 5
    RULE_pergunta = 6
    RULE_opcoes = 7
    RULE_discursiva = 8
    RULE_numerica = 9

    ruleNames =  [ "quiz", "metadados", "secoes", "secao", "item", "mcq", 
                   "pergunta", "opcoes", "discursiva", "numerica" ]

    EOF = Token.EOF
    QUIZ=1
    TITULO=2
    TEMPO=3
    SECOES=4
    SECAO=5
    MCQ=6
    PERGUNTA=7
    OPCOES=8
    RESPOSTA=9
    DISCURSIVA=10
    PALAVRAS=11
    NUMERICA=12
    INTERVALO=13
    ID=14
    STRING=15
    NUMBER=16
    LBRACE=17
    RBRACE=18
    LBRACK=19
    RBRACK=20
    COLON=21
    COMMA=22
    HYPHEN=23
    COMMENT=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QuizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUIZ(self):
            return self.getToken(QuizLangParser.QUIZ, 0)

        def ID(self):
            return self.getToken(QuizLangParser.ID, 0)

        def LBRACE(self):
            return self.getToken(QuizLangParser.LBRACE, 0)

        def metadados(self):
            return self.getTypedRuleContext(QuizLangParser.MetadadosContext,0)


        def secoes(self):
            return self.getTypedRuleContext(QuizLangParser.SecoesContext,0)


        def RBRACE(self):
            return self.getToken(QuizLangParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(QuizLangParser.EOF, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_quiz

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuiz" ):
                return visitor.visitQuiz(self)
            else:
                return visitor.visitChildren(self)




    def quiz(self):

        localctx = QuizLangParser.QuizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_quiz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(QuizLangParser.QUIZ)
            self.state = 21
            self.match(QuizLangParser.ID)
            self.state = 22
            self.match(QuizLangParser.LBRACE)
            self.state = 23
            self.metadados()
            self.state = 24
            self.secoes()
            self.state = 25
            self.match(QuizLangParser.RBRACE)
            self.state = 26
            self.match(QuizLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITULO(self):
            return self.getToken(QuizLangParser.TITULO, 0)

        def STRING(self):
            return self.getToken(QuizLangParser.STRING, 0)

        def TEMPO(self):
            return self.getToken(QuizLangParser.TEMPO, 0)

        def NUMBER(self):
            return self.getToken(QuizLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_metadados

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadados" ):
                return visitor.visitMetadados(self)
            else:
                return visitor.visitChildren(self)




    def metadados(self):

        localctx = QuizLangParser.MetadadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_metadados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(QuizLangParser.TITULO)
            self.state = 29
            self.match(QuizLangParser.STRING)
            self.state = 30
            self.match(QuizLangParser.TEMPO)
            self.state = 31
            self.match(QuizLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def secao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuizLangParser.SecaoContext)
            else:
                return self.getTypedRuleContext(QuizLangParser.SecaoContext,i)


        def getRuleIndex(self):
            return QuizLangParser.RULE_secoes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecoes" ):
                return visitor.visitSecoes(self)
            else:
                return visitor.visitChildren(self)




    def secoes(self):

        localctx = QuizLangParser.SecoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_secoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.secao()
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECAO(self):
            return self.getToken(QuizLangParser.SECAO, 0)

        def STRING(self):
            return self.getToken(QuizLangParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(QuizLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(QuizLangParser.RBRACE, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuizLangParser.ItemContext)
            else:
                return self.getTypedRuleContext(QuizLangParser.ItemContext,i)


        def getRuleIndex(self):
            return QuizLangParser.RULE_secao

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecao" ):
                return visitor.visitSecao(self)
            else:
                return visitor.visitChildren(self)




    def secao(self):

        localctx = QuizLangParser.SecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_secao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(QuizLangParser.SECAO)
            self.state = 39
            self.match(QuizLangParser.STRING)
            self.state = 40
            self.match(QuizLangParser.LBRACE)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5184) != 0):
                self.state = 41
                self.item()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(QuizLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mcq(self):
            return self.getTypedRuleContext(QuizLangParser.McqContext,0)


        def discursiva(self):
            return self.getTypedRuleContext(QuizLangParser.DiscursivaContext,0)


        def numerica(self):
            return self.getTypedRuleContext(QuizLangParser.NumericaContext,0)


        def getRuleIndex(self):
            return QuizLangParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = QuizLangParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.mcq()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.discursiva()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.numerica()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class McqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MCQ(self):
            return self.getToken(QuizLangParser.MCQ, 0)

        def ID(self):
            return self.getToken(QuizLangParser.ID, 0)

        def COLON(self):
            return self.getToken(QuizLangParser.COLON, 0)

        def pergunta(self):
            return self.getTypedRuleContext(QuizLangParser.PerguntaContext,0)


        def opcoes(self):
            return self.getTypedRuleContext(QuizLangParser.OpcoesContext,0)


        def RESPOSTA(self):
            return self.getToken(QuizLangParser.RESPOSTA, 0)

        def STRING(self):
            return self.getToken(QuizLangParser.STRING, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_mcq

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMcq" ):
                return visitor.visitMcq(self)
            else:
                return visitor.visitChildren(self)




    def mcq(self):

        localctx = QuizLangParser.McqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mcq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(QuizLangParser.MCQ)
            self.state = 55
            self.match(QuizLangParser.ID)
            self.state = 56
            self.match(QuizLangParser.COLON)
            self.state = 57
            self.pergunta()
            self.state = 58
            self.opcoes()
            self.state = 59
            self.match(QuizLangParser.RESPOSTA)
            self.state = 60
            self.match(QuizLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PerguntaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERGUNTA(self):
            return self.getToken(QuizLangParser.PERGUNTA, 0)

        def STRING(self):
            return self.getToken(QuizLangParser.STRING, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_pergunta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPergunta" ):
                return visitor.visitPergunta(self)
            else:
                return visitor.visitChildren(self)




    def pergunta(self):

        localctx = QuizLangParser.PerguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pergunta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(QuizLangParser.PERGUNTA)
            self.state = 63
            self.match(QuizLangParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPCOES(self):
            return self.getToken(QuizLangParser.OPCOES, 0)

        def LBRACK(self):
            return self.getToken(QuizLangParser.LBRACK, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(QuizLangParser.STRING)
            else:
                return self.getToken(QuizLangParser.STRING, i)

        def RBRACK(self):
            return self.getToken(QuizLangParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(QuizLangParser.COMMA)
            else:
                return self.getToken(QuizLangParser.COMMA, i)

        def getRuleIndex(self):
            return QuizLangParser.RULE_opcoes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcoes" ):
                return visitor.visitOpcoes(self)
            else:
                return visitor.visitChildren(self)




    def opcoes(self):

        localctx = QuizLangParser.OpcoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(QuizLangParser.OPCOES)
            self.state = 66
            self.match(QuizLangParser.LBRACK)
            self.state = 67
            self.match(QuizLangParser.STRING)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 68
                self.match(QuizLangParser.COMMA)
                self.state = 69
                self.match(QuizLangParser.STRING)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(QuizLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiscursivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISCURSIVA(self):
            return self.getToken(QuizLangParser.DISCURSIVA, 0)

        def ID(self):
            return self.getToken(QuizLangParser.ID, 0)

        def COLON(self):
            return self.getToken(QuizLangParser.COLON, 0)

        def pergunta(self):
            return self.getTypedRuleContext(QuizLangParser.PerguntaContext,0)


        def PALAVRAS(self):
            return self.getToken(QuizLangParser.PALAVRAS, 0)

        def NUMBER(self):
            return self.getToken(QuizLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_discursiva

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiscursiva" ):
                return visitor.visitDiscursiva(self)
            else:
                return visitor.visitChildren(self)




    def discursiva(self):

        localctx = QuizLangParser.DiscursivaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_discursiva)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(QuizLangParser.DISCURSIVA)
            self.state = 78
            self.match(QuizLangParser.ID)
            self.state = 79
            self.match(QuizLangParser.COLON)
            self.state = 80
            self.pergunta()
            self.state = 81
            self.match(QuizLangParser.PALAVRAS)
            self.state = 82
            self.match(QuizLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERICA(self):
            return self.getToken(QuizLangParser.NUMERICA, 0)

        def ID(self):
            return self.getToken(QuizLangParser.ID, 0)

        def COLON(self):
            return self.getToken(QuizLangParser.COLON, 0)

        def pergunta(self):
            return self.getTypedRuleContext(QuizLangParser.PerguntaContext,0)


        def INTERVALO(self):
            return self.getToken(QuizLangParser.INTERVALO, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(QuizLangParser.NUMBER)
            else:
                return self.getToken(QuizLangParser.NUMBER, i)

        def HYPHEN(self):
            return self.getToken(QuizLangParser.HYPHEN, 0)

        def getRuleIndex(self):
            return QuizLangParser.RULE_numerica

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumerica" ):
                return visitor.visitNumerica(self)
            else:
                return visitor.visitChildren(self)




    def numerica(self):

        localctx = QuizLangParser.NumericaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numerica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(QuizLangParser.NUMERICA)
            self.state = 85
            self.match(QuizLangParser.ID)
            self.state = 86
            self.match(QuizLangParser.COLON)
            self.state = 87
            self.pergunta()
            self.state = 88
            self.match(QuizLangParser.INTERVALO)
            self.state = 89
            self.match(QuizLangParser.NUMBER)
            self.state = 90
            self.match(QuizLangParser.HYPHEN)
            self.state = 91
            self.match(QuizLangParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





