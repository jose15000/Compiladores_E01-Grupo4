
# Compilador para QuizLang

## 1. Objetivo

Este projeto apresenta um compilador completo para a **QuizLang**, uma linguagem de domínio específico (DSL) projetada para a criação de quizzes. O compilador foi desenvolvido utilizando ANTLR para a geração dos analisadores léxico e sintático, e Python para a implementação da análise semântica e da simulação interativa do quiz.

A QuizLang permite que usuários definam a estrutura de um quiz, incluindo metadados, seções e diferentes tipos de questões (múltipla escolha, discursiva e numérica), de forma declarativa e legível. O objetivo do compilador é validar a estrutura e a semântica de um arquivo QuizLang e, em caso de sucesso, fornecer uma representação estruturada do quiz.

## 2. Linguagem e Ferramentas Utilizadas
*   **Linguagem Principal:** Python 3
*   **Geração de Parser:** ANTLR 4
*   **Dependências Python:** `antlr4-python3-runtime`

## 3. Instruções de Execução

### Pré-requisitos
- Python 3.x
- Java Development Kit (JDK) (necessário para o ANTLR, caso precise gerar os fontes do parser novamente)

1.  **Ative o ambiente virtual:**
    O projeto já inclui um ambiente virtual chamado `myenv`. Ative-o com o seguinte comando:
    ```bash
    source myenv/bin/activate
    ```

2.  **Instale as dependências:**
    A principal dependência Python é o runtime do ANTLR. Instale-o com:
    ```bash
    pip install antlr4-python3-runtime
    ```

3.  **Execute o compilador:**
    Para analisar e simular um arquivo de quiz (por exemplo, `teste_ok.txt`), execute o `main.py`:
    ```bash
    cd src
    python3 main.py exemplos/teste_ok.txt
    ```
    O programa irá validar o arquivo e, se não houver erros, iniciará a simulação interativa no terminal.

## 4. Responsabilidades dos Integrantes
*   **Anthony:** Definição da gramática da linguagem (`QuizLang.g4`) e configuração do ANTLR para geração do analisador léxico e sintático.
*   **José Henrique:** Implementação da análise semântica, incluindo a criação da Tabela de Símbolos (`SymbolTable`) e as regras de validação no `SemanticAnalyzer.py`.
*   **Alan:** Desenvolvimento do simulador interativo do quiz (`QuizSimulator.py`) e da estrutura principal do programa (`main.py`), integrando todas as fases do compilador.

## 5. Exemplo de Saída

Ao executar o compilador com um arquivo de entrada válido, como `exemplos/teste_ok.txt`, a saída será semelhante a esta:

### Relatório de Análise

Primeiro, o programa exibe a árvore sintática e o relatório da análise semântica.

```
--- Análise Concluída Sem Erros ---

--- Árvore de Análise Sintática ---
quiz
  TOKEN: 'quiz'
  TOKEN: 'OkQuiz'
  TOKEN: '{'
... (árvore sintática omitida para brevidade) ...
-------------------------------------

--- Relatório Semântico ---

Variáveis, tipos e escopos:
Escopo 'OkQuiz':
  - titulo: string
  - tempo: number
  - Seção 1: secao
  - Seção 2: secao
... (relatório semântico omitido para brevidade) ...
```

### Simulação Interativa do Quiz

Em seguida, a simulação do quiz é iniciada no terminal.

```
--- Iniciando Simulação do Quiz ---
==================================================
Bem-vindo ao Quiz: Quiz sem erros
Você tem 15 minutos para concluir.
==================================================
Pressione Enter para começar...

--- Iniciando Seção: Seção 1 ---

Q1: Qual a cor do céu?
  1. Azul
  2. Verde
  3. Vermelho
Sua resposta (digite o texto da opção): Azul
Correto!

... (simulação continua) ...
```
