
class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (str): name of songs creator.
        duration (int): The duration of the song in seconds. May be zero.
        """
    def __init__(self, title, artist, duration=0):
        # """Song init method
        # Args:
        #     title (str) :Initialises the 'title' attribute
        #     artist (Artist): At Artist object representing the song's creator.
        #     duration (Optional[int]): Initial value for the 'duration' attribute.
        #         Will default to zero if not specified
        # """
        self.title = title
        self.artist = artist
        self.duration = duration

# #can add a doc string like so
# Song.__init__.__doc__ = """SUCK A DICK"""
# #probably shouldnt provide doc string like that, but illustrates that methods can have attributes.
# #help(Song.__init__)
# #print(Song.__doc__)
# print(Song.__init__.__doc__)
#
# help(Song)

    def get_title(self):
        return self.title

    name = property(get_title)




class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): name of album
        year (int) : The year was released
        artist (str): the name of the artist.
              if not specified the artist will default to an artist with the name
              "Various artists".
        tracks (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to eh albums track list.

    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song(Song): the title of a song to add.
             position (Optional)[int]: If specified the song will be added to that position
                in the track list -inserting it between other songs if necessary.
                Otherwise, song will be added at end of the list

        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)

            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)

class Artist:

    """Basic class to store artist details/

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection,
            it is not an exhaustive list of the artist:s published albums

    Methods:
        add_album: Use to add a new album to the artists albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again( not yet implemented
        """

        self.albums.append(album)




        """the artist class has two data attributes. the string containing the artists name, and the list containing the album objects
        standard way to organise a record collection, with the albums by a particular group stored together.
        compilations albums where the songs are by varuous artists do complicate things.
        major problem with this design currently is that the artist object will have a areference to an album, and an album object
         will have a reference to the artist. This problem is sorted with garbage collection. Python typically has good garbage collection
        circular references like this are best avoided. will use adele as example. pythons pickle module can often cope with this type of nesting.
        in short, everything is referencing everything. and this is computationally heavy.
        """
    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection,
        A new album will be created in the collection if it doesnt already exist

        Args:
            name (str): name of the album
            year (int): year album producef
            title (str): title of the song

        """

        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
        else:
            print("Found album " + name)

        album_found.add_song(title)





def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)
            #print(new_album.__dict__)


    return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the origianl file"""

    with open("checkfile.txt","w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)
                         


#if this is the main program being ran, i.e. not an imported file being ran
if __name__ == '__main__':
    artists = load_data()
    print("there are {} artists".format(len(artists)))

    create_checkfile(artists)

# removing circular references. no need for song class to store an artist object anymore.
# we now have a way to find an artist in the list if we know the artist name, using the find_object function
# in addition, no need for album class to store artist object


#if Artist, Album and Song classes were part of the standard python library, then this example is no different
#to any of the previous code we've written. Although this fle uses Objects, it is not object oriented programming.
#OOP is a diff way of thinking and coding entirely. it uses classes and objects, yes but it also includes important
#concepts such as encapsulation, inheritance, composition and delegation.

# delegation involves passing on responsibility of a task to another object thats better suited to deal with it.
# its closely tied to encapsulation. e.g. we've encapsulated data with classses, but havent encapsulated methods very well.
# encasulating methods means considering questions such as qhich object is best suited to dealing with this task
# or where does responsibility for performing this function belong.
# i.e. if a car breaks down, i will look for someone who encapsulate the knowledge of how to fix it. i.e. the mechanic. who possesses
# the knowledge to fix.

#in load data, it does all the work of parsing the data when it finds a new album. really though,
# the object that knows most about albums, is the artists. and albums know all about songs]
#so should encapsulate the methods for dealing with albums in the artist class and songs in the album class.
#load data can delegate dealing to the appropriate class.





#raw literals
"""
a_string = "this is \nastring split \t\tand tabbed"
print(a_string)

raw_string = r"this is \nastring split \t\tand tabbed"
print(raw_string)

b_string = "this is " + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
"""