import os
import requests
import shutil
import fileinput
import json
import subprocess
from PIL import Image

def download_file(url, folder_path):
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Get the filename from the URL
    filename = url.split("/")[-1]

    # Download the file
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

# Get the folder name from user input
folder_name = input("Enter the Pokemon name: ")

# Create the folder in the "expansion" folder
expansion_folder = os.path.join(os.getcwd(), "expansion")
folder_path = os.path.join(expansion_folder, folder_name)


# Example URL
backsprite    = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/{folder_name}/front.png"
frontsprite   = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/{folder_name}/back.png"
icon          = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/{folder_name}/icon.png"
normalpalette = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/{folder_name}/normal.pal"
shinypalette  = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/{folder_name}/shiny.pal"
footprint     = f"https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/upcoming/graphics/pokemon/abomasnow/footprint.png"

# Download the file into the created folder
download_file(backsprite, folder_path)
download_file(frontsprite, folder_path)
download_file(icon, folder_path)
download_file(normalpalette, folder_path)
download_file(shinypalette, folder_path)
download_file(footprint, folder_path)

# Copy the pokemon_data.json file to the "other" folder
source_file = os.path.join(os.getcwd(), "other\pokemon_data.json")
destination_file = os.path.join(folder_path, "pokemon_data.json")
shutil.copy(source_file, destination_file)

# Capitalize the first letter of the folder name
folder_name = folder_name.capitalize()

# Edit line 3 of the pokemon_data.json file with the pokemon name
folder_name_line = f'        "species_name" : "{folder_name}",'
with fileinput.FileInput(destination_file, inplace=True) as file:
    for line in file:
        if file.lineno() == 3:
            print(folder_name_line)
        else:
            print(line, end='')

# Open the downloaded PNG file
image_path = os.path.join(folder_path, "icon.png")
image = Image.open(image_path)

# Get the palette from the image
palette = image.getpalette()

# Convert the palette to JASC-PAL format
jasc_palette = "JASC-PAL\n0100\n"
jasc_palette += f"{len(palette)//3}\n"
for i in range(0, len(palette), 3):
    r, g, b = palette[i:i+3]
    jasc_palette += f"{r} {g} {b}\n"

# Save the JASC-PAL palette to a file
palette_file_path = os.path.join(folder_path, "icon.pal")
with open(palette_file_path, "w") as palette_file:
    palette_file.write(jasc_palette)

# Close the image
image.close()

# Read the contents of the icon.pal file
palette_file_path = os.path.join(folder_path, "icon.pal")
with open(palette_file_path, "r") as palette_file:
    palette_lines = palette_file.readlines()

# Get the third line and remove leading/trailing whitespace
third_line = palette_lines[3].strip()

# Change the Icon Palette Number
if third_line == "131 131 115":
    # Read the contents of the pokemon_data.json file
    pokemon_data_path = os.path.join(folder_path, "pokemon_data.json")
    with open(pokemon_data_path, "r") as pokemon_data_file:
        lines = pokemon_data_file.readlines()

    # Find the line number for "icon_pal_num"
    icon_pal_num_line = next((i for i, line in enumerate(lines) if '"icon_pal_num"' in line), None)

    if icon_pal_num_line is not None:
        # Update the value of "icon_pal_num" to "0"
        lines[icon_pal_num_line] = '    "icon_pal_num": 0,\n'

        # Write the updated lines back to the pokemon_data.json file
        with open(pokemon_data_path, "w") as pokemon_data_file:
            pokemon_data_file.writelines(lines)

if third_line == "115 115 115":
    # Read the contents of the pokemon_data.json file
    pokemon_data_path = os.path.join(folder_path, "pokemon_data.json")
    with open(pokemon_data_path, "r") as pokemon_data_file:
        lines = pokemon_data_file.readlines()

    # Find the line number for "icon_pal_num"
    icon_pal_num_line = next((i for i, line in enumerate(lines) if '"icon_pal_num"' in line), None)

    if icon_pal_num_line is not None:
        # Update the value of "icon_pal_num" to "1"
        lines[icon_pal_num_line] = '    "icon_pal_num": 1,\n'

        # Write the updated lines back to the pokemon_data.json file
        with open(pokemon_data_path, "w") as pokemon_data_file:
            pokemon_data_file.writelines(lines)

if third_line == "98 156 131":
    # Read the contents of the pokemon_data.json file
    pokemon_data_path = os.path.join(folder_path, "pokemon_data.json")
    with open(pokemon_data_path, "r") as pokemon_data_file:
        lines = pokemon_data_file.readlines()

    # Find the line number for "icon_pal_num"
    icon_pal_num_line = next((i for i, line in enumerate(lines) if '"icon_pal_num"' in line), None)

    if icon_pal_num_line is not None:
        # Update the value of "icon_pal_num" to "2"
        lines[icon_pal_num_line] = '    "icon_pal_num": 2,\n'

        # Write the updated lines back to the pokemon_data.json file
        with open(pokemon_data_path, "w") as pokemon_data_file:
            pokemon_data_file.writelines(lines)

# Function to change line endings of a file
def change_line_endings(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    # Replace LF line endings with CR LF line endings
    content = content.replace(b"\n", b"\r\n")

    with open(file_path, "wb") as file:
        file.write(content)

# Change line endings of normal.pal
normal_palette_path = os.path.join(folder_path, "normal.pal")
change_line_endings(normal_palette_path)

# Change line endings of shiny.pal
shiny_palette_path = os.path.join(folder_path, "shiny.pal")
change_line_endings(shiny_palette_path)

# Make a GET request to the PokéAPI
folder_name = folder_name.lower()

# Make a GET request to the PokéAPI
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{folder_name}")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the Pokémon types from the response JSON
    pokemon_data = response.json()
    pokemon_types = [type_data["type"]["name"] for type_data in pokemon_data["types"]]

    # Read the contents of the pokemon_data.json file
    pokemon_data_path = os.path.join(folder_path, "pokemon_data.json")
    with open(pokemon_data_path, "r") as pokemon_data_file:
        lines = pokemon_data_file.readlines()

    # Find the line number for the "types" section
    types_line = next((i for i, line in enumerate(lines) if '"types"' in line), None)

    if types_line is not None:
        # Update the type lines in the lines list
        for i, pokemon_type in enumerate(pokemon_types):
            type_line = next((j for j, line in enumerate(lines[types_line:]) if f'"type{i+1}"' in line), None)
            if type_line is not None:
                type_line += types_line
                lines[type_line] = '            "type{}" : "TYPE_{}",\n'.format(i+1, pokemon_type.upper())
            else:
                print(f"Failed to find the line number for 'type{i+1}' line")

        # Write the updated lines back to the pokemon_data.json file
        with open(pokemon_data_path, "w") as pokemon_data_file:
            pokemon_data_file.writelines(lines)

        print(f"The Pokémon types for {folder_name} are: {', '.join(pokemon_types)}")
    else:
        print("Failed to find the line number for the 'types' section")
else:
    print("Failed to retrieve Pokémon information from the API")

if response.status_code == 200:
    # Extract the Pokémon base stats from the response JSON
    pokemon_data = response.json()
    base_stats = pokemon_data["stats"]

    # Read the contents of the pokemon_data.json file
    pokemon_data_path = os.path.join(folder_path, "pokemon_data.json")
    with open(pokemon_data_path, "r") as pokemon_data_file:
        data = pokemon_data_file.read()

    # Update the base stats in the data string
    for stat_data in base_stats:
        stat_name = stat_data["stat"]["name"]
        stat_value = stat_data["base_stat"]
        # Use the provided stat names instead of the ones from the PokéAPI
        if stat_name == "hp":
            data = data.replace('"baseHP"        : 100', f'"baseHP" : {stat_value}')
        elif stat_name == "attack":
            data = data.replace('"baseAttack"    : 100', f'"baseAttack" : {stat_value}')
        elif stat_name == "defense":
            data = data.replace('"baseDefense"   : 100', f'"baseDefense" : {stat_value}')
        elif stat_name == "special-attack":
            data = data.replace('"baseSpAttack"  : 100', f'"baseSpAttack" : {stat_value}')
        elif stat_name == "special-defense":
            data = data.replace('"baseSpDefense" : 100', f'"baseSpDefense" : {stat_value}')
        elif stat_name == "speed":
            data = data.replace('"baseSpeed"     : 100', f'"baseSpeed" : {stat_value}')

    # Write the updated data back to the pokemon_data.json file
    with open(pokemon_data_path, "w") as pokemon_data_file:
        pokemon_data_file.write(data)

    print(f"The base stats for {folder_name} have been updated.")
else:
    print("Failed to retrieve Pokémon information from the API")