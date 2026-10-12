from prettytable import PrettyTable


# Create an object
pokemon_table = PrettyTable()

# Access its methods and set the parameters of the arguments
pokemon_table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"], align="l")
pokemon_table.add_column("Type", ["Electric", "Water", "Fire"], align="l")

print(pokemon_table)

# Access its attributes
pokemon_table.border = False
print(type(pokemon_table.border))
print(pokemon_table)
