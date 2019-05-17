from WordCloudFa import WordCloudFa

wodcloud = WordCloudFa(persian_normalize=True, include_numbers=False, background_color="white")
text = ""
with open('mixed-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('mixed-example.png')