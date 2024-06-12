hora= int(input("Me diga um horário"))
if 0<= hora<12:
     print(f'Manhã')
elif 12<= hora<18:
     print(f'Tarde')
else:
    print(f'Noite')
