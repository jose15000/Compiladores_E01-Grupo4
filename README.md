
# Compilador para QuizLang

## 1. Introdução

Este projeto apresenta um compilador completo para a **QuizLang**, uma linguagem de domínio específico (DSL) projetada para a criação de quizzes. O compilador foi desenvolvido utilizando ANTLR para a geração dos analisadores léxico e sintático, e Python para a implementação da análise semântica e da simulação interativa do quiz.

A QuizLang permite que usuários definam a estrutura de um quiz, incluindo metadados, seções e diferentes tipos de questões (múltipla escolha, discursiva e numérica), de forma declarativa e legível. O objetivo do compilador é validar a estrutura e a semântica de um arquivo QuizLang e, em caso de sucesso, fornecer uma representação estruturada do quiz.

## 2. Como Executar

Para executar o compilador e o simulador de quiz, siga os passos abaixo.

### Pré-requisitos
- Python 3.x
- Java Development Kit (JDK) (necessário para o ANTLR, caso precise gerar os fontes do parser novamente)

### Instalação e Execução

1.  **Ative o ambiente virtual:**
    O projeto já inclui um ambiente virtual chamado `myenv`. Ative-o com o seguinte comando:
    ```bash
    source myenv/bin/activate
    ```

2.  **Instale as dependências:**
    A única dependência Python é o runtime do ANTLR. Instale-o com:
    ```bash
    pip install antlr4-python3-runtime
    ```

3.  **Execute o compilador:**
    Para analisar e simular um arquivo de quiz (por exemplo, `teste_ok.txt`), execute o `main.py`:
    ```bash
    python3 main.py teste_ok.txt
    ```
    O programa irá validar o arquivo e, se não houver erros, iniciará a simulação interativa no terminal.

## 3. Análise Léxica

A fase de análise léxica é responsável por converter a sequência de caracteres do código-fonte em uma sequência de tokens. A especificação dos tokens da QuizLang foi definida na gramática `QuizLang.g4` e é processada pelo ANTLR.

Os principais tokens da linguagem incluem:

*   **Palavras-chave:** `quiz`, `titulo`, `tempo`, `secao`, `mcq`, `pergunta`, `opcoes`, `resposta`, `discursiva`, `palavras`, `numerica`, `intervalo`.
*   **Identificadores:** `ID` (e.g., nomes de quizzes e questões).
*   **Literais:** `STRING` (para textos como títulos e perguntas) e `NUMBER` (para valores como tempo e limites).
*   **Símbolos e Delimitadores:** `{`, `}`, `[`, `]`, `:`, `,`, `-`.
*   **Comentários e Espaços em Branco:** São ignorados pelo analisador.

## 4. Análise Sintática

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

## 5. Análise Semântica

A análise semântica é responsável por verificar o "significado" do código, garantindo que ele faça sentido de acordo com as regras da linguagem. Esta fase foi implementada em Python no arquivo `SemanticAnalyzer.py`, utilizando o padrão de projeto *Visitor* para percorrer a árvore sintática.

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

## 6. Simulação (Execução)

Após a conclusão bem-sucedida de todas as fases de análise, o compilador entra na fase de execução. Esta fase é gerenciada pelo `QuizSimulator.py`.

O simulador também utiliza o padrão *Visitor* para percorrer a árvore sintática e extrair os dados do quiz (título, tempo, seções e questões). Em seguida, ele inicia uma sessão interativa no terminal, onde:

1.  O quiz é apresentado ao usuário.
2.  As perguntas são exibidas em ordem.
3.  O usuário pode inserir suas respostas.
4.  O simulador avalia as respostas (para questões de múltipla escolha e numéricas) e fornece feedback imediato.
5.  Ao final, o simulador exibe a pontuação total e o tempo gasto.

## 7. Conclusão

O compilador para QuizLang implementado cumpre com sucesso os requisitos de análise léxica, sintática, semântica e execução para a linguagem proposta. A utilização do ANTLR acelerou o desenvolvimento das fases iniciais, e a implementação em Python permitiu a criação de uma análise semântica robusta e de um simulador interativo funcional.

O projeto demonstra a aplicação prática dos conceitos de teoria da compilação, desde a análise de texto até a execução de uma lógica baseada na estrutura da linguagem.
