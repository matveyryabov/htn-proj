from google.cloud import vision
import io
from PIL import Image
import os #should be removed in final version

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="hackthenorth-be7580cfcf6a.json"

client = vision.ImageAnnotatorClient()

def CropAndRead(path, high_lights):
    """
    This function takes in a list of lists of highlighted points.
    Every one of these lists represents one thing that the user decided
    to highligh. This function will create a new cropped image to just
    contain what the user highlihgted, send that to the google cloud API
    and recieve the text in the cropped section and process it to
    return a meaningful output in a dictionary.

	path is the path to the downloaded image

	high_lights is a dictionary, containing keys that are the thing that will be 
	highlighted,v(like price) and values as a list of all points highlihgted by 
	the user for that particular entry.
    """
    output = dict()

    original_image = Image.open(path)

    for key in high_lights:
    	y_coords = []
    	x_coords = []

    	for point in high_lights[key]:
    		x_coords.append(point[0])
    		y_coords.append(point[1])

    	x_min = min(x_coords)
    	x_max = max(x_coords) + 1 ##+ 1 to make for looping easier later
    	y_min = min(y_coords)
    	y_max = max(y_coords) + 1

    	temp_Image = Image.new("RGB",(x_max-x_min,y_max-y_min),(0,0,0))

    	for x in range(x_min,x_max):
    		for y in range(y_min,y_max):
    			temp_Image.putpixel((x - x_min,y - y_min),original_image.getpixel((x,y)))

    	temp_Image.save("temp.png")

    	response = client.text_detection(image=vision.Image(content=(io.open("temp.png", 'rb').read())))

    	output[key] = response.text_annotations

    os.remove("temp.png")
    return(output)

"""
TEST:
thing =  CropAndRead("test.png",{
	       "price": [(0,0),(690,420)],
           "name": [(0,0),(350,220)]
	       })

for x in thing:
    print(thing[x][0].description)
"""