class Movie:
    def __init__(self, title, director, year, rating, genre):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.genre = genre

    def show_title(self):
        print("Title: " + self.title)

    def show_director(self):
        print("Director: " + self.director)

    def show_year(self):
        print("Year: " + str(self.year))

    def show_rating(self):
        print("Rating: " + str(self.rating))

    def show_genre(self):
        print("Genre: " + self.genre)



movie1 = Movie("Minions: The Rise of Gru", "Kyle Balda", 2022, 6.5, "Animation")
movie2 = Movie("Dragon Ball Super: Broly", "Tatsuya Nagamine", 2018, 7.7, "Anime")
movie3 = Movie("Pixels", "Chris Columbus", 2015, 5.6, "Comedy/Sci-Fi")


movie1.show_title()
movie1.show_director()
movie1.show_year()
movie1.show_rating()
movie1.show_genre()


movie2.show_title()
movie2.show_director()
movie2.show_year()
movie2.show_rating()
movie2.show_genre()

movie3.show_title()
movie3.show_director()
movie3.show_year()
movie3.show_rating()
movie3.show_genre()