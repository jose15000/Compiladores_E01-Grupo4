#!/bin/bash

# Saia do script se ocorrer qualquer erro
set -e

# Verifica se há mudanças no diretório de trabalho
if [ -z "$(git status --porcelain)" ]; then
  echo "Nenhuma mudança detectada."
  exit 0
fi

# Solicita ao usuário escolher entre um comentário geral ou individual
read -p "Deseja usar um comentário geral para todas as mudanças? (Y/N) [Padrão: Y]: " option

# Define a opção padrão como "Y" se o usuário pressionar Enter
option=${option:-Y}

# Converte a entrada para maiúsculas para simplificar a validação
option=${option^^}

# Verifica se a entrada do usuário é válida
if [[ "$option" != "Y" && "$option" != "N" ]]; then
  echo "Opção inválida. Por favor, escolha Y ou N."
  exit 1
fi

# Caso Y: Comentário geral para todos os commits
if [[ "$option" == "Y" ]]; then
  read -p "Digite a mensagem de commit para todas as mudanças (ou pressione Enter para 'Comentário geral para todos os commits'): " commit_message
  
  # Define mensagem padrão se o usuário pressionar Enter
  commit_message=${commit_message:-"Comentário geral para todos os commits"}

  # Adiciona e faz commit de cada arquivo individualmente
  for file in $(git status --porcelain | awk '{print $2}'); do
    echo "Processando arquivo: $file"
    
    # Adiciona o arquivo ao índice
    git add "$file"
    
    # Faz o commit com a mensagem única
    git commit -m "$commit_message"
    
  done

# Caso N: Comentário individual para cada arquivo
elif [[ "$option" == "N" ]]; then
  # Adiciona e faz commit de cada arquivo individualmente
  for file in $(git status --porcelain | awk '{print $2}'); do
    echo "Processando arquivo: $file"
    
    # Adiciona o arquivo ao índice
    git add "$file"
    
    # Solicita ao usuário uma mensagem de commit para cada arquivo
    read -p "Digite a mensagem de commit para $file: " commit_message
    
    # Define mensagem padrão se o usuário pressionar Enter
    commit_message=${commit_message:-"Comentário geral para todos os commits"}
    
    # Faz o commit com a mensagem personalizada
    git commit -m "$commit_message"
    
  done
fi

# Empurra as mudanças para o repositório remoto
git push

echo "Todas as mudanças foram commitadas."