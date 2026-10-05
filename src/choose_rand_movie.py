import random
movies = {
    "Alien 3": "sci-fi", 
    "Renfield": "vampire",
    "Pacific Rim": "scifi",
    "The Sword and the Sorcerror": "80s adventure",
    "Mad God": "scifi",
    "Spawn": "super hero",
}
movie = random.choice(list(movies.keys() ))
print(f"Title: {movie}")
print(f"Genre: {movies[movie]}")

