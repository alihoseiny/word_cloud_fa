# WordCloudFa
[![Downloads](https://pepy.tech/badge/wordcloud-fa)](https://pepy.tech/project/wordcloud-fa)
![](https://img.shields.io/pypi/v/wordcloud-fa.svg?style=popout)


![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/masked-example.png)


This module is an easy-to-use wrapper for [word_cloud module](https://github.com/amueller/word_cloud).

**Attention: It seems that you can use the original module now for creating wordclouds for Farsi with proper fonts.
 So you can use that module instead this one. But this module is steal useful if you are interested in its other features.
 If you found problems in original module for creating Farsi modules, please notify me at the issues page for removing this warning.**

The original module doesn't support Farsi Texts. But by using **WordCloudFa** you can generate word clouds from 
texts those are including Persian and English words.

This module is not only a wrapper, but it adds some features to the original module.

<!-- toc -->

- [How to Install](#how-to-install)
- [How to Use](#how-to-use)
  * [Generating Word Cloud from Text](#generating-word-cloud-from-text)
  * [Generating Word Cloud from Frequencies](#generating-word-cloud-from-frequencies)
  * [Working with Stopwords](#working-with-stopwords)
  * [Mask Image](#mask-image)
  * [Reshaping words](#reshaping-words)
- [Examples](#examples)
- [Font](#font)
- [Persian Tutorial](#persian-tutorial)
- [Contribution](#contribution)
- [There is any problem?](#there-is-any-problem)
- [Citations](#citations)

<!-- tocstop -->

# How to Install
For installing this module, you can simply run 

`pip install wordcloud-fa`.

This module tested on `python 3`

*WordCloudFa* depends on `numpy` and `pillow`.

Also you should have `Hazm` module. Normally, all of them will install automatically when you install this module using 
`pip` as described at the beginning of this section.  

To save the wordcloud into a file, `matplotlib` can also be installed.

**Attention**

You need to have `python-dev` for python3 on your system. If you don't have it, you can install it on operating systems 
those using `apt` as the package manager (Like Ubuntu) by this command:

`sudo apt-get install python3-dev`

And you can install it on operating systems those using `yum` as the package manager (like RedHat, Fedora and ...) you can 
use the following command:

`sudo yum install python3-devel` 

# How to Use
For creating a word cloud from a text, first you should import the class into your code:

`from wordcloud_fa import WordCloudFa`

you can create an instance of this class like:

`wodcloud = WordCloudFa()`

You can pass different parameters to the constructor. For see full documents of them, you can see 
[WordCloud Documentations](https://amueller.github.io/word_cloud/) 

There are two parameters that are not in the original class.

First one is `persian_normalize`. If you pass this parameter with `True` value, your data will normalize by using 
[Hazm normalizer](https://github.com/sobhe/hazm). It's recommended to always pass this parameter. That will replace 
arabic letters with persian ones and do some other stuff.
The default value of this parameter is `False`.

`wodcloud = WordCloudFa(persian_normalize=True)`  

the second parameter is `include_numbers` that is not in the published original module. If you set this parameter to `False`,
 all Persian, Arabic and English numbers will remove from your data.
 
 The default value of this parameter is `True`
 
 `wodcloud = WordCloudFa(include_numbers=False)`
 
 ## Generating Word Cloud from Text
 for generating word cloud from a string, you can simply call `generate` method of you instance:
 
 ```python
wodcloud = WordCloudFa(persian_normalize=True)
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('wordcloud.png')

``` 

## Generating Word Cloud from Frequencies

You can generate a word cloud from frequencies. You can use the output of `process_text` method as frequencies.
 Also you can use any dictionary like this.
 
 ```python
wodcloud = WordCloudFa()
frequencies = wodcloud.process_text(text)
wc = wodcloud.generate_from_frequencies(frequencies)
``` 

`generate_from_frequencies` method in this module will exclude stopwords. But the original module will not exclude them 
when you are using this method. Also you can use Persian words as keys in frequencies dict without any problem.

## Working with Stopwords

Stopwords are the words that we don't want to consider. If you dan't pass any stopword, the default words in the 
[stopwords](https://github.com/alihoseiny/word_cloud_fa/blob/master/wordcloud_fa/stopwords) file will consider as 
stopwords.

You don't want to use them at all and you want to choose your stopwords? you can simply set `stopwords` parameter when 
you are creating an instance from `WordCloudFa` and pass a `set` of words into it.

```python
stop_words = set(['کلمه‌ی اول', 'کلمه‌ی دوم'])
wc = WordCloudFa(stopwords=stop_words)
``` 

If you want to add additional words to the default stopwords, you can simply call `add_stop_words` method on your 
instance of `WordCloudFa` and pass an iterable type (`list`, `set`, ...) into it.

```python
wc = WordCloudFa()
wc.add_stop_words(['کلمه‌ی اول', 'کلمه‌ی دوم'])
``` 

Also you can add stopwords from a file. That file should include stopwords and each word should be in a separate line.

For that, you should use `add_stop_words_from_file` method. The only parameter of this 

method is relative or absolute path to the stop words file.

```python
wc = WordCloudFa()
wc.add_stop_words_from_file("stopwords.txt")
```

## Mask Image

You can mask the final word cloud by an image. For example, the first image of this document is a wordcloud masked by an image 
of the map of Iran country. For setting a mask, you should pass the `mask` parameter.

But before, you first should be sure you have a black and white image. Because other images will not create a good result.

Then, you should convert that image to a numpy array. For that, you should do something like this:

```python
import numpy as np
from PIL import Image

mask_array = np.array(Image.open("mask.png"))

```

You just should add those two imports, but you don't need to be worried about installing them, because those have been 
installed as dependencies of this module.

Then, you can pass that array to the constructor of the `WordCloudFa` class for masking the result.

```python
wodcloud = WordCloudFa(mask=mask_array)
```

Now you can use your worldcloud instance as before.

## Reshaping words

When you pass your texts into an instance of this class, all words will reshape for turning to a proper way for showing 
And avoiding the invalid shape of Persian or Arabic words (splitted and inverse letters).

If you want to do the same thing outside of this module, you can call `reshape_words` static method.

```python
reshaped_words = WordCloudFa.reshape_words(['کلمه‌ی اول', 'کلمه‌ی دوم'])
```

this method gets an `Iterable` as input and returns a list of reshaped words.

**DONT FORGET THAT YOU SHOULD NOT PASS RESHAPED WORDS TO THE METHODS OF THIS CLASS AND THIS STATIC METHOD IS ONLY FOR USAGES OUT OF THIS MODULE**

# Examples
You can see [Example codes in the Examples directory](https://github.com/alihoseiny/word_cloud_fa/tree/master/Examples).

![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/english-example.png)
![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/mixed-example.png)
![](https://github.com/alihoseiny/word_cloud_fa/raw/master/Examples/persian-example.png)

# Font
The default font is an unknown! font that supports both Persian and English letters. So you don't need to pass a font for 
getting results. But if you want to change the font you can pass `font_path` parameter.

# Persian Tutorial
If you want to read a brief tutorial about how to use this package in Farsi (Persian), you can 
[click on this link](https://blog.alihoseiny.ir/%da%86%da%af%d9%88%d9%86%d9%87-%d8%a8%d8%a7-%d9%be%d8%a7%db%8c%d8%aa%d9%88%d9%86-%d8%a7%d8%a8%d8%b1-%da%a9%d9%84%d9%85%d8%a7%d8%aa-%d9%81%d8%a7%d8%b1%d8%b3%db%8c-%d8%a8%d8%b3%d8%a7%d8%b2%db%8c%d9%85%d8%9f/?utm_source=github&utm_medium=readme&utm_campaign=wordcloudfa).

# Contribution
We want to keep this library fresh and useful for all Iranian developers. So we need your help for adding new features, fixing bugs and adding more documents.

You are wondering how you can contribute to this project? Here is a list of what you can do:

1. Documents are not enough? You can help us by adding more documents.
2. The current code could be better? You can make this cleaner or faster.
3. Do you think one useful feature missed? You can open an issue and tell us about it.
4. Did you find a good open and free font that supports Farsi and English? You can notify us by a pull request or if opening an issue

# There is any problem?
If you have questions, find some bugs or need some features, you can open an issue and tell us. For some strange reasons this is not possible? so contact me by this email: `salam@alihoseiny.ir`.

# Citations
Texts in the `Example` directory are from [this](https://fa.wikipedia.org/wiki/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86) and 
[this](https://en.wikipedia.org/wiki/Iran) Wikipedia pages.

