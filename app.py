from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album

class Application():
    def __init__(self):
        # Connect to the database

        # My comment:
        # DatabaseConnection is just a name of a class that is using psycopg library
        # Creates an instance of the class DatabaseConnection
        self._connection = DatabaseConnection()
        self._connection.connect()

        # Seed with some seed data

        # My comment:
        # Uses the "seed" method from DatabaseConnection to open, read, and seed the data in the sql file. 
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        user_input = int(input('What would you like to do?\n'
                           '1 - List all albums\n'
                           '2 - List all artists\n'
                           'Enter your choice: '))
        
        if user_input == 1:
            # Retrieve all artists
            # My comment:
            # Create an instance of the class ArtistReposistory 
            # Creates a connection between the Artist Repository Class Object and the database so that the data is accesible.
            # Calls the all method and stores the list of artist data as individual objects from the artist class in a variable
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            # List them out
            for artist in artists:
                print(artist)


            
if __name__ == '__main__':
    app = Application()
    app.run()

'''
album_repository = AlbumRepository(connection)



album = album_repository.find(1)
print(album)

new_album = album_repository.create(Album(None,"Trome Le Monde", 1991, 1))
albums = album_repository.all()
for album in albums:
    print(album)

delete_album = album_repository.delete(13)
albums = album_repository.all()
for album in albums:
    print(album)
'''
    
"""
connection.seed("seeds/book_store.sql")
book_repository = BookRepository(connection)
books = book_repository.all()

for book in books:
    print(book)
"""