# Reconhecimento do Curso e Semestres

input("Pressione Enter para iniciar...")

print("Bem vindo ao sistema de notas e faltas da UNIP")

while True:
    curso = input("Qual o seu curso? [Digite o nome por extenso]: ")
    if any(char.isalpha() for char in curso):
        curso = curso.upper()
        break
    else:
        print("Por favor, insira um nome válido contendo letras.")

semestres = input("Seu curso é Bacharel, Licenciatura ou Tecnólogo? [B/L/T]: ").upper()
if semestres == "B":
    semestres = [8, 9, 10]
elif semestres == "L":
    semestres = [8, 9, 10]
elif semestres == "T":
    semestres = [4, 5]
else:
    print("Opção Inválida.")
    exit()

# Notas e Faltas

while True:
    try:
        NP1 = float(input("Digite a nota da NP1 [Exemplo: 7.6]: "))
        NP2 = float(input("Digite a nota da NP2: "))
        PIM = float(input("Digite a nota do PIM: "))
        num_faltas = int(input("Quantos dias você faltou no total dessa disciplina?: "))
        break
    except ValueError:
        print("Por favor, insira apenas números.")
frequencia_calculo1 = (int(num_faltas*3)/60)*100
frequencia_calculo2 = (int(100 - frequencia_calculo1))

# Funcionamento

MS = (float(4*NP1 + 4*NP2 + 2*PIM)/10)
print(f"Sua média semestral é: {MS:.2f} e Sua frequência é: {frequencia_calculo2}%")
if frequencia_calculo2 < 75:
    print("Reprovado por falta, você não atingiu a frequência minima exigida!")
    exit()
if MS >= 7:
    print("Aprovado na Discplina, Parabéns!")
elif MS < 7:
    print("Você não atingiu a média mínima exigida para aprovação na Disciplina, você está de Exame e parecisa tirar 5 ou mais.")
    input("Pressione Enter se já realizou o exame...")
    EX = (float(input("Digite a nota do Exame [Exemplo: 9.5]: ")))
    MF = (MS + EX)/2
    if MF >= 5:
        print(f"Sua Média Final é {MF:.2f} e você está Aprovado na Disciplina, Parabéns!")
    else:
        print(f" Sua Média Final é {MF:.2f} e você está Reprovado na Disciplina, você não atingiu a média mínima e ficará de dependência...")

print("Fim do programa. Obrigado por utilizar!")

input("Pressione Enter para sair...")