

def TakimBelirle(oyuncu_takim):
    #print(oyuncu_takim)
    oyuncu_takim = oyuncu_takim[:-1] # sondaki '\n' karakterini siliyoruz.
    lst_oyuncu_takim = oyuncu_takim.split(", ") # her satiri , ile ayrilmis sekilde list icine aliyoruz.

    isim = lst_oyuncu_takim[0]  # her satir icin isimleri buluyoruz
    takim = lst_oyuncu_takim[1] # her satir icin takimlari buluyoruz

    return takim

#-----------------

with open("futbolcular.txt","r",encoding="utf-8") as futbolcular:

    for i in futbolcular:
        #print(i)
        takim = TakimBelirle(i)
        if (takim == "Fenerbahçe"):
            with open("fb.txt","a",encoding="utf-8") as fb:
                fb.write(i)
        elif (takim == "Beşiktaş"):
            with open("bjk.txt","a",encoding="utf-8") as bjk:
                bjk.write(i)
        elif (takim == "Göztepe"):
            with open("goz.txt","a",encoding="utf-8") as goz:
                goz.write(i)

