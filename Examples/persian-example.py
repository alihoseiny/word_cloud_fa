from WordCloudFa import WordCloudFa

wodcloud = WordCloudFa(persian_normalize=True)
text = ""
with open('persian-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('persian-example.png')