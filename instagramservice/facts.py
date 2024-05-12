# prompt - Sporządź proszę listę postów (opisow) dotyczących Maladze w formacie słownika w pythonie. Każdy post ma składać się z 5 podpunktów na różne tematy dotyczące danego miejsca. Każdy podpunkt ma się składać z 3 zdań zakończonych kropką. Mają to być ciekawostki turystyczne, kulturowe, kulinarne z tego regionu. Przykładowo, 'Potrawy, ktore musisz sprobowac w [miasto]', lub 'najciekawsze miejsca do odwiedzenia w barcelonie'. Każdy post ma zawierać dane miejsce, tytuł, kategorie jakiej dotyczy post (do wyboru - atrakcje_turystyczne, kulinarne, kultura, rozrywka, zakupy, plaza_odpoczynek) oraz 5 podpunktów. Tytuł ma być zachęcający, np moze zawierac 'najpopularniejsze potrawy w [miejscowosc]' albo 'ktore warto zobaczyc' i ma miec informacje gdzie. Kazdy podpunkt ma miec naglowek. Proszę sporządzić 5 takich postów dla podanego miejsca. Format ma wygladac miej wiecej tak dla kazdego postu : {
#         "miejsce": "miejscowosc",
#         "tytuł": "tytul-do-podania", "kategoria": "podaj kategorie",
#         "podpunkty":
#             'naglowek1': "podpunkt1", 'naglowek2': "podpunkt2", 'naglowek3: "podpunkt3", 'naglowek4: "podpunkt4", 'naglowek5": "podpunkt5"
#         ]
#     }

# kategorie - atrakcje_turystyczne, kulinarne, kultura, rozrywka, zakupy, plaza_odpoczynek

alicante_facts = [
    {
        "miejsce": "Alicante",
        "tytuł": "Najlepsze plaże i zatoczki w Alicante",
        "kategoria": "Turystyka",
        "podpunkty": {
            "Plaża Postiguet": "Znana ze złocistego piasku i czystych wód, idealna do opalania i relaksu.",
            "Plaża San Juan": "Jedna z najpopularniejszych plaż w Alicante, o długości 7 kilometrów, oferuje szeroką gamę atrakcji i sportów wodnych.",
            "Zatoczka Tabarca": "Mała wyspa położona niedaleko wybrzeża Alicante, słynna z krystalicznie czystej wody i doskonałych miejsc do nurkowania.",
            "Plaża La Granadella": "Urokliwa plaża z turkusowymi wodami i otoczeniem klifów, idealna do spokojnego wypoczynku i nurkowania.",
            "Plaża El Postiguet": "Popularna plaża miejska w samym centrum Alicante, oferująca szeroki wybór barów i restauracji tuż przy brzegu morza."
        }
    },
    {
        "miejsce": "Alicante",
        "tytuł": "Kulinarne doznania Alicante",
        "kategoria": "Kulinarne",
        "podpunkty": {
            "Paella Alicante": "Tradycyjne danie z ryżu, kurczaka i warzyw, charakterystyczne dla regionu Alicante.",
            "Turron": "Słodka przekąska z miodu, migdałów i jajek, bardzo popularna w Alicante, szczególnie podczas świąt Bożego Narodzenia.",
            "Gazpacho": "Chłodna zupa pomidorowa z warzyw, idealna na gorące dni, popularna w całej Hiszpanii, w tym w Alicante.",
            "Fideuà": "Podobna do paelli, zamiast ryżu zawiera makaron, zazwyczaj serwowana z owocami morza, typowa potrawa alicantyńska.",
            "Arroz a Banda": "Klasyczne danie z ryżu gotowanego w bulionie z owocami morza, często podawane z alioli, typowe dla wybrzeża Alicante."
        }
    },
    {
        "miejsce": "Alicante",
        "tytuł": "Najlepsze zabytki i atrakcje Alicante",
        "kategoria": "Zabytki",
        "podpunkty": {
            "Zamek Santa Barbara": "Jeden z największych zamków w Hiszpanii, z pięknymi widokami na miasto i morze.",
            "Muzeum Archeologiczne Alicante": "Bogata kolekcja artefaktów archeologicznych, obejmująca okresy od prehistorii do średniowiecza.",
            "Wielka Synagoga Alicante": "Jedna z najlepiej zachowanych średniowiecznych synagog w Hiszpanii, z interesującymi eksponatami i wystawami.",
            "Basílica de Santa María": "Gotycki kościół z XIII wieku, z bogatym wystrojem wnętrza i imponującymi witrażami.",
            "Dzielnica Barrio Santa Cruz": "Urokliwa dzielnica z wąskimi uliczkami, kolorowymi domami i pięknymi widokami na morze, idealna na spacer."
        }
    },
    {
        "miejsce": "Alicante",
        "tytuł": "Nocne życie w Alicante",
        "kategoria": "Rozrywka",
        "podpunkty": {
            "Port of Alicante": "Popularne miejsce na wieczorne spacery z widokiem na morze oraz na drinka w jednej z licznych barów i klubów.",
            "El Barrio": "Tętniąca życiem dzielnica nocna, pełna barów, klubów i restauracji, idealna na wieczór z przyjaciółmi.",
            "Kasyno Alicante": "Dla miłośników hazardu, oferuje szeroki wybór gier, od automatów po poker, oraz restaurację i bary.",
            "Plaza del Ayuntamiento": "Centralny plac w Alicante, który wieczorem ożywa dzięki ulicznym artystom, muzyce na żywo i licznej restauracji.",
            "Club Tramps": "Jeden z najpopularniejszych klubów nocnych w Alicante, znany z imprez tematycznych i znakomitej muzyki."
        }
    },
    {
        "miejsce": "Alicante",
        "tytuł": "Alicante dla miłośników sportów wodnych",
        "kategoria": "Sport",
        "podpunkty": {
            "Windsurfing na Playa de San Juan": "Idealne miejsce do uprawiania windsurfingu dzięki silnym wiatrom i doskonałym warunkom na plaży San Juan.",
            "Nurkowanie w Zatoce Tabarca": "Krystalicznie czysta woda i bogate życie morskie sprawiają, że nurkowanie w Zatoce Tabarca jest niezapomnianym doświadczeniem.",
            "Kitesurfing na Playa de Arenales del Sol": "Znana z silnych wiatrów, plaża Arenales del Sol jest doskonałym miejscem do kitesurfingu dla początkujących i zaawansowanych.",
            "Żeglarstwo w Porcie Alicante": "Port Alicante oferuje szeroki wybór zajęć związanych z żeglarstwem, od wynajmu łodzi po kursy żeglarskie.",
            "Paddleboarding na Costa Blanca": "Spokojne wody Morza Śródziemnego sprawiają, że paddleboarding jest popularnym sportem wodnym na Costa Blanca, idealnym dla całej rodziny."
        }
    }
]
