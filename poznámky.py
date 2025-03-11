#načtení od uživatele je například takto.   Zadáme název proměnné za to dáme rovná pak dáme datový typ a do závorek napíšeme na jakou větu má uživatel odpovědět a ta se dává do úvozovek. 
# Příklad: 
oblíbenéZvire= str(input("Co je tvoje oblíbené zvíře?")) 
#Přetypován se využívá na to, když chceme změnit datový typ na jiný. 
#Příklad : 
cislo = int(input())
#If se používá, když chceme aby program poznal co tam je a když by se tam nacházerlo to co je v if či elif tak aby podle toho mohl udělat ty pokyny co tam má (if a elif znamená to stejný jenom elif se používá na to, aby se pořád if neopakovalo).
#A pomocí else můžeme zadat co například s odpovědí má program dělat, pokavaď ta odpověď nesplňuje to co je napsáno v if nebo elif.
Příklady:
cislo= int(input("Napiš sem číslo."))
if (cislo == 1:):
    print ("Číslo je jedna.")
elif (cislo == 1):
    print("Číslo je jedna.")
else: 
    print("Číslo není jedna.")
#Logické operátory and, or či not slouží k tomu, aby se mohl program rozhodnout jestli je to pravda či ne and je k tomu, and slouží k tomu, že když jsou oba příákazy správně tak to bude vědět, že to je pravda, or když je jeden pravda tak to bude vědět, že to je pravda. A not k tomu, aby určil jestli je to pravda a vytvořil negaci u booleanu.
Příklad:
    cislo == 11 or 