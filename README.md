API Project - Artists and Works
================================

This project provides an API for managing artists and their works.

Requirements
------------
* Python 3.8 or later
* Django 3.2 or later
* Django REST Framework 3.12 or later

Installation
------------
1. Clone the repository:

    ```
    git clone https://github.com/ritikpatel17/DjangoArtistWorkAPI.git
    ```

2. Create a virtual environment and activate it:

    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

4. Run the migrations:

    ```
    python manage.py migrate
    ```

5. Create a superuser:

    ```
    python manage.py createsuperuser
    ```

6. Start the server:

    ```
    python manage.py runserver
    ```

Usage
-----
* To access the API, go to http://localhost:8000/api/
* To create a new artist, send a POST request to http://localhost:8000/api/artists/ with the following data:

    ```
    {
        "name": "Artist Name"
    }
    ```

* To create a new work, send a POST request to http://localhost:8000/api/works/ with the following data:

    ```
    {
        "link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "work_type": "YT"
    }
    ```

* To retrieve a list of artists, send a GET request to http://localhost:8000/api/artists/
* To retrieve a list of works, send a GET request to http://localhost:8000/api/works/
* To filter works by type, append the `work_type` parameter to the works endpoint, for example: http://localhost:8000/api/works/?work_type=YT
* To search for artists by name, append the `search` parameter to the artists endpoint, for example: http://localhost:8000/api/artists/?search=John
* To authenticate, send a POST request to http://localhost:8000/admin/ with the following data:

    ```
    {
        "username": "ritikpatel",
        "password": "rp123123"
    }
    ```
![Administration](./images/Administration.png)

![Artists Detail](./images/ArtistDetail.png)

![Works Detail](./images/WorkDetail.png)

