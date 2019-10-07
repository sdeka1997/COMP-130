"""
This program allows the world's museums and art collectors to each maintain 
their own database of their collections. Its simple, standard interface will
allow anyone to use the database for personal inquiry.
"""
def empty_db():
    """
    Returns an empty dictionary.
    """
    return {}

def add_item(database, artist, artwork, year, description, owner):
    """
    This function mutates the database to add one piece of artwork.
    """
    if database.has_key(artist) == True:
        info = database[artist]
        if info.has_key(artwork) == True:
            return False
        else:
            info[artwork] = (year, description, owner)
    else:
        info = {}
        database[artist] = {artwork : (year, description, owner)}
    return True

def change_owner(database, artist, artwork, new_owner):
    """
    This function mutates the database to change the owner of an 
    indicated artwork by an indicated artist. 
    """
    if database.has_key(artist) == True:
        info = database[artist]
        if info.has_key(artwork) == True:
            infolist = list(info[artwork])
            infolist.pop(-1)
            infolist.append(new_owner)
            infotuple = tuple(infolist)
            info[artwork] = infotuple
            return True
    return False    
    
def select_artist(database, artist):
    """
    Returns a new database with all of the information for 
    the given artist in the given database.
    """
    if database.has_key(artist) == True:
        return {artist: database[artist]}
    else:
        return {}

def select_artwork(database, artwork):
    """
    Returns a new database with all of the information for 
    the given artwork in the given database.
    """
    data = {}
    for artist in database.keys():
        info = database[artist]
        if info.has_key(artwork) == True:
            if artist not in data.keys():
                data[artist] = {}
            data[artist][artwork] = info[artwork]
    return data

def select_year(database, year):
    """
    Returns a new database with all of the information for 
    any artwork from the given year in the given database.
    """
    data = {}
    for artist in database.keys():
        info = database[artist]
        for artwork in info.keys():
            tupledata = info[artwork]
            if year == tupledata[0]:
                if artist not in data.keys():
                    data[artist] = {}
                data[artist][artwork] = tupledata
    return data

def select_description(database, keyword):
    """
    Returns a new database with all of the information for 
    any artwork from the given year in the given database.
    """
    data = {}
    for artist in database.keys():
        info = database[artist]
        for artwork in info.keys():
            tupledata = info[artwork]
            if keyword in tupledata[1]:
                if artist not in data.keys():
                    data[artist] = {}
                data[artist][artwork] = tupledata
    return data

def select_owner(database, owner):
    """
    Returns a new database with all of the information for 
    any artwork from the given year in the given database.
    """
    data = {}
    for artist in database.keys():
        info = database[artist]
        for artwork in info.keys():
            tupledata = info[artwork]
            if owner in tupledata[2]:
                if artist not in data.keys():
                    data[artist] = {}
                data[artist][artwork] = tupledata
    return data

def format_results(database):
    """
    Returns a string with one line per artwork. For each 
    artwork, it lists the artist, artwork, year, description, 
    and owner, each separated by a comma and a space.
    """
    datalist = ''
    for artist in database.keys():
        for artwork in database[artist]:
            year, keyword, owner = database[artist][artwork]
            datalist += str(artist) + ", " + str(artwork) + ", " + str(year) + ", " + str(keyword) + ", " + str(owner) + "\n"
    return datalist