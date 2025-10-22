# The CLASS (blueprint) for a playlist
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = [] # State: a list to hold songs

    # Behavior: Method to add a song
    def add_song(self, song_title):
        self.songs.append(song_title)
        print(f"Added '{song_title}' to the '{self.name}' playlist.")

    # Behavior: Method to remove a song
    def remove_song(self, song_title):
        if song_title in self.songs:
            self.songs.remove(song_title)
            print(f"Removed '{song_title}' from the playlist.")
        else:
            print(f"'{song_title}' is not in the playlist.")

    # Behavior: Method to display the playlist
    def display_playlist(self):
        print(f"\n--- Playlist: {self.name} ---")
        if not self.songs:
            print("The playlist is empty.")
        else:
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")


# --- Instantiation: Creating a single OBJECT ---
my_playlist = Playlist("My Road Trip Hits")

# --- Interacting with the object's methods to change its state ---
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Hotel California")
my_playlist.add_song("Stairway to Heaven")

my_playlist.display_playlist()

my_playlist.remove_song("Hotel California")

my_playlist.display_playlist()