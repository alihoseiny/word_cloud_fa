from WordCloudFa import WordCloudFa
import numpy as np
from PIL import Image

mask = np.array(Image.open("mask.png"))
wodcloud = WordCloudFa(persian_normalize=True, include_numbers=False, background_color="white", mask=mask)
wodcloud.add_stop_words(['the', 'and', 'with', 'by', 'in', 'to', 'to the', 'of', 'it', 'is', 'th', 'its', 'for'])
text = ""
with open('mixed-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('masked-example.png')