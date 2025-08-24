# Python 100 Days Code: Day 1

Este projeto contém exemplos práticos para aprender conceitos básicos de Python, adquiridos durante o curso do **AppBrewery**. Durante a execução do código, foram abordados os seguintes tópicos:

### 1. Imprimir mensagens na tela
- Uso do comando `print()` para exibir textos.
- Exemplo:
```
print("Hello World!")
```

### 2. Quebra de linha e repetição de strings
- Uso da sequência de escape `\n` para quebrar linhas.
- Multiplicação de strings para repeti-las.
- Exemplo:
```
print("Hello World!\n" * 3)
```

### 3. Concatenação de strings
- Combinação de textos com o operador `+`.
- Exemplo:
```
print("Hello " + "Lucca")
```

### 4. Entrada de dados do usuário
- Uso da função `input()` para capturar valores digitados.
- Integração da entrada em uma string com concatenação e f-strings.
- Exemplo:

```
name = input("Type your name: ")
print("Hello " + name + "!")
print(f"Hello {name}!")
```

### 5. Uso de variáveis e funções básicas
- Armazenar valores em variáveis para reutilização.
- Uso da função len() para calcular o tamanho de uma string.
- Exemplo em uma linha:

```
print(len(input("Type your name: ")))
```

- Exemplo separando em variáveis:

```
username = input("Type your name: ")
length = len(username)
print(length)
```

### 6. Boas práticas na nomeação de variáveis
- Use nomes descritivos.
- Não utilize espaços entre palavras.
- Não comece com números.
- Não utilize palavras reservadas como `print` ou `input`.
- Prefira nomes simples para evitar erros de digitação.
- Verifique sempre se a empresa possui diretrizes internas de estilo.

## Projeto Final: Gerador de Nome de Banda

Este projeto aplica todos os conceitos aprendidos anteriormente em um pequeno programa interativo. O usuário fornece algumas informações e o programa gera automaticamente um nome de banda divertido.

### O que o programa faz:
- Exibe uma mensagem de boas-vindas ao usuário.
- Pede para o usuário informar o nome da cidade onde nasceu.
- Pede para o usuário informar o nome do seu primeiro animal de estimação.
- Combina essas informações para criar e exibir um nome de banda personalizado.

### Exemplo de execução:
```
Hello, player! Welcome to the band generator program!
What's the name of the city you were born? London
What's the name of your first pet? Bella
Your band name is: London Bella
```

### Conceitos aplicados:
- Uso do comando `print()` para criar mensagens de interação.
- Entrada de dados com `input()`.
- Armazenamento de valores em variáveis.
- Uso de f-strings para formatar a saída final.