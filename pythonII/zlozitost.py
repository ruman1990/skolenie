# ukazka zlozitosti algoritmu
katalog_produkt ={"2554801" : { "nazov" : "Voda" , "pocet": 5 , "cena" : 2.50 } , 
                    "156126" : { "nazov" : "chlieb" , "pocet": 5 , "cena" : 2.50 }}

katalog_produkt2 =[{ "nazov" : "Voda" , "pocet": 5 , "cena" : 2.50 } , 
          { "nazov" : "chlieb" , "pocet": 5 , "cena" : 2.50 }]

print(katalog_produkt["2554801"])
for x in katalog_produkt2:
    if x['nazov']=='Voda':
        print(x)
