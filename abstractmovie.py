import abc
from abc import ABC, abstractmethod

class MovieCategory(ABC):
    """
    An Abstract Base Class (ABC) for movie categorization.
    It requires all concrete subclasses to implement the categorize method.
    """

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def categorize(self):
        """
        Abstract method that MUST be implemented by any concrete subclass.
        This method will return the specific category of the movie.
        """
        pass

    def display_title(self):
        """
        A regular concrete method that can be used by all subclasses.
        """
        print(f"Movie Title: {self.title}")

class HorrorMovie(MovieCategory):
    """
    A concrete implementation for the Horror movie category.
    It MUST provide an implementation for the abstract 'categorize' method.
    """
    def categorize(self):
        return f"The movie '{self.title}' is categorized as HORROR."
    
class ActionMovie(MovieCategory):
    """
    A concrete implementation for the Action movie category.
    It MUST provide an implementation for the abstract 'categorize' method.
    """
    def categorize(self):
        return f"The movie '{self.title}' is categorized as ACTION/ADVENTURE."

movie1 = HorrorMovie("The Silent House")
movie2 = ActionMovie("Explosion 7")

movie1.display_title()
print(movie1.categorize())

print("-" * 20)

movie2.display_title()
print(movie2.categorize())
