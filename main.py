import time
while True:
    word = input("Anlamadığınız bir kelime yazın")
    meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "CRİNGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "ROFL": "bir şakaya karşılık cevap",
                "SHEESH": "onaylamamak",
                "CREEPY" : "korkunç",
                "AGGRO" : "agresifleşmek/sinirlenmek",
                "cringe": "Garip ya da utandırıcı bir şey",
                "lol": "Komik bir şeye verilen cevap",
                "Cringe": "Garip ya da utandırıcı bir şey",
                "Lol": "Komik bir şeye verilen cevap",
                "rofl": "bir şakaya karşılık cevap",
                "sheesh": "onaylamamak",
                "creepy" : "korkunç",
                "aggro" : "agresifleşmek/sinirlenmek",
                "Rofl": "bir şakaya karşılık cevap",
                "Sheesh": "onaylamamak",
                "Creppy" : "korkunç",
                "Aggro" : "agresifleşmek/sinirlenmek",
                "Bug" : "Hata",
                "bug" : "Hata",
                "BUG" : "Hata",
                }
    if word in meme_dict.keys():
        print("Anlamı : ",meme_dict[word])
        time.sleep(0.7)
    else:
        print("Sözlükte böyle bir kelime bulunmuyor:Lütfen başka bir kelime deneyiniz")
        time.sleep(0.7)
