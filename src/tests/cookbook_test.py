import pytest

from ..core import Recipe, Ingredient, Difficulty
from ..core.cookbook import Cookbook


@pytest.fixture()
def recipe_1():
    name = "Puszyste placki z jabłkami"
    ingredients = [Ingredient("mąka pszenna", 150, "g"),
                   Ingredient("zimne mleko", 200, "ml"),
                   Ingredient("jajko", 1),
                   Ingredient("cukier waniliowy", 1, "tsp"),
                   Ingredient("cynamon", 1, "tsp"),
                   Ingredient("proszek do pieczenia", 1, "tsp"),
                   Ingredient("jabłko", 2),
                   Ingredient("olej", 100, "ml")]
    description = ["W misce wymieszaj mąkę, cukier, cynamon, proszek do pieczenia, jajo z zimnym mlekiem.",
                   "Jabłko obierz, pokrój w małe kawałki i wymieszaj z ciastem.",
                   "Placki z jabłkami smaż na rozgrzanej patelni, z 2 łyżkami oleju, z obu stron na złoty kolor."]
    difficulty = Difficulty.EASY
    estimated_time = 15
    related_links = "https://www.przepisy.pl/przepis/puszyste-placki-z-jablkami"

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_2():
    name = "Magiczne ciasto"
    ingredients = [Ingredient("żółtka jajek", 3),
                   Ingredient("białka jajek", 2),
                   Ingredient("cukier", 90, "g"),
                   Ingredient("masło", 90, "g"),
                   Ingredient("mąka pszenna", 90, "g"),
                   Ingredient("mleko", 375, "ml"),
                   Ingredient("woda", 2, "tbsp"),
                   Ingredient("sól", 1, "pn"),
                   Ingredient("ekstrakt waniliowy", 1, "odrobina"), # TODO: Handle very small amounts of the ingredient (tylko nazwa np.)
                   Ingredient("cukier puder", 1, "odrobina")]
    description = ["Białka oddzielamy od żółtek. Żółtka z cukrem oraz łyżka wody ubijamy na puszystą masę.",
                   "Stopniowo dodajemy roztopione i ostudzone masło oraz ekstrakt waniliowy.",
                   "Do masy przesiewamy mąkę, dokładnie miksujemy.",
                   "Pod koniec wlewamy letnie mleko i ponownie mieszamy.",
                   "Na końcu dodajemy ubitą pianę z białek. Mieszamy całość delikatnie drewnianą szpatułką.",
                   "Formę smarujemy masłem i wykładamy papierem do pieczenia. Przelewamy ciasto. Pieczemy je ok 70 min ( góra, dół). Upieczone ciasto wyjmujemy z piekarnika i studzimy. Następnie wkładamy do lodówki i dobrze chłodzimy.",
                   "Przed podaniem posypujemy cukrem pudrem. Ciasto w przekroju posiada trzy różne warstwy."]
    difficulty = Difficulty.EASY
    estimated_time = 10
    related_links = "https://www.przepisy.pl/przepis/magiczne-ciasto"

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_3():
    name = "Ekspresowe ciasto"
    ingredients = [Ingredient("jajko", 3),
                   Ingredient("cukier", 240, "g"),
                   Ingredient("mleko 3.2%", 150, "ml"),
                   Ingredient("olej", 120, "ml"),
                   Ingredient("mąka pszenna", 300, "g"),
                   Ingredient("proszek do pieczenia", 1, "tsp"),
                   Ingredient("owoce leśne (świeże lub mrożone)", 250, "g")]
    description = ["Jajka na wilgotne ciasto na oleju ubij z cukrem, aż będą jasne i puszyste. Dodaj mleko i olej, wymieszaj.",
                   "Teraz dodaj do biszkoptu przesianą mąkę pszenną z proszkiem do pieczenia i wymieszaj miękką łyżką.",
                   "Foremkę o wymiarach 20 na 20 cm wyłóż papierem do pieczenia, wlej przygotowane wilgotne ciasto na oleju i posyp owocami (zamrożonymi). Piecz w temperaturze 170–180°Cprzez ok. 45 minut do nawet godziny, w zależności od piekarnika – do suchego patyczka."]
    difficulty = Difficulty.EASY
    estimated_time = 10
    related_links = "https://www.przepisy.pl/przepis/ekspresowe-ciasto-11993"

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_4():
    name = "Ciasto na słodkie naleśniki"
    ingredients = [Ingredient("mąka pszenna", 1, "glass"),
                   Ingredient("jajko", 2),
                   Ingredient("mleko", 0.5, "glass"),
                   Ingredient("woda mineralna", 0.5, "glass"),
                   Ingredient("cukier waniliowy", 1, "tbsp"),
                   Ingredient("miód", 1, "tbsp"),
                   Ingredient("olej", 30, "ml"),
                   Ingredient("sól", 1, "pn"),
                   Ingredient("tłuszcz do smażenia", 30, "g")]
    description = ["Do miski wbij jajka i wymieszaj z cukrem i miodem. Następnie dodaj pozostałe składniki – mąkę, mleko, wodę, sól oraz olej – i wymieszaj używając do tego miksera. Ciasto powinno uzyskać gładką konsystencję.",
                   "Na rozgrzanej i posmarowanej lekko tłuszczem patelni smaż naleśniki na złoty kolor z obu stron. Cukier waniliowy możesz sam przygotować w domowych warunkach – przekrojoną laskę wanilii włóż do słoiczka, a następnie zasyp ją zwykłym cukrem, zakręć słoik i pozostaw na kilka dni."]
    difficulty = Difficulty.EASY
    estimated_time = 10
    related_links = "https://www.przepisy.pl/przepis/ciasto-nalesnikowe-na-slodko"

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipe_5():
    name = "Wiosenny gulasz"
    ingredients = [Ingredient("wołowina", 500, "g"),
                   Ingredient("cebula", 1),
                   Ingredient("fix Knorr: 'Gulasz węgierski'", 1),
                   Ingredient("czosnek", 2, "ząbki"), # TODO: Poprawić
                   Ingredient("papryka czerwona", 2),
                   Ingredient("marchewka", 2),
                   Ingredient("liść laurowy", 2),
                   Ingredient("oliwa", 1, "tbsp")]
    description = ["Pokrój mięso w kostkę. Pokrój cebulę w półksiężyce. Pokrój czosnek w plasterki. Usuń z papryk gniazda nasienne i pokrój je w kostkę. Pokrój marchewkę w plasterki.",
                   "Rozgrzej 0.5 łyżki oliwy w dużym garnku na średnim ogniu. Wrzuć pokrojone w kostkę mięso i poczekaj aż się zrumieni z każdej strony. Smaż ok. 5 min. Odstaw.",
                   "Dodaj do garnka 0.5 łyżki oliwy. Podsmaż cebule i czosnek aż po 3-4 min. zaczną wydzielać aromat. Dodaj marchewki i papryki, gotuj dalej przez około 5 min. Wrzuć mięso z powrotem do garnka.",
                   "Knorr Naturalnie smaczne wymieszaj z 500 ml wody, następnie wlej do mięsa z warzywami. Dodaj liście laurowe. Zagotuj, zmniejsz ogień i gotuj pod przykryciem przez około 1,5 h lub do momentu aż mięso zmięknie. Podawaj z kaszą jęczmienną lub kluskami. Udekoruj gęstym jogurtem naturalnym i posiekaną pietruszką."]
    difficulty = Difficulty.HARD
    estimated_time = 90
    related_links = "https://www.przepisy.pl/przepis/wiosenny-gulasz"

    return Recipe(name, ingredients, description,
                  difficulty=difficulty, estimatedTime=estimated_time, relatedLinks=related_links)

@pytest.fixture()
def recipes(recipe_1: Recipe,
            recipe_2: Recipe,
            recipe_3: Recipe,
            recipe_4: Recipe,
            recipe_5: Recipe):
    
    return [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]


def init_test():
    # Get all files and check whether they are read properly
    pass

def init_empty_test():
    pass

def sort_alphabetically_test():
    pass

def sort_ingredients_count_test():
    pass

def sort_difficulty_test():
    pass

def sort_by_estimated_time_test():
    pass

def filter_by_name_phrases_test():
    pass

def filter_ingredients_test():
    pass

def filter_difficulty_test():
    pass

def filter_by_estimated_time_test():
    pass

def add_remove_recipe_test():
    pass

def update_recipe_test():
    pass