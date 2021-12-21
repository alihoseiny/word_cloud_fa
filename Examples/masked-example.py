from wordcloud_fa import WordCloudFa
import numpy as np
from PIL import Image

mask = np.array(Image.open("mask.png"))

# Passing `no_reshape` parameter for you may cause problem in showing Farsi texts. If your output from the example
# is not true, you can remove that parameter
wodcloud = WordCloudFa(persian_normalize=True, include_numbers=False, background_color="white", mask=mask, no_reshape=True)

# Adding extra stop words:
wodcloud.add_stop_words(['the', 'and', 'with', 'by', 'in', 'to', 'to the', 'of', 'it', 'is', 'th', 'its', 'for', '[ ]', '. [', '] ['])

text = ""
with open('mixed-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('masked-example.png')