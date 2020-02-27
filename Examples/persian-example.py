from wordcloud_fa import WordCloudFa

wodcloud = WordCloudFa(no_reshape=True, persian_normalize=True, include_numbers=False, collocations=False, width=800, height=400)
text = ""
with open('persian-example.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('persian-example.png')
