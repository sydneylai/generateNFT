from os import path, mkdir
from PIL import Image
output_folder = "generated"
if not path.exists(output_folder):
    mkdir(output_folder)
def generate_image(background, character, object, file_name):
  background_file = path.join("backgrounds", f"{background}.png")
  background_image = Image.open(background_file)
  #Create character
  character_file = path.join("characters", f"{character}.png")
  character_image = Image.open(character_file)
  coordinates = (int(1920/2-character_image.width/2), int(1000-character_image.height)) #x, y
  background_image.paste(character_image, coordinates, mask=character_image)
  #Create object
  if object != "none":
    object_file = path.join("objects", f"{object}.png")
    object_image = Image.open(object_file)
    coordinates = (int(1920/2+character_image.width/2+30), int(1000-object_image.height)) #x, y
    background_image.paste(object_image, coordinates, mask=object_image)
    output_file = path.join(output_folder, f"{file_name}.png")
    background_image.save(output_file)
for background in ["background1", "background2", "background3"]:
    for character in ["elf1", "elf2", "elf3"]:
        for object in ["object1", "object2", "object3"]:
            generate_image(background, character, object, file_name=f"{background}{character}{object}")
