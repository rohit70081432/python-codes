import abc
from abc import ABC, abstractmethod

class MovieCategory(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def categorize(self):
        pass

    def display_title(self):
        print(f"Movie Title: {self.title}")

class HorrorMovie(MovieCategory):
    def categorize(self):
        return f"The movie  is a historic movie."

class ActionMovie(MovieCategory):
    def categorize(self):
      return f"The movie  is an Action movie."

movie1 = HorrorMovie("KANTARA THE LEGEND")
movie2 = ActionMovie("SALAAR PART 1")

movie1.display_title()
print(movie1.categorize())

movie2.display_title()
print(movie2.categorize())