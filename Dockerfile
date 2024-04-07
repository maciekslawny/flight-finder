FROM python:3.10

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki projektu do katalogu roboczego kontenera
COPY . /app/


COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

# Zainstaluj zależności projektu
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y redis-tools

# Ustaw zmienną środowiskową dla Chrome
ENV CHROME_BIN=/usr/bin/google-chrome

# Zainstaluj Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Pobierz i zainstaluj ChromeDriver
RUN LATEST_CHROMEDRIVER=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && mv /usr/bin/chromedriver-linux64 /usr/bin/chromedriver \
    && rm /tmp/chromedriver.zip


# Dodaj ścieżkę do ChromeDrivera do zmiennej PATH
ENV PATH="/usr/bin/chromedriver:${PATH}"

# Dodaj ścieżkę do ChromeDrivera do zmiennej PATH
ENV PATH="/usr/bin:${PATH}"

# Tworzymy dowiązanie symboliczne do chromedriver-linux64 jako chromedriver
RUN ln -s /usr/bin/chromedriver-linux64 /usr/bin/chromedriver

# Usuń starszą wersję ChromeDrivera
RUN rm -rf /root/.cache/selenium/chromedriver/linux64/114.0.5735.90/chromedriver

# Uruchom serwer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]