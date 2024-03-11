import requests
from bs4 import BeautifulSoup
import time

#add to url to accomodate for equiptment

def scraper(level, style, time, muscles):
    exercise_count = 0
    print("Searching for the perfect exercises!")
    if muscles == "random":
        if style == "random":
            url = "https://bodybuilding.com/exercises/finder/?level="f"{level},beginner"
        else:
            url = "https://bodybuilding.com/exercises/finder/?exercise-type="f"{style}&level="f"{level},beginner"
    else:
        for muscle in muscles:
            if style == "random":
                url = "https://bodybuilding.com/exercises/finder/?exercise-type="f"{level},beginner&muscle="f"{muscle}"
            else:
                url = "https://bodybuilding.com/exercises/finder/?exercise-type="f"{style}&level="f"{level},beginner&muscle="f"{muscle}"

            request = requests.get(url)
            soup = BeautifulSoup(request.content, "html.parser")
            exercises = soup.find_all("div", class_="ExResult-cell ExResult-cell--nameEtc")
            f = open("exercises.txt", "w+")
            for exercise in exercises:
                name = exercise.find("h3", class_="ExHeading ExResult-resultsHeading")
                f.write(name.text.strip() + '\n')
                exercise_count += 1
            f.close()

    print("getting ready to generate now!")
    return exercise_count


