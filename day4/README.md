# Python 100 Days Code: Day 4

Este projeto contém exemplos práticos para aprender a trabalhar com geração de números aleatórios, listas e tratamento de erros em Python. Também inclui dois projetos para aplicar os conceitos aprendidos: **Bank Roulette** (projeto intermediário) e **Rock Paper Scissors** (projeto final).

### 1. Random Module
- **Pseudorandom Number Generators**:
    - Computadores não são realmente aleatórios; eles usam algoritmos para gerar números “pseudoaleatórios”.
    - O algoritmo mais famoso usado em linguagens de programação modernas é o Mersenne Twister.

- **Usando o Módulo Random**:
    - Para usar é necessário importar:
    ```
    import random
    ```
- **Números inteiros aleatórios**:
    - `randint(a, b)` → retorna um número inteiro aleatório entre a e b, incluindo ambos. 
    ```
    random_integer = random.randint(1, 10)
    print(random_integer)
    ```

- **Números decimais aleatórios**:
    - `random()` → gera um número entre 0.0 (inclusive) e 1.0 (exclusivo).
    - Pode-se ajustar o intervalo multiplicando o resultado.

    ```
    random_number_0_to_1 = random.random() * 10
    print(random_number_0_to_1)
    ```

    - `uniform(a, b)` → gera um número float aleatório entre a e b (pode incluir o limite superior dependendo do arredondamento).
    ```
    random_float = random.uniform(1, 10)
    print(random_float)
    ```

- **Cara ou coroa com randint**:
    ```
    random_heads_or_tails = random.randint(0, 1)
    if random_heads_or_tails == 0:
        print("Heads")
    else:
        print("Tails")
    ```

### 2. Listas em Python
**Criando listas**

```
fruits = ["Cherry", "Apple", "Pear"]
```
```
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", ..., "Hawaii"]
```

**Acessando itens**
- Indexação começa em 0.
```
states_of_america[0]   # "Delaware"
```
- Índices negativos acessam itens de trás para frente:
```
fruits[-1]   # "Pear"
```

**Modificando listas**
- Alterar itens existentes:
```
states_of_america[1] = "Pencilvania"
```

- Adicionar itens ao final:
```
states_of_america.append("Angelaland")
```

- Adicionar vários itens de uma vez:
```
states_of_america.extend(["Angelaland", "Jack Bauer Land"])
```

### 3. IndexError e Listas Aninhadas
**Obtendo o tamanho de listas ou strings**

```
len(states_of_america)  # Retorna o número de itens na lista
len("Hello")            # Retorna 5
```

**IndexError**
- Ocorre quando tentamos acessar um índice que não existe na lista.
```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3])  # IndexError
```

**Listas aninhadas (2D Lists)**
- Uma lista pode conter outras listas:
```
fruits = ["Strawberries", "Nectarines", "Apples"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
```

## Projeto Intermediário: Bank Roulette

### O que o projeto faz?
- Cria uma lista de amigos.
- Seleciona uma pessoa aleatoriamente para pagar a conta usando `random.randint()` ou `random.choice()`.

### O que foi aprendido?
- Como escolher um elemento aleatório de uma lista.
- Duas formas diferentes:
    - Usando índice aleatório com `randint()`.
    - Usando `random.choice()`, que seleciona diretamente um item da lista.
- Reforço do uso de `len()` para evitar IndexError.

## Projeto Final: Rock Paper Scissors
### O que o projeto faz?
- Implementa o clássico jogo Pedra, Papel e Tesoura.
- O jogador escolhe sua opção via `input()`.
- O computador escolhe aleatoriamente uma jogada usando `randint()`.
- O programa compara as jogadas e exibe o resultado (vitória, derrota ou empate).
- O jogo também exibe ícones ASCII das jogadas.

### O que foi aprendido?
- Uso combinado de listas, índices e entrada do usuário.
- Como associar listas de opções (rock, paper, scissors) a listas de ícones (ASCII art) usando índices correspondentes.
- Estruturas condicionais para verificar quem ganhou.
- Manipulação de strings com `.lower()` para padronizar entrada do usuário.
- Uso de `random.randint()` para gerar jogadas do computador.

### Referência:
- Demo: https://appbrewery.github.io/python-day4-demo/