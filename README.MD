# Documentação: Linguagem quizlang

## 1. Introdução à QuizLang

O compilador da QuizLang valida a estrutura e a lógica do seu quiz, garantindo que ele esteja bem formado e livre de erros comuns, como respostas incorretas ou questões duplicadas.

## 2. Como Escrever um Quiz: Um Exemplo Prático

Um arquivo QuizLang é fácil de ler e escrever. A seguir, um exemplo de um quiz completo:

```
quiz MeuPrimeiroQuiz {
    titulo "Um Quiz Simples"
    tempo 10 // Tempo em minutos

    secao "Conhecimentos Gerais" {
        mcq Q1:
            pergunta "Qual a capital da França?"
            opcoes ["Londres", "Berlim", "Paris", "Madri"]
            resposta "Paris"

        discursiva Q2:
            pergunta "Descreva o que é a fotossíntese."
            palavras 50 // Limite de palavras para a resposta

        numerica Q3:
            pergunta "Em que ano o homem pisou na Lua?"
            intervalo 1969-1969
    }
}
```

## 3. Estrutura da Linguagem

Todo arquivo QuizLang segue uma hierarquia simples:

*   **`quiz`**: O bloco principal que define o quiz. Ele deve ter um **ID** (um nome sem espaços, como `MeuPrimeiroQuiz`).
*   **`metadados`**: Dentro do quiz, você deve especificar:
    *   `titulo`: O título do quiz, entre aspas.
    *   `tempo`: Um número que representa o tempo limite em minutos.
*   **`secao`**: Um quiz é dividido em uma ou mais seções. Cada seção tem um nome (entre aspas) e contém um conjunto de questões.
*   **`item`**: Cada questão é um item dentro de uma seção.

## 4. Tipos de Questões

A QuizLang suporta três tipos de questões:

### 4.1. Múltipla Escolha (`mcq`)

Usada para questões onde o usuário deve escolher uma entre várias opções.

*   **Sintaxe:**
    *   `mcq ID_DA_QUESTAO:`
    *   `pergunta "..."`
    *   `opcoes ["Opção 1", "Opção 2", ...]`
    *   `resposta "Opção Correta"`
*   **Regras Semânticas:**
    *   A `resposta` deve ser uma das `opcoes`.
    *   Deve haver no mínimo duas opções.
    *   As opções não podem ser repetidas.

### 4.2. Discursiva (`discursiva`)

Usada para questões de resposta aberta.

*   **Sintaxe:**
    *   `discursiva ID_DA_QUESTAO:`
    *   `pergunta "..."`
    *   `palavras NUMERO_DE_PALAVRAS`
*   **Regras Semânticas:**
    *   O limite de `palavras` deve ser um número maior que zero.

### 4.3. Numérica (`numerica`)

Usada para questões cuja resposta é um número ou está dentro de um intervalo numérico.

*   **Sintaxe:**
    *   `numerica ID_DA_QUESTAO:`
    *   `pergunta "..."`
    *   `intervalo NUMERO_INICIAL-NUMERO_FINAL`
*   **Regras Semânticas:**
    *   O número inicial do intervalo não pode ser maior que o número final.

## 5. Como Usar o Compilador

O compilador da QuizLang é uma ferramenta de linha de comando que analisa um arquivo `.txt` contendo seu quiz.

### 5.1. Execução

Para analisar um arquivo, utilize o seguinte comando no seu terminal:

```bash
python3 main.py <caminho_para_o_seu_arquivo.txt>
```

Por exemplo:

```bash
python3 main.py meu_quiz.txt
```

### 5.2. Saída do Compilador

O compilador fornecerá uma das seguintes saídas:

*   **Sucesso:** Se o seu arquivo for sintática e semanticamente correto, ele exibirá uma análise da estrutura do quiz e uma mensagem de sucesso.
*   **Erro Sintático:** Se houver um erro na estrutura do seu código (e.g., falta de uma chave `}`), ele indicará a linha e a coluna do erro.
*   **Erro Semântico:** Se a estrutura estiver correta, mas a lógica não (e.g., uma resposta de `mcq` que não corresponde a nenhuma opção), ele listará todos os erros semânticos encontrados.

O compilador também gera um relatório detalhado da análise semântica, incluindo todos os símbolos, escopos e variáveis identificados, o que pode ser útil para depuração.

