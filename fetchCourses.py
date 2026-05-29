import cloudscraper
from bs4 import BeautifulSoup

class CoursesFetcher:

    def __init__(self,url):
        self.url = url

    def fetchCourses(self):
        courses = []

        scraper = cloudscraper.create_scraper(
            browser = {
                "browser" : "chrome",
                "platform" : "linux",
                "mobile" : False
            }
        )

        response = scraper.get(
            self.url,
            timeout = 30
        )

        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(
            html,
            "lxml"
        )
        soupCourses = soup.find_all("span", class_="pgmname")

        # soupCourses = soup.find("a", href="javascript:void(0)")

        for i , course in enumerate(soupCourses):
            courses.insert(i,course.get_text())

        return courses
