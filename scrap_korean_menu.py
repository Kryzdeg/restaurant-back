from requests_html import HTMLSession
import re
from core.models import Meal


session = HTMLSession()
r = session.get('http://masiso.pl/menu/')
all_texts = [x.text for x in r.html.find('div.elementor-column.elementor-col-100.elementor-top-column.elementor-element')]

regex = r"((\w+ ?)+)\n(.+ ?)+\n(\d+)zł(\n(\w+[\s-]?)+)?"
meals = []

all_texts.pop(0)
all_texts.pop(0)
all_texts.pop()

# print(all_texts)

for i, text in enumerate(all_texts):
    if text == "":
        all_texts.remove("")
        continue    
    try:
        meal = re.match(regex, text)
        if meal:
            meals.append(meal.groups())
    except:
        pass

data = dict()

type_meal = 'starter'
for i, meal in enumerate(meals):
    if meal[0] in ["Ryż", "Makaron", "Suchy makaron"]:
        continue

    m = {
        "id": i + 1,
        "name": meal[0],
        "namek": meal[2],
        "price": meal[3],
        "description": meal[4],
        "meal_type": type_meal
    }

    if meal[0] == "Tteokbokki":
        type_meal = "dinner"
    
    if meal[0] == "Odeng Tang":
        type_meal = "grill"

    Meal.objects.create(
        name=m['name'],
        namek=m["namek"],
        price=m["price"],
        description=m["description"],
        meal_type=m["meal_type"]
    )
