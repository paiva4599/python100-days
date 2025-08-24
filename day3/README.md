# Python 100 Days Code: Day 3

Este projeto contém exemplos práticos para aprender estruturas condicionais, operadores lógicos e conceitos fundamentais de controle de fluxo em Python.

### 1. Estruturas Condicionais (If / Else)
- Uso do `if` para executar código quando uma condição é verdadeira.
- Uso do `else` para executar código quando a condição é falsa.
- Importância da indentação no Python (linhas “filhas” dependem de linhas “pais”).
- Operadores de comparação usados para verificar condições:
    - '>' maior que
    - '<' menor que
    - '>=' maior ou igual a
    - '<=' menor ou igual a
    - '==' igual a
    - '!=' diferente de
- Exemplo:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
```

### 2. Operador Módulo (%)
- O módulo retorna o resto da divisão de dois números.
- Útil para verificar números pares ou ímpares.
- Exemplo:

```
number_to_check = int(input("What is the number you want to check? "))

if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 3. Estruturas Aninhadas (Nesting) e Elif
- If dentro de outro if (nesting): usado para verificar múltiplas condições relacionadas.
- elif: usado quando há mais de duas condições possíveis.
- Exemplo:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 12:
        print("The ticket costs $7.")
    elif age > 12 and age < 18:
        print("The ticket costs $10.")
    else:
        print("The ticket costs $14.")
else:
    print("Sorry you have to grow taller before you can ride.")
```

### 4. Múltiplos Ifs Independentes
- If/elif/else: apenas um bloco é executado (mutuamente exclusivos).
- Ifs aninhados: condições dependem umas das outras.
- Vários ifs independentes: todas as condições são avaliadas separadamente.
- Exemplo:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
```

### 5. Operadores Lógicos (and / or / not)
- **and**: ambas as condições precisam ser verdadeiras.
- **or**: apenas uma condição precisa ser verdadeira.
- **not**: inverte o valor lógico da condição.
- Exemplo:

```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
```

## Conceitos-chave aprendidos
- Controle de fluxo com if, elif e else
- Uso do módulo (%) para verificar números pares/ímpares
- Estruturas aninhadas e múltiplas condições independentes
- Uso de operadores lógicos (and, or, not)
- Uso de variáveis para armazenar resultados intermediários
- Cálculos dinâmicos com entrada do usuário
- Uso de f-strings para exibir valores formatados

## Projeto Intermediário: Python Pizza
Esse projeto tem como objetivo calcular automaticamente o preço final de uma pizza com base nas escolhas do cliente: tamanho, pepperoni e queijo extra.

### Conceitos aplicados:
- Entrada de dados com `input()` para coletar preferências do usuário.
- Estruturas condicionais (`if`, `elif`, `else`) para definir o valor da pizza conforme as opções.
- Operadores de atribuição incremental (`+=`) para somar valores ao total da conta.
- Uso de f-strings para formatar a mensagem final ao cliente.

### Fluxo do Programa:
1. Usuário escolhe tamanho da pizza (`S`, `M`, `L`).
2. Decide se quer pepperoni (`Y` ou `N`).
3. Decide se quer queijo extra (`Y` ou `N`).
4. O programa soma os valores correspondentes:
    - **Tamanho**: S = 15, M = 20, L = 25.
    - **Pepperoni**: +2 para S, +3 para M e L.
    - **Queijo extra**: +1 para qualquer tamanho.
5. Exibe a conta final formatada com f-string.

## Projeto Final: Treasure Island
Este é um jogo de aventura em texto totalmente interativo, onde o jogador precisa fazer escolhas corretas para encontrar o tesouro escondido. O jogo usa estruturas condicionais aninhadas e entrada do usuário para criar uma experiência divertida e envolvente.

### O que o código faz?
1. **Mensagem inicial com arte ASCII** – O jogo começa com uma tela de abertura chamativa.
2. **Primeira escolha: o cruzamento** – O jogador decide ir para a esquerda ou para a direita.
    - Escolher **R (Right)** termina o jogo imediatamente.
3. **Segunda escolha: a sala com portas** – O jogador decide entre as portas **Y (Yellow), R (Red)** ou **G (Green)**.
    - Portas **Yellow** ou **Green** resultam em derrota.
    - Porta **Red** leva o jogador à vitória.
4. **Mensagens finais claras** – O jogo informa se o jogador perdeu ou encontrou o tesouro.

### O que eu aprendi com este projeto?
- Uso de estruturas condicionais complexas (`if` / `elif` / `else`)
- Validação simples de entrada do usuário
- Organização do fluxo lógico de um jogo interativo
- Elementos de design de terminal (ASCII art) para deixar o jogo mais imersivo.

### Referências:
- Demo: https://appbrewery.github.io/python-day3-demo/