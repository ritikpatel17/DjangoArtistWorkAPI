
from .myApp.models import Artist, Work

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoAssig.settings")
django.setup()

# create an artist
artist = Artist(name='Pablo Picasso')
artist.save()



# create a list of works
works = [
    Work(link='https://www.youtube.com/watch?v=1cIXHFsd16o', work_type='Youtube'),
    Work(link='https://www.instagram.com/p/BzF0AluHhZJ/', work_type='Instagram'),
    Work(link='https://www.pinterest.com/pin/772789617065822642/', work_type='Other')
]

# save each work and add them to the artist's work list
for work in works:
    work.save()
    artist.works.add(work)
