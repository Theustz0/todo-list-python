# 📝 Lista de Tarefas (To-Do List) em Python

Gerenciador de tarefas em linha de comando (CLI) desenvolvido em Python. Permite adicionar, visualizar, concluir e remover tarefas de forma simples e interativa, com validação das entradas do usuário.

Projeto feito como exercício de lógica de programação, utilizando **laços de repetição** (`while`, `for`), **estruturas condicionais** (`if`/`elif`/`else`), **listas** e **manipulação de strings**.

## ✨ Funcionalidades

O programa exibe um menu com as seguintes opções:

| Opção | Ação |
|-------|------|
| 🟢 `A` | Adicionar uma nova tarefa |
| ⚪ `R` | Remover tarefa / marcar como concluída |
| 🔵 `M` | Mostrar todas as tarefas |
| 🟣 `T` | Remover todas as tarefas |
| 🔴 `S` | Sair do programa |

Todas as opções passam por **validação de entrada**: se o usuário digitar algo inválido, o programa pede que ele digite novamente até uma opção válida ser informada.

## 🚀 Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/downloads/) instalado na máquina.

```bash
# Clone o repositório
git clone https://github.com/Theustz0/lista-de-tarefas-python.git

# Entre na pasta do projeto
cd lista-de-tarefas-python

# Execute o programa
python "Lista de Tarefas.py"
```

## 🖥️ Exemplo de uso

```
====================================================================================================
                    - BEM - VINDO A SUA LISTA DE TAREFAS AUTOMÁTICA 1.0 -
====================================================================================================
🟢 A = ADICIONAR UMA NOVA TAREFA
⚪ R = REMOVER TAREFAS/CONCLUIR
🔵 M = MOSTRAR TODAS AS TAREFAS
🟣 T = REMOVER TODAS AS TAREFAS
🔴 S = SAIR
====================================================================================================
➡️  digite qual opção você deseja:
```

## 🛠️ Tecnologias e conceitos utilizados

- Python 3
- Laços `while` e `for`
- Estruturas condicionais `if` / `elif` / `else`
- Listas e manipulação de strings (`f-strings`, `.upper()`, `.title()`, `.center()`)
- Validação de entradas do usuário

## 📌 Próximas melhorias (ideias)

- [ ] Salvar as tarefas em um arquivo, para não perdê-las ao fechar o programa
- [ ] Adicionar data/hora de criação de cada tarefa
- [ ] Permitir editar uma tarefa já existente

## 📄 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

Desenvolvido por [Theustz0](https://github.com/Theustz0)
