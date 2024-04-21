import random


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

