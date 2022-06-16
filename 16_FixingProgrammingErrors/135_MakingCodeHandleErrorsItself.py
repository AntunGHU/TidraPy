# 7'59''
# Daje neki tipican primjer, pocinje sa Zero division
#? def division(a,b):
#?     return a/b
#? division(1,0)
#  Traceback (most recent call last):
#    File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/135_MakingCodeHandleErrorsItself.py", line 5, in <module>
#      division(1,0)
#    File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/135_MakingCodeHandleErrorsItself.py", line 4, in division
#      return a/b
#  ZeroDivisionError: division by zero

# Imamo 2 greske, jedna okidac i jedna u definiciji koja treba biti nas fokus!! Razlog zasto je rekao da treba kompletnu gresku ukljuciti u pitanje!
# Nastavlja sa znacajem try except u omogucavanju da se ostatak koda izvodi!
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        # print("Besmisleno je djeliti s nulom!")
        return "Besmisleno je djeliti s nulom!"
print(division(1,0))
# korigira print u return jer bez returna uvjek dobijamo None na izlazu! 
# Takodjer naglasava imati u liniji sa except i tocno ime greske koju ocekujemo npr ovdje "ZeroDivisionError" koju Py poznaje i zaplavi! jer mu je to key-word!