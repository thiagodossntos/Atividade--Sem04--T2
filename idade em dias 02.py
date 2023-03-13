anos = int(input('quantos anos você tem? '))
meses = int(input('agora os meses: '))
dias = int(input('pode colocar os dias? '))

a = anos * 365
m = meses * 30
d = a + m + dias
print(f'essa é a sua idade somente em dias {d}')
