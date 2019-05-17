# WordCloudFa
![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/masked-example.png)
This module is a easy-to-use wrapper for [word_cloud module](https://github.com/amueller/word_cloud)
Original module don't support Farsi Texts. But by using **WordCloudFa** you can generate word clouds from persian texts
all texts those have Persian and English words.

This module is not just a wrapper and adds some features to the original module.

# How to Install
For installing this module, you can simply run `pip install word-cloud-fa`.

This module tested on `python 3`

*WordCloudFa* depends on `numpy` and `pillow`.

Also you should have `Hazm` module. Normally, all of them will install automatically when you install this module using 
`pip` as described at the beginning of this section.  

To save the wordcloud into a file, `matplotlib` can also be installed.

# How to Use
For creating word cloud of a text, first you should import the class into your code:

`from WordCloudFa import WordCloudFa`

you can create an instance of this class like:

`wodcloud = WordCloudFa()`

You can pass different parameters to to constructor. For see full documents of them, you can see 
[WordCloud Documentations](https://amueller.github.io/word_cloud/) 

There are two parameters those are not in the original class.

First one is `persian_normalize`. If you pass this parameter with `True` value, your data will normalize by using 
[Hazm normalizer](https://github.com/sobhe/hazm). It's recommended to always pass this parameter. That will replace 
arabic letters with persian ones and do some other stuff.
Default value of this parameter is `False`.

`wodcloud = WordCloudFa(persian_normalize=True)`  

second parameter is `include_numbers` that is not in the published original module. If you set this parameter to `False`,
 all Persian, Arabic and English numbers will remove from your data.
 
 Default value of this parameter is `True`
 
 `wodcloud = WordCloudFa(include_numbers=False)`
 
 ## Generating Word Cloud from Text
 for generating word cloud from a string, you can simply call `generate` method of you instance:
 
 ```python
wodcloud = WordCloudFa(persian_normalize=True)wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('wordcloud.png')

``` 

## Generating Word Cloud from Frequencies

You can generate word cloud from frequencies. You can use output of `process_text` method as frequencies.
 Also you can use any dictionary like this.
 
 ```python
wodcloud = WordCloudFa()
frequencies = wodcloud.process_text(text)
wc = wodcloud.generate_from_frequencies(frequencies)
``` 

`generate_from_frequencies` method in this module will exclude stopwords. But original module will not exclude them 
when you are using this method. Also you can use Persian words as keys in frequencies dict without any problem.

# Examples
You can see [Example codes in the Examples directory](https://github.com/alihoseiny/word_cloud_fa/tree/master/Examples).

![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/english-example.png)
![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/mixed-example.png)
![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/persian-example.png)

# Contribution
We want to keep this library fresh and useful for all Iranian developers. So we need your help for adding new features, fixing bugs and adding more documents.

You are wondering how you can contribute in this project? Here is a list of what you can do:

1. Documents are not enough? You can help us by adding more documents.
2. Current code could be better? You can make this cleaner or faster.
3. You think one useful feature missed? You can open an issue and tell us about it.
4. You found a good open and free font that support Farsi and English? You can notify us by a pull request or if opening an issue

# There is any problem?
If you have questions, find some bugs or need some features, you can open an issue and tell us. For some strange reasons this is not possible? so contact me by this email: `salam@alihoseiny.ir`.