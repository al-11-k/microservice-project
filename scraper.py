import requests
from bs4 import BeautifulSoup
import time


def network_error(muscle_num):
    """Populates the exercise file with saved exercises from cache if network is down"""
    print("Network error. Workout will be generated from cache.")
    if muscle_num == "1":
        source = open("upper_body_cache.txt", "r")
        dest = open("exercises.txt", "w+")
        for line in source:
            dest.write(line)
        source.close()
        dest.close()
        return

    if muscle_num == "2":
        source = open("lower_body_cache.txt", "r")
        dest = open("exercises.txt", "w+")
        for line in source:
            dest.write(line)
        source.close()
        dest.close()
        return

    else:
        source = open("full_body_cache.txt", "r")
        dest = open("exercises.txt", "w+")
        for line in source:
            dest.write(line)
        source.close()
        dest.close()
        return


def create_url(style, muscles):
    """Creates the url to request based on the user parameters"""
    if muscles == "random":
        if style == "random":
            url = "https://bodybuilding.com/exercises/finder/?"
        else:
            url = "https://bodybuilding.com/exercises/finder/?exercise-type="f"{style}"
    else:
        for muscle in muscles:
            if style == "random":
                url = "https://bodybuilding.com/exercises/finder/?muscle="f"{muscle}"
            else:
                url = "https://bodybuilding.com/exercises/finder/?exercise-type="f"{style}&muscle="f"{muscle}"
    return url


def scraper(style, muscles, muscle_num):
    """Scrapes bodybuilding.com for exercises"""
    print("Searching for the perfect exercises!")
    url = create_url(style, muscles)

    request = requests.get(url)
    if request.status_code == 503 or request.status_code == 404:
        network_error(muscle_num)

    else:
        soup = BeautifulSoup(request.content, "html.parser")
        exercises = soup.find_all("div", class_="ExResult-cell ExResult-cell--nameEtc")
        f = open("exercises.txt", "w+")
        for exercise in exercises:
            name = exercise.find("h3", class_="ExHeading ExResult-resultsHeading")
            f.write(name.text.strip() + '\n')
        f.close()

    print("getting ready to generate now!")

