# Python 100 Days Code: Day 2

Este projeto contém exemplos práticos para aprender conceitos fundamentais de Python. Durante a execução do código, foram abordados os seguintes tópicos:

### 1. Tipos de Dados (Data Types)
- Integers (números inteiros): números sem casas decimais.
- Floats (números decimais): números com casas decimais.
- Booleans (True / False): valores lógicos usados em condições.
- Exemplo:

```
print(123 + 345)          # Soma de inteiros
print(123_456_789)        # Uso de _ para facilitar leitura
print(3.14159)            # Número decimal
print(True)               # Boolean True
print(False)              # Boolean False
```

### 2. TypeError, Type Checking e Conversão de Tipos
- **TypeError**: erro ao usar um tipo de dado incorreto (ex: `len(123)`).
- **Type Checking**: uso de `type()` para verificar tipos de dados.
- **Type Conversion**: conversão manual entre tipos (`str()`, `int()`, `float()`, `bool()`).
- **Concatenação de string com int**: corrigida usando conversão explícita para string.
- Exemplo:

```
print(len("Hello"))                # Corrigido
print(type("abc"))                 # <class 'str'>
print(type(123))                   # <class 'int'>
print(type(3.14))                  # <class 'float'>
print(type(True))                  # <class 'bool'>
print(str(123))                    # int -> str
print(int("456"))                  # str -> int
print(float("3.14"))               # str -> float
print(bool(1))                     # int -> bool

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_name))
```

### 3. Operadores Matemáticos e Ordem de Precedência
- Operadores básicos: `+`, `-`, `*`, `/`, `//`, `**`
- PEMDAS: ordem correta das operações matemáticas (Parênteses, Expoentes, Multiplicação/Divisão, Adição/Subtração).
- Exemplo:

```
print(3 * 3 + 3 / 3 - 3)         # Resultado de acordo com a ordem de precedência
print(3 * (3 + 3) / 3 - 3)       # Alterado para resultar em 3
```

### 4. Manipulação de Números, Arredondamento e f-Strings
- **Flooring**: int() converte para inteiro removendo casas decimais.
- **Arredondamento**: round() arredonda corretamente (padrão matemático).
- **Arredondamento com casas decimais**: round(valor, casas_decimais)
- **f-Strings**: inserir variáveis diretamente dentro de strings com f"".
- Exemplo:

```
bmi = 84 / 1.65 ** 2
print(bmi)                  # Float original
print(int(bmi))             # Flooring
print(round(bmi))           # Arredondamento inteiro
print(round(bmi, 2))        # Arredondamento com 2 casas
age = 25
print(f"I am {age} years old")   # Uso de f-strings
```

## Projeto Final: Calculadora de Gorjetas
Este projeto aplica todos os conceitos aprendidos em um pequeno programa interativo para calcular quanto cada pessoa deve pagar ao dividir uma conta com gorjeta.

### O que o programa faz:
- Mostra uma mensagem de boas-vindas.
- Pede o valor total da conta.
- Pede a porcentagem da gorjeta a ser dada.
- Pede o número de pessoas que vão dividir a conta.
- Calcula automaticamente o valor que cada pessoa deve pagar e exibe o resultado formatado.

### Exemplo de execução:
```
Welcome to the tip calculator!
What was the total bill? $100
What percentage tip would you like to give? 10 12 15 12
How many people to split the bill? 4
Each person should pay: 28.0
```

### Conceitos aplicados:
- Conversão de entrada do usuário (`input()` → `float()` e `int()`).
- Operações matemáticas combinadas com porcentagem.
- Arredondamento do resultado com `round(valor, 2)`.
- f-Strings para formatar a saída final.

### Referências:
- Demo: https://appbrewery.github.io/python-day2-demo/
- Very Optional Reading: 
    Floating Point Arithmetic https://docs.python.org/3/tutorial/floatingpoint.html