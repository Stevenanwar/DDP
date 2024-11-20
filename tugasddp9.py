# nomer 1
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5)+32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

# Nomer 2
def is_genap(bilangan):
    return bilangan % 2==0

print(is_genap(4))
print(is_genap(7))


# nomer 3
def nilai(skor):
    if skor >= 75:
        print("lulus")
    else:
        print("gagal")
nilai(80)
nilai(60)

# nomor 4
def bilangan(a):   
    hasil= []

    for i in range(1, a):
        if i % 2 != 0:
            hasil.append(i)
            
    print(hasil)

bilangan(20)