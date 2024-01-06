from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# Connect to the database

# My comment:
# DatabaseConnection is just a name of a class that is using psycopg library
# Creates an instance of the class DatabaseConnection
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data

# My comment:
# Uses the "seed" method from DatabaseConnection to open, read, and seed the data in the sql file. 
connection.seed("seeds/music_library.sql")

# Retrieve all artists

# My comment:
# Create an instance of the class ArtistReposistory 
# Creates a connection between the Artist Repository Class Object and the database so that the data is accesible.
# Calls the all method and stores the list of artist data as individual objects from the artist class in a variable
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()


# List them out
for artist in artists:
    print(artist)

album_repository = AlbumRepository(connection)

albums = album_repository.all()
for album in albums:
    print(album)

album = album_repository.find(1)
print(album)
"""
connection.seed("seeds/book_store.sql")
book_repository = BookRepository(connection)
books = book_repository.all()

for book in books:
    print(book)
"""