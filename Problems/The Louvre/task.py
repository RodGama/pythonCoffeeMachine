class Painting:

    def __init__(self, title, painter, year):
        self.painter = painter
        self.title = title
        self.year = year


title = str(input())
name = str(input())
year = int(input())
paint = Painting(title, name, year)
print(f"\"{title}\" by {name} ({year}) hangs in the Louvre.")
