import json

from fetchUniLinks import LinkFetcher
from fetchDesc import DescFetcher
from fetchCourses import CoursesFetcher

URL = (
    "https://www.topuniversities.com/"
    "universities/"
    "massachusetts-institute-technology-mit"
)

topUniLinks = "https://www.topuniversities.com/world-university-rankings"


def main():

    fetchUniLinks = LinkFetcher(topUniLinks)

    soups = fetchUniLinks.fetch()

    print("*************************")
    print(soups)
    print("*************************")

    for soup in soups:
        fetchUniDesc = DescFetcher(soup)

        descData = fetchUniDesc.fetchDesc()

        fetchUniCourses = CoursesFetcher(soup)

        CoursesData = fetchUniCourses.fetchCourses()
        print("\n")
        print("############### URL ##################")
        print(soup)
        print("\n")
        print("############### Description ##################")
        print(descData)
        print("############### Courses ##################")
        for course in CoursesData:
            print(course)

        




main()
