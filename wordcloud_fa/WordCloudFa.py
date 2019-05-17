from typing import List, Set, Iterable, Dict
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from wordcloud import WordCloud
from os.path import dirname, join
from os import environ
from hazm import Normalizer
from re import sub

FILE = dirname(__file__)
STOPWORDS = set(map(str.strip, open(join(FILE, 'stopwords')).readlines()))
FONT_PATH = environ.get('FONT_PATH', join(FILE, 'Fonts', 'font.ttf'))


class WordCloudFa(WordCloud):
    """
    This is a wrapper around WordCloud module for working with Farsi and Arabic words plus English words.
    For reading about parameters you can read `WordCloud` documents at:
    https://github.com/amueller/word_cloud/blob/d36f526e3d8346e6d7a2656631f05f68e402517d/wordcloud/wordcloud.py#L150
    There are two additional parameters in this class those are not in the WordCloud published module:
    :param include_numbers if be True, all English, Persian and Arabic numbers will exclude from conting and showing
    :param persian_normalize if be True, all words will normalize using `hazm` normalizer. for more info see:
    https://github.com/sobhe/hazm
    If you don't pass stopwords, default stopwords in the `stopwords` file will consider.
    """
    def __init__(self, font_path=None, width=400, height=200, margin=2,
                 ranks_only=None, prefer_horizontal=.9, mask=None, scale=1,
                 color_func=None, max_words=200, min_font_size=4,
                 stopwords=None, random_state=None, background_color='black',
                 max_font_size=None, font_step=1, mode="RGB",
                 relative_scaling='auto', regexp=None, collocations=True,
                 colormap=None, normalize_plurals=True, contour_width=0,
                 contour_color='black', repeat=False, include_numbers=True, persian_normalize: bool = False):
        """

        :param font_path: Default value is the font file in the `Fonts` directory
        :param mask: an Image as a numpy array. It's better to use a black and white image as `masked-example.py` file.
        :param max_words: Maximum number of words considered. If you want to consider all of your words, it should be
                          equal or greater than number of unique words in your data
        :param stopwords: An Iterable contains words you don't want to consider. If be None, default stopwords will
                          consider. You should add values to default words using `add_stop_words` method.
        :param include_numbers: if be True, all English, Persian and Arabic numbers will exclude from conting and showing
        """
        super().__init__(font_path, width, height, margin,
                         ranks_only, prefer_horizontal, mask, scale,
                         color_func, max_words, min_font_size,
                         stopwords, random_state, background_color,
                         max_font_size, font_step, mode,
                         relative_scaling, regexp, collocations,
                         colormap, normalize_plurals, contour_width,
                         contour_color, repeat)
        self.font_path = font_path if font_path is not None else FONT_PATH
        self.stopwords = stopwords if stopwords is not None else STOPWORDS
        self.persian_normalize: bool = persian_normalize
        self.include_numbers = include_numbers

    @staticmethod
    def reshape_words(words: Iterable) -> List[str]:
        """
        This method make words proper for displaying in the wordcloud.
        We first join all words together as a string, then reshape them and finally split them, because it's faster than
        reshaping each word separately.
        ATTENTION: words should not contain \n because this character used as separator. so if a word has `\n` character
        in it, considers as two separate words.
        :param words: an iterable including words
        :return: a ist of proper words for showing in the WordCloud
        """
        combined_words = "".join(x + "\n" for x in words)
        return get_display(arabic_reshaper.reshape(combined_words)).split("\n")

    def add_stop_words(self, stop_words: Iterable) -> None:
        """
        Adds new stopwords to the default STOPWORDS set. You should not use strings or output of the `reshape_words`.
        :param stop_words:
        :return:
        """
        for stop_word in stop_words:
            self.stopwords.add(stop_word)

    def process_text(self, text):
        """
        If `persian_normalize` attribute has been set to True, normalizes `text` with Hazm Normalizer.
        If `include_numbers` attribute has been set to False, removes all Persian, English and Arabic numbers from
        text`.
        At the end returns result of `WordCloud.process_text` method.
        :param text: str
        :return:
        """
        if self.persian_normalize:
            normalizer = Normalizer()
            text = normalizer.normalize(text)
        if not self.include_numbers:
            text = sub(r"[0-9\u06F0-\u06F9\u0660-\u0669]", "", text)
        return super().process_text(text)

    def generate_from_frequencies(self, frequencies: Dict[str, float], max_font_size=None):
        """
        Removes words those are in `stopwords` attribute. then reshape remaining words for make them proper for
        displaying as a wordcloud.
        Attention: Behaviour of this method is diferrent from `WrodCloud.generate_from_frequencies` because that will not
        exclude the stopwords when you are using this method. But in this class, we exclude stopwords.
        :param frequencies: a dictionary like: {'word1': 11, 'word2': 1}
        :param max_font_size: same as WordCloud
        :return:
        """
        words: List[str] = list(frequencies.keys())
        values: List[float] = list(frequencies.values())
        stopwords: Set[str] = set([i.lower() for i in self.stopwords])
        combined_words = "".join(x + "\n" for x in words if x not in stopwords)
        if self.persian_normalize:
            normalizer = Normalizer()
            combined_words = normalizer.normalize(combined_words)
        reshaped_words: List[str] = get_display(arabic_reshaper.reshape(combined_words)).split("\n")
        new_frequencies = dict(zip(reshaped_words, values))
        return super().generate_from_frequencies(new_frequencies, max_font_size)

    def generate(self, text):
        """
        Generates wordcloud from a text. It is a wrapper for `generate_from_text` method.
        :param text:
        :return:
        """
        return self.generate_from_text(text)

    def to_html(self):
        """
        Left unimplemented same as WordCloud module.
        :return:
        """
        pass

