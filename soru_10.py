''' Soru 10 : Kişinin kilo indeksini hesaplayıp indeks değerine göre zayıf, kilolu veya fazla kilolu olarak sonuç döndüren kodu yazınız.(kilo indeks hesabı için internete bakabilirsiniz) 
Bunun için kullanıcıdan kilo ve boy ölçülerini isteyiniz. Kilo indeksi 
25’in altında ise zayıf, 
25-30 arasında ise normal, 
30-40dan büyük ise kilolu, 
40tan büyük ise aşırı kilolu sonuçlarına varsın.'''


print("Vucut Kitle Indeks Hesaplama ")
boy = float(input("Boy(m): "))
kilo = int(input("Kilo(kg): "))

endeks = kilo/(boy*boy)

if endeks < 25:
    print("Zayif")
elif endeks >25 and endeks < 30:
    print("Normal")
elif endeks >30 and endeks < 40:
    print("Kilolu")
elif endeks >40:
    print("Dikkat!OBEZSINIZ.")