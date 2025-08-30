def media_idade (lista):
    return sum (lista) / len (lista)

def maior_idade(lista):
    if not lista:
        return None
    maior = lista[0]
    for idade in lista:
        if idade > maior:
            maior = idade
    return maior

def ler_idade (mensagem):
    while True :
        try :
            idade = float(input (mensagem))
            if 0 <= idade <= 100:
                return idade
            else:
                print ("idade inválida, digite entre 0 a 100.")
        except ValueError:
            print ("valor invalido digite um numero.")

idades = []
quantidade = int(input("quantas idades deseja cadastrar?"))
              
for i in range(quantidade):
    print(f"\nIdade {i + 1}")
    idade = ler_idade("Digite a idade: ")
    idades.append(idade)
    
print("\n--- RESULTADOS ---")
print(f"Todas as idades cadastradas: {idades}")
print(f"Maior idade: {maior_idade(idades)}")
print(f"Média das idades: {media_idade(idades):.2f}")     

        

 