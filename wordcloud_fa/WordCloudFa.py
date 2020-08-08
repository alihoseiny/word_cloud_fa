from typing import List, Set, Iterable, Dict, Pattern
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from wordcloud import WordCloud, STOPWORDS
from os.path import dirname, join
from os import environ
from hazm import Normalizer, word_tokenize
import re
from sys import version

from wordcloud.tokenization import unigrams_and_bigrams, process_tokens

FILE = dirname(__file__)
STOPWORDS.update(map(str.strip, open(join(FILE, 'stopwords'), encoding="utf8").readlines()))
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

    unhandled_characters_regex: Pattern[str] = re.compile("["
                                                          u"\U0001F600-\U0001F64F"  # emoticons
                                                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                          u"\U00002702-\U000027B0\U000024C2-\U0001F251"
                                                          u"\U0001f926-\U0001f937\U00010000-\U0010ffff"
                                                          u"\u200d\u2640-\u2642\u2600-\u2B55\u23cf"
                                                          u"\u23e9\u231a\u3030\ufe0f\u2069\u2066"
                                                          u"\u200c\u2068\u2067"
                                                          u"]+", flags=re.UNICODE)

    def __init__(self, font_path=None, width=400, height=200, margin=2,
                 ranks_only=None, prefer_horizontal=.9, mask=None, scale=1,
                 color_func=None, max_words=200, min_font_size=4,
                 stopwords=None, random_state=None, background_color='black',
                 max_font_size=None, font_step=1, mode="RGB",
                 relative_scaling='auto', regexp=None, collocations=True,
                 colormap=None, normalize_plurals=True, contour_width=0,
                 contour_color='black', repeat=False, include_numbers=True, persian_normalize: bool = False,
                 no_reshape: bool = False, remove_unhandled_utf_characters: bool = True):
        """

        :param font_path: Default value is the font file in the `Fonts` directory
        :param mask: an Image as a numpy array. It's better to use a black and white image as `masked-example.py` file.
        :param max_words: Maximum number of words considered. If you want to consider all of your words, it should be
                          equal or greater than number of unique words in your data
        :param stopwords: An Iterable contains words you don't want to consider. If be None, default stopwords will
                          consider. You should add values to default words using `add_stop_words` method.
        :param include_numbers: if be True, all English, Persian and Arabic numbers will exclude from conting and showing
        :param no_reshape: if be True, reversing Persian/Arabic words will disable.
        :param remove_unhandled_utf_characters: remove the characters those will create undefined behaviour (emoticons, symbols, pictographs, transport and map symbols, ios flags and ...).
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
        self.stopwords: set = set(stopwords) if stopwords is not None else STOPWORDS
        self.persian_normalize: bool = persian_normalize
        self.include_numbers = include_numbers
        self.no_reshape: bool = no_reshape
        self.remove_unhandled_utf_characters: bool = remove_unhandled_utf_characters

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
        combined_words: str = "".join(x + "\n" for x in words)
        return get_display(arabic_reshaper.reshape(combined_words)).split("\n")

    @staticmethod
    def normalize_words(words: Iterable) -> List[str]:
        """
        This method gets an Iterable containing some Farsi words as elements, normalizes them using Hazm and then
        returns a list of normalized words.
        :param words: an iterable including words
        :return: A list of normalized elements of the `words` iterable.
        """
        combined_words: str = "".join(x + "\n" for x in words)
        normalizer: Normalizer = Normalizer()
        normalized_combined_words: str = normalizer.normalize(combined_words)
        return normalized_combined_words.split("\n")

    def add_stop_words(self, stop_words: Iterable) -> None:
        """
        Adds new stopwords to the default STOPWORDS set. You should not use strings or output of the `reshape_words`.
        :param stop_words:
        :return:
        """
        for stop_word in stop_words:
            self.stopwords.add(stop_word)

    def add_stop_words_from_file(self, file_path: str) -> None:
        """
        Reads all words in the `file_path` and add them to the `stop_words` set.
        You should place each stop word in a separate line in your file without empty line at the end
        (Empty line may cause adding an empty string to the list of stop_words).
        :param file_path: Relative or Absolute path to the file.
        :return:
        """
        with open(file_path, 'r') as file:
            self.add_stop_words([x.strip() for x in file.readlines()])

    def process_text(self, text: str) -> Dict[str, int]:
        """
        Splits a long text into words.
        If `persian_normalize` attribute has been set to True, normalizes `text` with Hazm Normalizer.
        If `include_numbers` attribute has been set to False, removes all Persian, English and Arabic numbers from
        text`.
        Attention: this method will not remove stopwords from the input.
        :param text: The text we want to process
        :return: a dictionary. keys are words and values are the frequencies.
        """
        flags = (re.UNICODE if version < '3' and type(text) is unicode  # noqa: F821
                 else 0)

        if self.remove_unhandled_utf_characters:
            text = WordCloudFa.unhandled_characters_regex.sub(r'', text)

        if self.persian_normalize:
            normalizer = Normalizer()
            text = normalizer.normalize(text)
        if not self.include_numbers:
            text = re.sub(r"[0-9\u06F0-\u06F9\u0660-\u0669]", "", text)

        if self.regexp:
            words = re.findall(self.regexp, text, flags)
        else:
            words = word_tokenize(text)

        if self.collocations:
            # We remove stopwords in the WordCloudFa, so there is no need for passing them in this function.
            word_counts = unigrams_and_bigrams(words, [], self.normalize_plurals, self.collocation_threshold)
        else:
            word_counts, _ = process_tokens(words, self.normalize_plurals)

        return word_counts

    def generate_from_frequencies(self, frequencies: Dict[str, float], max_font_size=None):
        """
        Removes words those are in `stopwords` attribute. then reshape remaining words for make them proper for
        displaying as a wordcloud.
        Attention: Behaviour of this method is different from `WrodCloud.generate_from_frequencies` because that will not
        exclude the stopwords when you are using this method. But in this class, we exclude stopwords.
        Attention: `remove_unhandled_utf_characters` option has no effect on this method and you should handle those characters by yourself.
        :param frequencies: a dictionary like: {'word1': 11, 'word2': 1}
        :param max_font_size: same as WordCloud
        :return:
        """
        words: List[str] = []
        values: List[float] = []

        stopwords: Set[str] = set([i.lower() for i in self.stopwords])

        for word in frequencies.keys():
            if word not in stopwords:
                words.append(word)
                values.append(frequencies.get(word))

        if not self.no_reshape:
            words = WordCloudFa.reshape_words(words)

        if self.persian_normalize:
            words = WordCloudFa.normalize_words(words)

        new_frequencies = dict(zip(words, values))
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

