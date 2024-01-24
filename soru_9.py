#Soru 9 : Kullanıcıdan bir kelime girişi alan ve bu kelimenin palindrom (tersten okunduğunda aynı olan) olup olmadığını kontrol eden bir döngü ve koşullu ifade kombinasyonu nasıl oluşturulur?

while True:
    kelime = input("Bir kelime giriniz:")
    ters_kelime = kelime[: : -1]

    if kelime == ters_kelime:
        print("Kelime palindromdur.")
    else:
        print("Kelime palindrom degildir.")