class Car:
    def __init__(self, model, year, color, price, body, interior):
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.body = body
        self.interior = interior

    def start_engine(self):
        print(self.model + " engine started")

    def show_year(self):
        print(self.year)

    def show_color(self):
        print(self.color)

    def show_price(self):
        print(self.price)

    def show_body(self):
        print(self.body)

    def check_interior(self):
        if "leather" in self.interior:
            print(self.model + " only has 2 seats")


Car1 = Car("Lambo", 2027, "Light Blue", 600000, "wide", "red leather")
Car2 = Car("Bugatti Mistral", 2029, "Neon Blue", 2000000, "wide", "black leather")

Car1.start_engine()
Car1.show_year()
Car1.show_color()
Car1.show_price()
Car1.show_body()
Car1.check_interior()

Car2.start_engine()
Car2.show_year()
Car2.check_interior()