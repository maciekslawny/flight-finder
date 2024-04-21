from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
from decouple import config
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

class InstagramService():
    def __init__(self):
        self.post = None

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
