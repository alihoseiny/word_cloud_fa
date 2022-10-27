from wordcloud_fa import WordCloudFa

wodcloud = WordCloudFa(persian_normalize=True, include_numbers=False, background_color="white", stopwords={'[', ']', '[]', '] [', '[ ]', '] .', ')', '('}, no_reshape=True)

with open('mixed-example.txt', 'r') as file:
    text = file.read()

wc = wodcloud.generate(text)
print(wc.process_text(text))
image = wc.to_image()
image.show()
image.save('mixed-example.png')
