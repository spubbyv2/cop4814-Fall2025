import main_functions, requests
from dotenv import load_dotenv
import os

load_dotenv()

# NASA's API url
url = "https://api.nasa.gov/planetary/apod?api_key="

# Read your NASA API key
api_key = os.getenv("NASA_KEY")

#Build the final API url
final_url = url + api_key

#Make the API request
response = requests.get(final_url).json()

#Serialize the result to a JSON document
main_functions.save_to_file(response, "response.json")


#What is the type of the object deserialized?

#What are its keys?

#Access some of their values passing their keys