import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'djangobasics.settings')

import django
django.setup()

import random

from faker import Faker
from first_app.models import Topic,Webpage,AccessRecords

#create faker object
fake_obj = Faker()
topics = ["technology","blogging","travelling","books"]

def add_topics():
    top = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    top.save()
    return top

def populate_others(A=4):
    for i in range(A):
        topic = add_topics()

        fake_url = fake_obj.url()
        fake_name = fake_obj.company()
        fake_date = fake_obj.date()

        web_pg = Webpage.objects.get_or_create(top_name=topic,name=fake_name,url=fake_url)[0]
        acc_rec = AccessRecords.objects.get_or_create(web_name=web_pg,create_dt=fake_date)[0]

if __name__ == '__main__':
    print("creating fake data")
    populate_others(4)
    print("fake records created!")
