grammar QuizLang;

// Regra inicial (Parser)
quiz: QUIZ ID LBRACE metadados secoes RBRACE EOF;

metadados: TITULO STRING TEMPO NUMBER;
secoes: secao+;
secao: SECAO STRING LBRACE item* RBRACE;
item: mcq | discursiva | numerica;

mcq: MCQ ID ':' pergunta opcoes RESPOSTA STRING;
pergunta: PERGUNTA STRING;
opcoes: OPCOES LBRACK STRING (',' STRING)* RBRACK;
discursiva: DISCURSIVA ID ':' pergunta PALAVRAS NUMBER;
numerica: NUMERICA ID ':' pergunta INTERVALO NUMBER '-' NUMBER;

// Tokens (Lexer)
QUIZ: 'quiz';
TITULO: 'titulo';
TEMPO: 'tempo';
SECOES: 'secoes';
SECAO: 'secao';
MCQ: 'mcq';
PERGUNTA: 'pergunta';
OPCOES: 'opcoes';
RESPOSTA: 'resposta';
DISCURSIVA: 'discursiva';
PALAVRAS: 'palavras';
NUMERICA: 'numerica';
INTERVALO: 'intervalo';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' (~["\r\n])* '"';
NUMBER: [0-9]+;

LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
COLON: ':';
COMMA: ',';
HYPHEN: '-';

WS: [ \t\r\n]+ -> skip; // Ignora espaços em branco, tabulações e quebras de linha