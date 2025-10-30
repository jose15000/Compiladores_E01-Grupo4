
# Relatório Acadêmico: Implementação de um Compilador para QuizLang

## 1. Introdução

Este relatório detalha a implementação de um compilador para a **QuizLang**, uma linguagem de domínio específico (DSL) projetada para a criação de quizzes. O compilador foi desenvolvido como um projeto acadêmico na disciplina de Compiladores, utilizando ferramentas como ANTLR para a geração dos analisadores léxico e sintático, e Python para a implementação das análises subsequentes e da lógica principal.

A QuizLang permite que usuários definam a estrutura de um quiz, incluindo metadados, seções e diferentes tipos de questões (múltipla escolha, discursiva e numérica), de forma declarativa e legível. O objetivo do compilador é validar a estrutura e a semântica de um arquivo QuizLang e, em caso de sucesso, fornecer uma representação estruturada do quiz.

## 2. Análise Léxica

A fase de análise léxica é responsável por converter a sequência de caracteres do código-fonte em uma sequência de tokens. A especificação dos tokens da QuizLang foi definida na gramática `QuizLang.g4` e é processada pelo ANTLR.

Os principais tokens da linguagem incluem:

*   **Palavras-chave:** `quiz`, `titulo`, `tempo`, `secao`, `mcq`, `pergunta`, `opcoes`, `resposta`, `discursiva`, `palavras`, `numerica`, `intervalo`.
*   **Identificadores:** `ID` (e.g., nomes de quizzes e questões).
*   **Literais:** `STRING` (para textos como títulos e perguntas) e `NUMBER` (para valores como tempo e limites).
*   **Símbolos e Delimitadores:** `{`, `}`, `[`, `]`, `:`, `,`, `-`.
*   **Comentários e Espaços em Branco:** São ignorados pelo analisador.

## 3. Análise Sintática

A análise sintática verifica se a sequência de tokens gerada pelo analisador léxico obedece à estrutura gramatical da QuizLang. A gramática, também definida em `QuizLang.g4`, estabelece a hierarquia e a ordem das declarações.

A estrutura de um arquivo QuizLang é a seguinte:

1.  **Quiz:** O elemento raiz, definido pela palavra-chave `quiz`, um ID e um bloco de conteúdo.
2.  **Metadados:** Um bloco que contém o `titulo` (uma string) e o `tempo` (um número) do quiz.
3.  **Seções:** Um quiz pode conter uma ou mais seções, cada uma com um nome (string) e um bloco contendo questões.
4.  **Itens (Questões):** Dentro de uma seção, podem ser definidos três tipos de questões:
    *   `mcq`: Múltipla escolha, com uma pergunta, uma lista de opções e uma resposta correta.
    *   `discursiva`: Questão aberta, com uma pergunta e um limite de `palavras`.
    *   `numerica`: Questão de resposta numérica, com uma pergunta e um `intervalo` de valores válidos.

O ANTLR gera um `Parser` e uma árvore sintática (`Parse Tree`) que representa a estrutura do código-fonte. Se o código for sintaticamente inválido, o compilador reporta o erro e interrompe a execução.

## 4. Análise Semântica

A análise semântica é a fase mais complexa e é responsável por verificar o "significado" do código, garantindo que ele faça sentido de acordo com as regras da linguagem. Esta fase foi implementada em Python, utilizando o padrão de projeto *Visitor* (`QuizLangVisitor`) para percorrer a árvore sintática gerada pelo ANTLR.

As principais verificações semânticas implementadas são:

*   **Gerenciamento de Escopo e Símbolos:** O analisador utiliza uma Tabela de Símbolos para registrar todos os identificadores (IDs de quizzes, seções e questões) e suas informações associadas, como tipo e escopo.
*   **Verificação de Redefinição:** Garante que não haja identificadores duplicados no mesmo escopo. Por exemplo, duas questões não podem ter o mesmo ID dentro da mesma seção.
*   **Validação de Questões de Múltipla Escolha (`mcq`):**
    *   A resposta correta deve estar presente na lista de opções.
    *   As opções não podem ser duplicadas.
    *   A questão deve ter no mínimo duas opções.
*   **Validação de Questões Numéricas (`numerica`):**
    *   O valor inicial do intervalo não pode ser maior que o valor final.
*   **Validação de Questões Discursivas (`discursiva`):**
    *   O limite de palavras deve ser um número positivo.
*   **Avisos:** O analisador emite um aviso se uma seção for declarada, mas não contiver nenhuma questão.

### 4.1. Tabela de Símbolos

A Tabela de Símbolos (`SymbolTable`) é uma estrutura de dados central para a análise semântica. Ela foi implementada como uma classe em Python e armazena informações sobre cada símbolo (identificador) encontrado no código.

*   **Estrutura:** A tabela é um dicionário onde a chave é uma tupla `(escopo, nome_do_simbolo)`. Isso permite que um mesmo nome seja usado em escopos diferentes (por exemplo, `Q1` na `Secao1` e `Q1` na `Secao2`).
*   **Gerenciamento de Escopo:** A tabela mantém uma pilha de escopos (`scope_stack`) para rastrear o escopo atual. Ao entrar em uma nova estrutura (como um quiz ou uma seção), um novo escopo é empilhado. Ao sair, ele é desempilhado.
*   **Operações:** As operações fundamentais são `define` (para adicionar um novo símbolo ao escopo atual, verificando se ele já existe) e `lookup` (para procurar por um símbolo, começando do escopo atual e subindo na hierarquia até o escopo global).

## 5. Conclusão

O compilador para QuizLang implementado cumpre com sucesso os requisitos de análise léxica, sintática e semântica para a linguagem proposta. A utilização do ANTLR acelerou o desenvolvimento das fases iniciais, permitindo um foco maior na lógica semântica, que foi implementada de forma robusta em Python.

O projeto demonstra a aplicação prática dos conceitos de teoria da compilação, como a construção de gramáticas, a geração de árvores sintáticas, o gerenciamento de escopos com tabelas de símbolos e a implementação de validações semânticas através do padrão Visitor.

Como trabalhos futuros, o compilador poderia ser estendido para gerar código em algum formato de destino, como JSON, XML ou HTML, transformando a definição do quiz em um formato executável ou visualizável.
