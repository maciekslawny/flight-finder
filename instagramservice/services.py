from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from decouple import config
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

class InstagramService():
    def __init__(self):
        self.post = None
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

        # Wczytaj istniejący obrazek
        background = Image.open(f"instagramservice/images/{background_image}")

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

        test = cl.photo_upload(f"instagramservice/images/instagram_post_images/post-{self.post.id}.jpg", self.post.description)
        print('RESPONSE TEST: ', test)

    from PIL import Image, ImageDraw, ImageFont

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