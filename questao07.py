nome=input("Me diga o seu nome")
matéria=input("Me diga uma matéria")
nota1=int(input("Qual foi a sua nota:"))
nota2=int(input("Qual foi a sua outra nota:"))
media=(nota1+nota2)/2
if media>=6:
    situação="Aprovado(a)"
else:
    situação="Reprovado(a)"
print(f'{nome}, você está {situação} na disciplina de {matéria}')
