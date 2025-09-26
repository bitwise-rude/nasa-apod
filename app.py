import os # only for accessing API key
from dotenv import load_dotenv # Only for acessing API key
import requests
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.text import Text

# Loading the API key, you can paste the key here
load_dotenv()
api_key = os.getenv("API_KEY")

# some contants
width = 80
console = Console()


# requesting NASA
url = "https://api.nasa.gov/planetary/apod"
params = {
    'count':1,
    'api_key':api_key
}
response_as_json= requests.get("https://api.nasa.gov/planetary/apod", params=params).json()

# data retrieved
date = response_as_json[0]['date']
title = response_as_json[0]['title']
url = response_as_json[0]['url']

# image data
img_bytes = requests.get(url).content
img = Image.open(BytesIO(img_bytes))

height = int((img.height / img.width) * width * 0.5)  # preserve aspect ratio
img = img.resize((width, height))
img = img.convert("L") # graysacling

# converting to ascii art
chars = "@%#*+=-:. "
pixels = img.getdata()
ascii_str = "".join(chars[pixel // 25] for pixel in pixels)

# displaying the ascii art
for i in range(0, len(ascii_str), width):
    print(ascii_str[i:i+width])
