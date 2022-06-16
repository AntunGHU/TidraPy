# 8'22''
# Citava cjelina jos uvjek se pise u Atom-u! Videa snima s Camtasia
# Najvaznija lekcija do sada! Pocetak energican! Novi video sad iskusnog Arda! Bavio se temom pomalo ali je stalno osjecao da nije dovoljno pa je odlucio posvetiti posebnu lekciju greskama u Py.
# Ako ne znamo citati greske, razumjeti ih, imat cemo problema sa svakom temom jer greske rade i najiskusniji programeri!
# Zato, kad se greska pojavi, don't panick, just folow instructions!

print(1)
int(9)
# int 9   # int 9
        #     ^
# SyntaxError: invalid syntax
# Iznad dodje prva linija error-reporta (koju nisam napisao jer je predugacka: Evo je:
# File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/131_SyntaxErrors.py", line 8) Neke su greske detaljnije, kod nekih sami moramo skuziti sto je greska, kao ovdje. Nakon sto smo skuzili da built-in fun "int" trazi () i stavili ih program ide dalje!
print(2)
print (3)     # File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/131_SyntaxErrors.py", line 14
              # print 3
                    # ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(3)?
# Evo primjera sadrzajnijeg opisa greske!!!
a=[1,2,3]       # File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/131_SyntaxErrors.py", line 19
                # a=[1,2,3)
                        # ^
# SyntaxError: closing parenthesis ')' does not match opening parenthesis '['