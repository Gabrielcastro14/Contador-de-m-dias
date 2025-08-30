import pandas as pd 


def calculo_media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def ler_nota (mensagem):
    while True:
        try: 
            nota = float(input( mensagem))
            if 0 <= nota <= 10: 
                return nota 
            else: 
                print ("nota invalida digite entre 0 e 10.")
        except ValueError:
            print ("valor invalido, digite um numero. ")


def situacao_aluno (media):
    if media >= 7:
         return f"aprovado com media {media:.2f}"
    elif media >= 5: 
      return f"recuperaçao com media {media:.2}"
    else:
        return f"reprovado com media {media:.2f}"
    

def processar_aluno () :
    nome = input("digite o nome do aluno: ").strip (). title ()
    nota1 = ler_nota ("digite a primeira nota ")
    nota2 = ler_nota ("digite a segunda nota ") 
    nota3 = ler_nota ("digite a terceira nota" )

    media = calculo_media (nota1, nota2, nota3)
    situacao = situacao_aluno (media) 
    
    return {
    "nome": nome,
    "notas": [nota1, nota2, nota3],
    "media": media,
    "situacao": situacao
    }
    
boletim = []

quantidade = int(input("quantos alunos deseja cadastrar?"))
for i in range (quantidade):
    print ( f"\naluno {i + 1}")
    aluno = processar_aluno ()
    boletim.append (aluno)


print ("\n boletim final")
print ("-" * 40 ) 
    
aprovados   = 0 
recuperacao = 0
reprovados  = 0


for aluno in boletim : 
    nome  = aluno ['nome']
    notas = ",".join(f"{n:.1f}" for n in aluno ['notas'])
    media = aluno ['media']
    situacao = aluno ['situacao']
    
    print (f"nome: {aluno['nome']}         ")
    print (f"notas: {aluno['notas']}       ")
    print (f"media: {aluno['media']:.2f}   ")
    print (f"situacao: {aluno['situacao']} ")
    print ("-" * 40) 
  
    if "aprovado" in situacao.lower ():
      aprovados += 1 
    elif "recuperacao" in situacao.lower ():
      recuperacao += 1
    elif "reprovado" in situacao.lower ():
      reprovados += 1

print("\nResumo Final:")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")     
 
df = pd.DataFrame (boletim)

df[['nota 1', 'nota2', 'nota3']] = pd.DataFrame(df['notas']. to_list() )

df.drop(columns='notas',inplace= True )

df.to_csv ("boletim_final.csv", index = False)

print ("\nArquivo 'boletim_final.csv' salvo com sucesso na pasta do projeto!")