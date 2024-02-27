# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# Create a dictionary to hold the actor's names.
actors = {}

# Create a dictionary using the built-in function.
actors = dict()

# A dictionary of an actor.
actors = {"name": "Tom Cruise" }

print(f'{actors["name"] }')

# Add an actor to the dictionary with the key "name"
# and the value "Denzel Washington".
actors['name'] = "Denzel Washington"
print(actors)
print(f'{actors["name"] }')

print(type(actors))
print(type(actors["name"]))
# Print the actors dictionary.


# Print only the actor.


# A list of actors
actors_list = ["Tom Cruise",
    "Angelina Jolie",
    "Kristen Stewart",
    "Denzel Washington"]

print(actors_list)

actors["name"] = actors_list

# Overwrite the value, "Denzel Washington", with the list of actors.


# Print the first actor
print(f'{actors["name"][0]}')
print(type(actors["name"]))
print(type(actors["name"][0]))
# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actress = {"name":"Angelina Jolie", 
           "genre":"Action",
           "nationality":"US"}

print(actress)

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information

another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky",
        "Rocky"]}

print(another_actor["best movies"], another_actor["name"])
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}

print(film['revenues']['United States'])


# ---------------------------------------------------------------
