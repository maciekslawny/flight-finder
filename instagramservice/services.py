from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from decouple import config
import random
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagramservice.facts import alicante_facts, malaga_facts
import os
from flightfinder.models import City


class InstagramService():
    def __init__(self):
        self.post = None
        self.post_fact = None
        self.story = None
        self.flights_queryset = None

    def create_post_image(self):
        background_image = ''
        if self.post.arrival_city == 'Alicante':
            background_image = 'alicante-tlo.jpg'
        if self.post.arrival_city == 'Neapol':
            background_image = 'neapol-tlo.jpg'
        if self.post.arrival_city == 'Malaga':
            background_image = 'malaga-tlo.jpg'
        if self.post.arrival_city == 'Barcelona':
            background_image = 'barcelona-tlo.jpg'
        if self.post.arrival_city == 'Bergamo':
            background_image = 'bergamo-tlo.jpg'
        if self.post.arrival_city == 'Brindisi':
            background_image = 'brindisi-tlo.jpg'
        if self.post.arrival_city == 'Paryz':
            background_image = 'paryz-tlo.jpg'
        if self.post.arrival_city == 'Piza':
            background_image = 'piza-tlo.jpg'
        if self.post.arrival_city == 'Rzym':
            background_image = 'rzym-tlo.jpg'
        if self.post.arrival_city == 'Zadar':
            background_image = 'zadar-tlo.jpg'
        # Wczytaj istniejący obrazek
        background = Image.open(f"instagramservice/images/instagram_post_new/{str(self.post.arrival_city).lower()}-tlo-1.jpg")

        # Ustaw czcionkę i tekst
        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  130)  # Wybierz czcionkę i rozmiar
        draw = ImageDraw.Draw(background)

        # Uzyskaj granice obszaru zawierającego tekst


        price = f'{self.post.price}'
        _, _, text_width, h = draw.textbbox((0, 0), price, font=font)




        price_end_position = 895

        if text_width > 240:
            price_end_position = 915

        text_price_position = (price_end_position - text_width, -3)

        draw.text(text_price_position, str(price), fill="white", font=font)





        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  70)  # Wybierz czcionkę i rozmiar
        text_price_position = (925, 52)
        draw.text(text_price_position, str('PLN'), fill="white", font=font)



        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  60)  # Wybierz czcionkę i rozmiar


        departure_city_instance = City.objects.get(name=self.post.departure_city)
        if departure_city_instance.genitive:
            text = f'z {departure_city_instance.genitive}'
        else:
            text = f'z {departure_city_instance.name}'



        _, _, text_width, h = draw.textbbox((0, 0), text, font=font)


        print('width', text_width)

        text_size = 60
        if text_width > 390:
            text_size = 45

        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  text_size)
        _, _, text_width, h = draw.textbbox((0, 0), text, font=font)
        text_price_position = (1060 - text_width, 140)
        draw.text(text_price_position, str(text), fill="white", font=font)




        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  70)

        date_text = f'{str(self.post.flight_date)[8:10]}.{str(self.post.flight_date)[5:7]} - {str(self.post.flight_return_date)[8:10]}.{str(self.post.flight_return_date)[5:7]}'

        _, _, text_width, h = draw.textbbox((0, 0), date_text, font=font)

        print('width', text_width)


        text_price_position = (315 - (text_width/2), 911)
        draw.text(text_price_position, str(date_text), fill="white", font=font)




        # Zapisz obraz jako plik JPEG
        background.save(f"instagramservice/images/instagram_post_images/post-{self.post.id}.jpg")

    def publish_post(self):
        cl = Client()
        ACCOUNT_USERNAME = config('INSTAGRAM_LOGIN')
        ACCOUNT_PASSWORD = config('INSTAGRAM_PASSWORD')
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        medias = cl.user_medias(user_id, 20)

        test = cl.photo_upload(f"instagramservice/images/instagram_post_images/post-{self.post.id}.jpg",
                               self.post.description)
        print('RESPONSE TEST: ', test)

    from PIL import Image, ImageDraw, ImageFont

    def create_post_fact_images(self):
        title = self.post_fact.fact.title
        title_split = title.split(' ')
        flag_word = ''
        result_words_list = []
        for x, word in enumerate(title_split):
            print(word)

            if x == 0:
                flag_word = word

            elif len(flag_word) > 6:
                result_words_list.append(flag_word)
                flag_word = word
            else:
                flag_word = flag_word + ' ' + word

            if x == len(title_split) - 1:
                result_words_list.append(flag_word)

        longest_word = len(max(result_words_list, key=len))

        font_size = 125
        space = 130
        if len(result_words_list) > 4 or longest_word > 12:
            font_size = 110
            space = 115

        print(result_words_list)

        files = os.listdir(f"instagramservice/images/instagram_posts_facts/background/{self.post_fact.fact.category}/")
        file_count = len(files)
        img_id = random.randint(1, file_count)
        print('LICZBA PLIKOW', file_count)

        background = Image.open(
            f"instagramservice/images/instagram_posts_facts/background/{self.post_fact.fact.category}/{self.post_fact.fact.img_id}.jpg")
        W, H = 1080, 1080
        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  font_size)  # Wybierz czcionkę i rozmiar
        draw = ImageDraw.Draw(background)

        y = 150
        for text in result_words_list:
            _, _, w, h = draw.textbbox((0, -200 + len(result_words_list) * 150), text, font=font)
            draw.text((40 + 5, (H - h) / 2 + y + 5), text, fill="#F9d9b8", font=font)
            draw.text((40, (H - h) / 2 + y), text, fill="#fdbd76", font=font)
            # draw.text((40, (H-h)/2 + y), text, fill="#fdbd76", font=font)

            y = y + space

        # Zapisz obraz jako plik JPEG
        background.save(f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-1-tlo.jpg")

        items = {self.post_fact.fact.title_1: self.post_fact.fact.description_1,
                 self.post_fact.fact.title_2: self.post_fact.fact.description_2,
                 self.post_fact.fact.title_3: self.post_fact.fact.description_3,
                 self.post_fact.fact.title_4: self.post_fact.fact.description_4,
                 self.post_fact.fact.title_5: self.post_fact.fact.description_5}

        for number, fact in enumerate(items):

            if number == len(items) - 1:
                background = Image.open(f"instagramservice/images/post-fact-bg-3.jpg")
            else:
                background = Image.open(f"instagramservice/images/post-fact-bg-2.jpg")

            # NUMEREK

            W, H = 1080, 1080
            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      100)  # Wybierz czcionkę i rozmiar
            draw = ImageDraw.Draw(background)
            number_dot = str(number + 1) + '.'
            _, _, w, h = draw.textbbox((0, 0), number_dot, font=font)
            draw.text(((W - w) / 2, 187), number_dot, fill="#F9d9b8", font=font)
            draw.text(((W - w) / 2, 185), number_dot, fill="#fdbd76", font=font)

            # PODTYTUŁ
            subtitle = list(items.keys())[number]
            print(subtitle)
            if len(subtitle) <= 20:
                font_size = 90
            elif 30 > len(subtitle) > 20:
                font_size = 70
            elif 30 <= len(subtitle) < 35:
                font_size = 60
            else:
                font_size = 50

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      font_size)
            _, _, w, h = draw.textbbox((0, 0), subtitle, font=font)
            draw.text(((W - w) / 2, 380), subtitle, fill="#F9d9b8", font=font)
            draw.text(((W - w) / 2, 383), subtitle, fill="#fdbd76", font=font)

            # OPIS
            description = list(items.values())[number]
            print('DLUGOSC DESC:', len(description), description)
            if len(description) <= 150:
                font_size = 60
                text_gap = 70
            elif 151 > len(description) > 170:
                font_size = 55
                text_gap = 65
            elif 171 > len(description) > 185:
                font_size = 50
                text_gap = 65
            else:
                font_size = 45
                text_gap = 55
            text_split = description.split(' ')
            flag_word = ''
            description_lines_list = []
            for x, word in enumerate(text_split):
                print(word)

                if x == 0:
                    flag_word = word

                elif len(flag_word) > 17:
                    description_lines_list.append(flag_word)
                    flag_word = word
                else:
                    flag_word = flag_word + ' ' + word

                if x == len(text_split) - 1:
                    description_lines_list.append(flag_word)

            print(description_lines_list)
            height = 525
            for description_line in description_lines_list:
                font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                          font_size)
                _, _, w, h = draw.textbbox((0, 0), description_line, font=font)
                draw.text(((W - w) / 2, height + 3), description_line, fill="white", font=font)
                draw.text(((W - w) / 2, height), description_line, fill="black", font=font)
                height += text_gap

            # Zapisz obraz jako plik JPEG
            background.save(
                f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-{number + 1}.jpg")

    def upload_post_fact(self):

        cl = Client()
        ACCOUNT_USERNAME = config('INSTAGRAM_LOGIN')
        ACCOUNT_PASSWORD = config('INSTAGRAM_PASSWORD')
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        medias = cl.user_medias(user_id, 20)

        photo_list = [
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-1-tlo.jpg",
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-1.jpg",
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-2.jpg",
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-3.jpg",
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-4.jpg",
            f"instagramservice/images/instagram_posts_facts/post-fact-title-{self.post_fact.id}-5.jpg"
        ]

        test = cl.album_upload(photo_list,
                               self.post_fact.fact.description + '\n' + self.post_fact.fact.hashtags)
        print('RESPONSE TEST: ', test)

    def create_story_image(self):
        # Wczytaj istniejący obrazek
        background = Image.open(f"instagramservice/images/tlo-story.jpg")

        # Ustaw czcionkę i tekst
        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  110)  # Wybierz czcionkę i rozmiar
        draw = ImageDraw.Draw(background)

        # Tekst
        text = "PROPOZYCJE  LOTÓW"
        text_color = "white"
        background_color = "white"




        current_position = 365

        used_cities = []
        for flight in self.flights_queryset:

            if flight.ticket.flight.arrival_city in used_cities:
                continue
            used_cities.append(flight.ticket.flight.arrival_city)

            text = f"{flight.ticket.flight.departure_city} - {flight.ticket.flight.arrival_city}"
            if len(text) > 17:
                size = 59
            else:
                size = 64

            image = 610

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      size)

            text_width = draw.textlength(text, font=font)
            print('text_width', text_width)
            x = 30
            y = current_position
            draw.text((image - text_width, y), text, fill=text_color, font=font)


            text_price = f'{flight.total_price} PLN'
            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      85)

            text_width = draw.textlength(text_price, font=font)
            print('text_width', text_width)
            x = 30
            y = current_position
            draw.text((image - text_width + 455, y), text_price, fill=text_color, font=font)


            text = 'w 2 strony!'
            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Regular.ttf",
                                      51)

            text_width = draw.textlength(text, font=font)
            print('text_width', text_width)
            x = 30
            y = current_position
            draw.text((image - text_width + 455, y+90), text, fill=text_color, font=font)




            current_position += 70

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Regular.ttf",
                                      55)
            text = f"Wylot: {str(flight.ticket.flight.flight_date)[8:10]}.{str(flight.ticket.flight.flight_date)[5:7]}"
            text_width = draw.textlength(text, font=font)
            x = 30
            y = current_position
            text_width = draw.textlength(text, font=font)
            draw.text((image - text_width, y), text, fill=text_color, font=font)

            current_position += 70

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Regular.ttf",
                                      55)
            text = f"Powrót: {str(flight.return_ticket.flight.flight_date)[8:10]}.{str(flight.return_ticket.flight.flight_date)[5:7]}"
            text_width = draw.textlength(text, font=font)
            x = 30
            y = current_position
            text_width = draw.textlength(text, font=font)
            draw.text((image - text_width, y), text, fill=text_color, font=font)

            current_position += 145

        # Zapisz obraz jako plik JPEG
        background.save(f"instagramservice/images/instagram_post_images/story-{self.story.id}.jpg")
