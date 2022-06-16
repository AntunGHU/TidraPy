# 10'58''
# Ovdje govori o drugoj vrsti gresaka: Exceptions-ima
a = 1
b = '2'
c = 2
print(int(2.5))
print(a+float(b))  #   File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/132_RuntimeErrors.py", line 6, in <module>
            #       print(a+b)
            # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Sad nam se greske razlikuju: Kod Arda je SyntaxError! i ima ^ a kod mene ne! Ali, fuck! Kod njega nema zadnje ) pa zato. Dosadni Ardo! Mogao je vec preskociti syntax error! Ipak jedno uopcavanje: 
#! UVJEK kad imamo ^ u ErrorRep-u prvo pogledajmo nakon samog mjesta gdje je ^ liniju ispred!
# Nakon fiksiranja problema s ) dobija istu gresku kao i ja! Ispravio sa dodavanjem float(b) a zatim pokazao i mogucnost rjesavanja pretvaranjem a u str i u svega u konkatination!
print(str(a)+b)
# u nastavku da ima i drugih gresaka osim Type error-a, npr: NameError
print(c)    # File "/home/antun/Documents/aCod/TidraPy/16_FixingProgrammingErrors/132_RuntimeErrors.py", line 14, in <module>
            # print(c)
        # NameError: name 'c' is not defined
# ispravlja promocijom c pa nastavlja sa "Zero division Error". Polako postaje nabacivanje! Nije nastavnik!