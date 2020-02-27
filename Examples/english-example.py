from wordcloud_fa import WordCloudFa

wodcloud = WordCloudFa(include_numbers=False, regexp=r"\w[\w']+")
text = ""
with open('english-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('english-example.png')
