import pandas as pd

pokemons = pd.read_csv('pokemon.csv')
print(pokemons.head())
print(pokemons['weight_kg'])