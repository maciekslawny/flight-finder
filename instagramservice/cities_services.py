import random

class MalagaService:
    def __init__(self):
        self.descriptions = [
            "Malaga to niezwykłe miasto, gdzie historia, kultura i przyroda spotykają się w doskonałym połączeniu! 🏛️🌿🌞 Odkryj urok starego miasta, spacerując po wąskich uliczkach pełnych barw i aromatów. Zanurz się w historii podczas zwiedzania fascynujących muzeów i zabytkowych budowli, a wieczorem rozkoszuj się relaksem na plaży, delektując się widokiem zachodzącego słońca nad Morzem Śródziemnym.",
            "Malaga to miejsce, gdzie czas płynie wolniej, a życie toczy się w rytmie hiszpańskiej fiesty! 🎉🎶 Zanurz się w lokalnej kulturze, uczestnicząc w tradycyjnych festiwalach i wydarzeniach, które ożywiają ulice miasta. Niezapomniane smaki, zapachy i dźwięki Malagi sprawią, że każda chwila będzie pełna radości i inspiracji!",
            "Odkryj Malagę jako idealne miejsce na romantyczne wakacje, gdzie słońce, morze i kultura tworzą niepowtarzalną atmosferę miłości i namiętności! 💑 Zacznij dzień od spokojnego spaceru po malowniczym nabrzeżu, a wieczorem rozkoszuj się romantyczną kolacją przy świecach w uroczym zaułku starego miasta.",
            "Malaga to prawdziwy raj dla miłośników kuchni śródziemnomorskiej! 🍽️🐟 Odkryj lokalne smaki, delektując się świeżymi owocami morza, aromatycznymi tapas i wykwintnymi winami regionu. Niech każdy posiłek w Maladze będzie kulinarnej przygodą, która zachwyci Twoje podniebienie i umysł!",
            "Czy marzysz o przygodzie pełnej słońca, morza i kultury? Malaga to właśnie to miejsce, gdzie Twoje marzenia się spełnią! ☀️🏖️🎨 Odkryj bogactwo artystyczne miasta, spacerując po ulicach, które inspirowały wielkich mistrzów. Zrelaksuj się na pięknych plażach Costa del Sol i pozwól się ponieść atmosferze swobody i radości, która w Maladze towarzyszy każdemu kroku.",
            "Malaga to więcej niż tylko miasto - to styl życia! 🌟🌴🎉 Odkryj niezwykłą energię Malagi, uczestnicząc w lokalnych wydarzeniach kulturalnych, festiwalach i koncertach, które ożywiają ulice miasta. Niech Malaga stanie się Twoim ulubionym miejscem na wakacje, gdzie każdy dzień jest pełen niespodzianek i przygód!"
        ]
        self.hashtags = [
            "#Malaga",
            "#CostaDelSol",
            "#Spain",
            "#VisitMalaga",
            "#TravelSpain",
            "#Espana",
            "#MalagaCity",
            "#MalagaLife",
            "#MalagaBeach",
            "#MalagaViews",
            "#MalagaSun",
            "#MalagaFood",
            "#MalagaCulture",
            "#MalagaHistory",
            "#MalagaTrip",
            "#MalagaHoliday",
            "#MalagaExplore",
            "#MalagaTourism",
            "#MalagaAttractions",
            "#MalagaExperience"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result

class NaplesService:
    def __init__(self):
        self.descriptions = [
            "Neapol to miasto, gdzie historia, kultura i smaki spotykają się w niezwykłym połączeniu! 🏰🍕🎭 Odkryj bogactwo zabytków, spacerując po uliczkach starego miasta, które pełne są tajemnic i legend. Zanurz się w aromacie prawdziwej włoskiej kuchni, degustując wyśmienite pizze, makaron i inne lokalne specjały. Niech Neapol stanie się Twoim miejscem, gdzie każdy kęs to podróż przez smaki i historię!",
            "Czy marzysz o wakacjach pełnych słońca, morza i kultury? Neapol to miejsce, gdzie Twoje marzenia się spełnią! ☀️🏖️🎨 Odkryj malownicze plaże Zatoki Neapolitańskiej, gdzie błękitne fale zapraszają do kąpieli i relaksu. Po dniu pełnym wrażeń, pozwól się ponieść atmosferze swobody i radości, uczestnicząc w tradycyjnych neapolitańskich festiwalach i wydarzeniach kulturalnych.",
            "Neapol to prawdziwy raj dla miłośników kulinariów! 🍝🍷 Odkryj lokalne smaki, degustując wyśmienite potrawy przygotowywane ze świeżych składników, które zachwycą Twoje podniebienie i umysł. Niech każdy posiłek w Neapolu będzie kulinarnej przygodą, która wciągnie Cię w wir smaków i aromatów!",
            "Odkryj Neapol jako idealne miejsce na romantyczne wakacje, gdzie słońce, morze i kultura tworzą niepowtarzalną atmosferę miłości i namiętności! 💑 Zacznij dzień od spokojnego spaceru po urokliwych uliczkach starego miasta, a wieczorem rozkoszuj się romantyczną kolacją przy świecach w przytulnej restauracji nad brzegiem morza.",
            "Neapol to więcej niż tylko miasto - to styl życia! 🌟🌊🎉 Odkryj niezwykłą energię Neapolu, uczestnicząc w lokalnych wydarzeniach kulturalnych, festiwalach i koncertach, które ożywiają ulice miasta. Niech Neapol stanie się Twoim ulubionym miejscem na wakacje, gdzie każdy dzień jest pełen niespodzianek i przygód!"
        ]
        self.hashtags = [
            "#Naples",
            "#Italy",
            "#VisitNaples",
            "#TravelItaly",
            "#Italia",
            "#NaplesCity",
            "#NaplesLife",
            "#NaplesBeach",
            "#NaplesViews",
            "#NaplesSun",
            "#NaplesFood",
            "#NaplesCulture",
            "#NaplesHistory",
            "#NaplesTrip",
            "#NaplesHoliday",
            "#NaplesExplore",
            "#NaplesTourism",
            "#NaplesAttractions",
            "#NaplesExperience"
        ]
    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result

class AlicanteService:
    def __init__(self):
        self.descriptions = [
            "Alicante to niezwykłe miejsce, gdzie spotykają się cudowne plaże, niebiańskie widoki i niezapomniane smaki! 🏖️🌅🍹 Pozwól sobie na chwilę relaksu nad błękitnym Morzem Śródziemnym, rozkoszując się promieniami słońca i świeżym powietrzem. Wieczorem wyrusz na spacer po urokliwych uliczkach Starego Miasta, gdzie tradycja łączy się z nowoczesnością, tworząc niepowtarzalną atmosferę. Niech Alicante stanie się Twoim miejscem, gdzie każdy dzień jest pełen radości i inspiracji! ✨😊",
            "Odkryj urok Alicante, gdzie słońce świeci przez większość roku, a życie toczy się spokojnie i beztrosko. ☀️🌴🌊 Zanurz się w relaksującym rytmie plażowego życia, delektując się morskimi smakołykami i kolorowymi drinkami. Spacerując po historycznych uliczkach, poczuj magię hiszpańskiej kultury i tradycji, która otacza Cię na każdym kroku. Alicante to miejsce, gdzie czas zwalnia, a każda chwila jest warta zapamiętania! 🚶‍♀️🌺",
            "Wakacje w Alicante to więcej niż tylko plażowanie - to odkrywanie nowych kultur, tradycji i smaków! 🌍🍽️ Poznaj lokalną społeczność, uczestnicząc w festiwalach i wydarzeniach kulturalnych, które ożywiają miasto, i zanurz się w atmosferze radości i świętowania.",
            "Czy masz ochotę na romantyczną kolację wzdłuż nabrzeża, smakowite tapasy w lokalnej tawernie, czy może chwile relaksu na plaży? W Alicante znajdziesz wszystko, czego potrzebujesz! 💖 Zacznij dzień od porannej jogi na plaży, delektując się widokiem wschodu słońca nad morzem, a potem pozwól się ponieść hiszpańskiej muzyce i tańcom podczas wieczornego fiestas.",
            "Alicante to prawdziwa oaza dla miłośników natury, kultury i kulinariów! 💖🌴☀️ Przemierzaj piękne plaże, odkrywaj tajemnicze zakamarki Starego Miasta i delektuj się wykwintnymi hiszpańskimi potrawami. Niech Alicante stanie się Twoim rajem na ziemi, gdzie każdy dzień to nowa przygoda!",
            "Odkryj Alicante jako idealne miejsce na romantyczne wakacje, gdzie słońce, morze i kultura tworzą niepowtarzalną atmosferę miłości i namiętności! 💑 Zacznij dzień od spokojnego spaceru po plaży, a wieczorem rozkoszuj się romantyczną kolacją przy świecach w uroczym restauracyjnym zaułku.",
            "Alicante to prawdziwy skarb Costa Blanca, gdzie czekają na Ciebie niezapomniane przygody i niezliczone atrakcje! ✨🌴🌊 Zrelaksuj się na błogiej plaży, odkrywaj historyczne zabytki i rozkoszuj się lokalnymi przysmakami, które zachwycą Twoje podniebienie. Niech Alicante stanie się Twoim ulubionym miejscem na wakacje!",
            "Odkryj Alicante jako idealne miejsce na rodzinne wakacje, gdzie czekają na Ciebie niezapomniane przygody i mnóstwo zabawy! 🌞👨‍👩‍👧‍👦🎉 Spędź dzień na plaży, delektując się zabawami w wodzie i budując zamki z piasku, a wieczorem skosztuj tradycyjnych przysmaków w przytulnych restauracjach.",
            "Czy marzysz o przygodzie pełnej słońca, morza i uśmiechu? Alicante to właśnie to miejsce, gdzie Twoje marzenia się spełnią! ☀️🏖️😊 Odkryj malownicze plaże Costa Blanca, gdzie złocisty piasek i błękitne fale zapraszają do zabawy i relaksu. Niech Alicante stanie się Twoim rajem na ziemi, gdzie każdy dzień to przygoda pełna słońca, morza i uśmiechu! 🌟🍹",
            "Alicante to nie tylko miejsce na wakacje - to miejsce, gdzie marzenia stają się rzeczywistością! 🌟🏖️🌈 Odkryj malownicze plaże Costa Blanca, gdzie złocisty piasek i błękitne fale zapraszają do zabawy i relaksu. Po dniu pełnym wrażeń, zanurz się w lokalnym życiu nocnym, uczestnicząc w tradycyjnych hiszpańskich fiestach i festiwalach. Alicante to miejsce, gdzie każda chwila jest warta zapamiętania! 🎉💃🍹"
        ]
        self.hashtags = [
            "#Alicante",
            "#CostaBlanca",
            "#Spain",
            "#VisitAlicante",
            "#TravelSpain",
            "#Espana",
            "#AlicanteCity",
            "#AlicanteLife",
            "#AlicanteBeach",
            "#AlicanteViews",
            "#AlicanteSun",
            "#AlicanteFood",
            "#AlicanteCulture",
            "#AlicanteHistory",
            "#AlicanteTrip",
            "#AlicanteHoliday",
            "#AlicanteExplore",
            "#AlicanteTourism",
            "#AlicanteAttractions",
            "#AlicanteExperience"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result

