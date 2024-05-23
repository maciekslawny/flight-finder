from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from decouple import config
import random
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagramservice.facts import alicante_facts, malaga_facts
import os


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
        background = Image.open(f"instagramservice/images/instagram_post_images/cities-bg/{background_image}")

        # Ustaw czcionkę i tekst
        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  210)  # Wybierz czcionkę i rozmiar
        draw = ImageDraw.Draw(background)

        # Uzyskaj granice obszaru zawierającego tekst

        text_price = draw.textbbox((0, -200), str(self.post.price) + ' PLN', font=font)
        text_price_position = ((background.width - text_price[2]) // 2, (background.height - text_price[3]) // 2)

        draw.text(text_price_position, str(self.post.price) + ' PLN', fill="white", font=font)

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
        background = Image.open(f"instagramservice/images/story-tlo.jpg")

        # Ustaw czcionkę i tekst
        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  110)  # Wybierz czcionkę i rozmiar
        draw = ImageDraw.Draw(background)

        # Tekst
        text = "LOTY NA MAJ"
        text_color = "black"
        background_color = "white"

        # Pozycja tekstu
        text_width = draw.textlength(text, font=font)
        x = 120
        y = 140

        # Narysuj tło dla tekstu
        draw.rounded_rectangle([x - 20, y, x + text_width + 20, y + 130], radius=50, fill=background_color)

        # Narysuj tekst na tle
        draw.text((x, y), text, fill=text_color, font=font)

        font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                  90)
        text = "Wyloty z Gdańska:"
        text_width = draw.textlength(text, font=font)
        x = 90
        y = 500
        text_width = draw.textlength(text, font=font)
        draw.text((x, y), text, fill=text_color, font=font)

        current_position = 630
        for flight in self.flights_queryset:
            print(flight)

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      70)
            text = f"{flight.ticket.flight.arrival_city} - {flight.total_price} zł "
            text_width = draw.textlength(text, font=font)
            x = 90
            y = current_position
            text_width = draw.textlength(text, font=font)
            draw.text((x, y), text, fill=text_color, font=font)

            current_position += 70

            font = ImageFont.truetype("flightfinder/management/commands/fonts/Rubik-Bold.ttf",
                                      60)
            text = f"Wylot: {str(flight.ticket.flight.flight_date)[5:10]}  -  Powrót: {str(flight.return_ticket.flight.flight_date)[5:10]}"
            text_width = draw.textlength(text, font=font)
            x = 90
            y = current_position
            text_width = draw.textlength(text, font=font)
            draw.text((x, y), text, fill=text_color, font=font)

            current_position += 100

        # Zapisz obraz jako plik JPEG
        background.save(f"instagramservice/images/instagram_post_images/story-{self.story.id}.jpg")
