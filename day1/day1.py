# 1. Imprima "Hello world!"
print("Hello World!")

# 2. Use \n para repetir a frase em múltiplas linhas (3 vezes)
print("Hello World!\n" * 3)

# 3. Concatene strings com espaço no meio
print("Hello " + "Lucca")

# 4. Peça o nome do usuário e exiba com exclamação
name = input("Type your name: ")
print("Hello " + name + "!")
print(f"Hello {name}!")

# 5.1. Mostre o número de caracteres digitados em uma única linha
print(len(input("Type your name: ")))

# 5.2. Use variáveis separadas para armazenar o nome e seu tamanho
username = input("Type your name: ")
length = len(username)
print(length)
