nome=input("Me diga o seu nome")
idade=int(input("Me diga sua idade"))
if idade>=16:
     print(f'{nome}, você tem {idade} anos e por isso  você pode emitir seu título de eleitor')
else:
    print(f'{nome}, você tem {idade} anos e por isso  você não pode emitir seu título de eleitor')
