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

class RomaService:
    def __init__(self):
        self.descriptions = [
            "Rzym to miasto, gdzie historia ożywa na każdym kroku! 🏛️🌟 Przejdź się po starożytnych ruinach Koloseum, Forum Romanum i Panteonu, a poczujesz magię Wiecznego Miasta. Każda ulica kryje tajemnice przeszłości, które czekają na odkrycie przez Ciebie.",
            "Zanurz się w kulturze Rzymu, miasta pełnego sztuki i architektury! 🎨🏰 Odkryj wspaniałe muzea, galerie sztuki i barokowe kościoły, które zachwycą nawet najbardziej wymagających miłośników piękna. Niech Rzym stanie się Twoim artystycznym rajem.",
            "Rzym to raj dla smakoszy! 🍕🍝 Odkryj autentyczne smaki włoskiej kuchni w lokalnych trattoriach, delektując się pysznymi pastami, pizzą i gelato. Każdy posiłek w Rzymie to uczta dla podniebienia.",
            "Odkryj romantyczną stronę Rzymu, gdzie miłość unosi się w powietrzu! 💑 Spaceruj wzdłuż rzeki Tyber, odwiedzaj urocze kawiarnie i delektuj się kolacją przy świecach w sercu starego miasta. Rzym to idealne miejsce na romantyczne wakacje.",
            "Marzysz o przygodzie pełnej historii, kultury i wspaniałych widoków? Rzym to miejsce, które spełni Twoje marzenia! 🌞🏖️🎨 Zwiedzaj imponujące zabytki, spaceruj po malowniczych placach i ciesz się atmosferą tego niesamowitego miasta.",
            "Rzym to więcej niż miasto - to doświadczenie! 🌟🌴🎉 Poczuj niezwykłą energię Rzymu, biorąc udział w lokalnych festiwalach, koncertach i wydarzeniach kulturalnych. Niech Rzym stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
        ]
        self.hashtags = [
            "#Rome",
            "#Roma",
            "#Italy",
            "#VisitRome",
            "#TravelItaly",
            "#Italia",
            "#RomeCity",
            "#RomeLife",
            "#RomeViews",
            "#RomeHistory",
            "#RomeFood",
            "#RomeCulture",
            "#RomeTrip",
            "#RomeHoliday",
            "#RomeExplore",
            "#RomeTourism",
            "#RomeAttractions",
            "#RomeExperience",
            "#RomanHoliday",
            "#RomeAdventure"
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

class BarcelonaService:
    def __init__(self):
        self.descriptions = [
            "Barcelona to miasto, gdzie nowoczesność spotyka się z tradycją! 🏙️🌞 Odkryj arcydzieła Gaudiego, takie jak Sagrada Familia i Park Güell, spacerując po kolorowych ulicach pełnych życia. Każdy zakątek Barcelony tętni kulturą i historią.",
            "Zanurz się w rytmie Barcelony, gdzie życie toczy się w rytmie fiesty! 🎉💃 Uczestnicz w lokalnych festiwalach, odwiedzaj tętniące życiem targi i ciesz się niepowtarzalną atmosferą tego dynamicznego miasta.",
            "Barcelona to raj dla miłośników kuchni! 🍽️🍷 Delektuj się wyśmienitymi tapas, świeżymi owocami morza i wybornymi winami. Każdy posiłek w Barcelonie to niezapomniana kulinarna podróż.",
            "Odkryj romantyczną Barcelonę, gdzie magia miłości unosi się w powietrzu! 💑 Spaceruj wzdłuż plaży Barceloneta, podziwiaj zachody słońca i delektuj się romantyczną kolacją w jednej z urokliwych restauracji starego miasta.",
            "Czy marzysz o przygodzie pełnej słońca, morza i kultury? Barcelona to właśnie to miejsce! ☀️🏖️🎨 Zwiedzaj fascynujące muzea, relaksuj się na plaży i ciesz się artystyczną atmosferą miasta, które nigdy nie śpi.",
            "Barcelona to więcej niż miasto - to styl życia! 🌟🌴🎶 Poczuj niezwykłą energię Barcelony, biorąc udział w koncertach, wystawach i lokalnych wydarzeniach kulturalnych. Niech Barcelona stanie się Twoim ulubionym miejscem na wakacje pełne wrażeń."
        ]
        self.hashtags = [
            "#Barcelona",
            "#Catalonia",
            "#Spain",
            "#VisitBarcelona",
            "#TravelSpain",
            "#Espana",
            "#BarcelonaCity",
            "#BarcelonaLife",
            "#BarcelonaBeach",
            "#BarcelonaViews",
            "#BarcelonaSun",
            "#BarcelonaFood",
            "#BarcelonaCulture",
            "#BarcelonaHistory",
            "#BarcelonaTrip",
            "#BarcelonaHoliday",
            "#BarcelonaExplore",
            "#BarcelonaTourism",
            "#BarcelonaAttractions",
            "#BarcelonaExperience"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result

class BergamoService:
    def __init__(self):
        self.descriptions = [
            "Bergamo to urokliwe miasto, gdzie historia spotyka się z malowniczymi krajobrazami! 🏰🌄 Odkryj średniowieczne mury Città Alta, spacerując po wąskich uliczkach i podziwiając widoki, które zapierają dech w piersiach.",
            "Zanurz się w atmosferze Bergamo, miasta pełnego sztuki i kultury! 🎨🏛️ Odkryj bogactwo muzeów, galerii sztuki i zabytkowych kościołów, które odzwierciedlają długą i fascynującą historię tego miejsca.",
            "Bergamo to raj dla miłośników włoskiej kuchni! 🍝🍷 Delektuj się wyśmienitymi daniami, takimi jak casoncelli, polenta i lokalne wina. Każdy posiłek w Bergamo to uczta dla zmysłów.",
            "Odkryj romantyczną stronę Bergamo, gdzie każda chwila jest pełna magii! 💑 Spaceruj po malowniczych uliczkach starego miasta, podziwiaj widoki z góry i delektuj się romantyczną kolacją w jednej z uroczych restauracji.",
            "Czy marzysz o przygodzie pełnej historii, kultury i pięknych widoków? Bergamo to idealne miejsce! 🌞🏞️🎨 Zwiedzaj imponujące zabytki, spaceruj po malowniczych parkach i ciesz się atmosferą tego niezwykłego miasta.",
            "Bergamo to więcej niż miasto - to wyjątkowe doświadczenie! 🌟🌳🎉 Poczuj niezwykłą energię Bergamo, biorąc udział w lokalnych festiwalach, koncertach i wydarzeniach kulturalnych. Niech Bergamo stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
        ]
        self.hashtags = [
            "#Bergamo",
            "#Lombardy",
            "#Italy",
            "#VisitBergamo",
            "#TravelItaly",
            "#Italia",
            "#BergamoCity",
            "#BergamoLife",
            "#BergamoViews",
            "#BergamoHistory",
            "#BergamoFood",
            "#BergamoCulture",
            "#BergamoTrip",
            "#BergamoHoliday",
            "#BergamoExplore",
            "#BergamoTourism",
            "#BergamoAttractions",
            "#BergamoExperience",
            "#CittaAlta",
            "#BergamoMagic"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result



class BrindisiService:
    def __init__(self):
        self.descriptions = [
            "Brindisi to urokliwe nadmorskie miasto, gdzie historia i kultura łączą się z pięknymi plażami! 🏖️🌊 Odkryj starożytne zabytki, takie jak rzymskie kolumny i katedra, a następnie zrelaksuj się na piaszczystych wybrzeżach.",
            "Zanurz się w klimacie Brindisi, miasta pełnego śródziemnomorskiego uroku! 🌅🚤 Spaceruj po malowniczych nabrzeżach, podziwiaj jachty w porcie i ciesz się wspaniałymi widokami na Adriatyk.",
            "Brindisi to raj dla miłośników kuchni apulijskiej! 🍽️🍷 Delektuj się lokalnymi specjałami, takimi jak orecchiette, świeże owoce morza i wyborne wina. Każdy posiłek w Brindisi to prawdziwa uczta.",
            "Odkryj romantyczną stronę Brindisi, gdzie każda chwila nabiera wyjątkowego znaczenia! 💑 Spaceruj wzdłuż nadmorskiej promenady, podziwiaj zachody słońca i delektuj się kolacją przy świecach w jednym z urokliwych lokali.",
            "Czy marzysz o wakacjach pełnych słońca, morza i kultury? Brindisi to idealne miejsce! ☀️🌴🎨 Zwiedzaj fascynujące zabytki, relaksuj się na pięknych plażach i ciesz się autentyczną atmosferą tego południowego miasta.",
            "Brindisi to więcej niż tylko miasto - to prawdziwa przygoda! 🌟🌊🎉 Poczuj niezwykłą energię Brindisi, biorąc udział w lokalnych festiwalach, koncertach i wydarzeniach kulturalnych. Niech Brindisi stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
        ]
        self.hashtags = [
            "#Brindisi",
            "#Puglia",
            "#Italy",
            "#VisitBrindisi",
            "#TravelItaly",
            "#Italia",
            "#BrindisiCity",
            "#BrindisiLife",
            "#BrindisiViews",
            "#BrindisiHistory",
            "#BrindisiFood",
            "#BrindisiCulture",
            "#BrindisiTrip",
            "#BrindisiHoliday",
            "#BrindisiExplore",
            "#BrindisiTourism",
            "#BrindisiAttractions",
            "#BrindisiExperience",
            "#AdriaticSea",
            "#BrindisiSunset"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result


class ParisService:
    def __init__(self):
        self.descriptions = [
            "Paryż to miasto miłości, sztuki i historii! 🗼❤️ Odkryj ikoniczne zabytki, takie jak Wieża Eiffla, Luwr i Katedra Notre-Dame, spacerując po romantycznych uliczkach i bulwarach tego niezwykłego miasta.",
            "Zanurz się w kulturalnym bogactwie Paryża, gdzie sztuka i moda królują na każdym kroku! 🎨👗 Odwiedź słynne muzea, galerie sztuki i butiki, które czynią Paryż światową stolicą kultury i elegancji.",
            "Paryż to raj dla smakoszy! 🥐🍷 Delektuj się wyśmienitymi potrawami, od croissantów po wykwintne dania haute cuisine, w uroczych kawiarniach i restauracjach rozsianych po całym mieście.",
            "Odkryj romantyczną stronę Paryża, gdzie każdy zakątek emanuje magią miłości! 💑 Spaceruj brzegiem Sekwany, podziwiaj zachody słońca z Montmartre i delektuj się romantyczną kolacją przy świecach w jednej z wielu urokliwych restauracji.",
            "Czy marzysz o przygodzie pełnej sztuki, historii i niepowtarzalnych widoków? Paryż to miejsce, które spełni Twoje marzenia! 🌞🏛️🎨 Zwiedzaj imponujące zabytki, odkrywaj malownicze dzielnice i ciesz się atmosferą tego niesamowitego miasta.",
            "Paryż to więcej niż miasto - to doświadczenie życia! 🌟🌸🎶 Poczuj niezwykłą energię Paryża, biorąc udział w festiwalach, koncertach i wydarzeniach kulturalnych. Niech Paryż stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
        ]
        self.hashtags = [
            "#Paris",
            "#France",
            "#VisitParis",
            "#TravelFrance",
            "#ParisCity",
            "#ParisLife",
            "#ParisViews",
            "#ParisHistory",
            "#ParisFood",
            "#ParisCulture",
            "#ParisTrip",
            "#ParisHoliday",
            "#ParisExplore",
            "#ParisTourism",
            "#ParisAttractions",
            "#ParisExperience",
            "#EiffelTower",
            "#Louvre",
            "#NotreDame",
            "#CityOfLight"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result



class PisaService:
    def __init__(self):
        self.descriptions = [
            "Piza to miasto znane z kultowej Krzywej Wieży! 🏰🌟 Odkryj fascynujące zabytki, takie jak Katedra, Baptysterium i Plac Cudów, które przyciągają turystów z całego świata.",
            "Zanurz się w historii i kulturze Pizy, gdzie każde miejsce opowiada swoją unikalną historię! 🎨🏛️ Spaceruj po urokliwych uliczkach i podziwiaj piękno renesansowej architektury.",
            "Piza to raj dla miłośników toskańskiej kuchni! 🍝🍷 Delektuj się lokalnymi przysmakami, takimi jak pappardelle al cinghiale, cacciucco i wyśmienite wina. Każdy posiłek w Pizie to prawdziwa uczta.",
            "Odkryj romantyczną stronę Pizy, gdzie każda chwila nabiera wyjątkowego uroku! 💑 Spaceruj wzdłuż rzeki Arno, podziwiaj zachody słońca i delektuj się romantyczną kolacją przy świecach w jednym z urokliwych lokali.",
            "Czy marzysz o przygodzie pełnej historii, kultury i pięknych widoków? Piza to idealne miejsce! 🌞🏞️🎨 Zwiedzaj imponujące zabytki, spaceruj po malowniczych placach i ciesz się atmosferą tego niezwykłego miasta.",
            "Piza to więcej niż tylko miasto - to prawdziwe doświadczenie! 🌟🌳🎉 Poczuj niezwykłą energię Pizy, biorąc udział w lokalnych festiwalach, koncertach i wydarzeniach kulturalnych. Niech Piza stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
        ]
        self.hashtags = [
            "#Pisa",
            "#Tuscany",
            "#Italy",
            "#VisitPisa",
            "#TravelItaly",
            "#Italia",
            "#PisaCity",
            "#PisaLife",
            "#PisaViews",
            "#PisaHistory",
            "#PisaFood",
            "#PisaCulture",
            "#PisaTrip",
            "#PisaHoliday",
            "#PisaExplore",
            "#PisaTourism",
            "#PisaAttractions",
            "#PisaExperience",
            "#LeaningTower",
            "#PiazzaDeiMiracoli"
        ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result


class ZadarService:
    def __init__(self):
        def __init__(self):
            self.descriptions = [
                "Zadar to perła Adriatyku, gdzie historia spotyka się z pięknymi plażami! 🌊🏖️ Odkryj starożytne ruiny, rzymskie forum i unikalne instalacje, takie jak Morskie Organy i Powitanie Słońca.",
                "Zanurz się w atmosferze Zadar, miasta pełnego śródziemnomorskiego uroku! 🌅🚤 Spaceruj po malowniczych nabrzeżach, podziwiaj zachody słońca, które Alfred Hitchcock uważał za najpiękniejsze na świecie.",
                "Zadar to raj dla miłośników kuchni dalmatyńskiej! 🍽️🍷 Delektuj się lokalnymi specjałami, takimi jak peka, pašticada i wyborne wina. Każdy posiłek w Zadar to prawdziwa uczta.",
                "Odkryj romantyczną stronę Zadar, gdzie każda chwila jest pełna magii! 💑 Spaceruj po promenadzie Riva, podziwiaj widoki na morze i delektuj się romantyczną kolacją przy świecach w jednej z uroczych restauracji.",
                "Czy marzysz o przygodzie pełnej słońca, morza i kultury? Zadar to idealne miejsce! ☀️🏞️🎨 Zwiedzaj imponujące zabytki, relaksuj się na pięknych plażach i ciesz się autentyczną atmosferą tego nadmorskiego miasta.",
                "Zadar to więcej niż tylko miasto - to wyjątkowe doświadczenie! 🌟🌊🎉 Poczuj niezwykłą energię Zadar, biorąc udział w lokalnych festiwalach, koncertach i wydarzeniach kulturalnych. Niech Zadar stanie się Twoim ulubionym miejscem na niezapomniane wakacje."
            ]
            self.hashtags = [
                "#Zadar",
                "#Dalmatia",
                "#Croatia",
                "#VisitZadar",
                "#TravelCroatia",
                "#CroatiaFullOfLife",
                "#ZadarCity",
                "#ZadarLife",
                "#ZadarViews",
                "#ZadarHistory",
                "#ZadarFood",
                "#ZadarCulture",
                "#ZadarTrip",
                "#ZadarHoliday",
                "#ZadarExplore",
                "#ZadarTourism",
                "#ZadarAttractions",
                "#ZadarExperience",
                "#AdriaticSea",
                "#ZadarSunset"
            ]

    def get_random_description(self):
        return random.choice(self.descriptions)

    def get_10_random_hashtags(self):
        selected_hashtags = random.sample(self.hashtags, min(10, len(self.hashtags)))
        result = ''
        for hashtag in selected_hashtags:
            result += hashtag + ' '
        return result