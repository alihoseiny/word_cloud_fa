from typing import List, Set, Iterable
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
    def __init__(self, font_path=None, width=400, height=200, margin=2,
                 ranks_only=None, prefer_horizontal=.9, mask=None, scale=1,
                 color_func=None, max_words=200, min_font_size=4,
                 stopwords=None, random_state=None, background_color='black',
                 max_font_size=None, font_step=1, mode="RGB",
                 relative_scaling='auto', regexp=None, collocations=True,
                 colormap=None, normalize_plurals=True, contour_width=0,
                 contour_color='black', repeat=False, include_numbers=False, persian_normalize: bool = False):
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
        We first join all words together as a string, then reshape them and finally split them, because it's faster than
        reshaping each word separately.
        :param words:
        :return:
        """
        combined_words = "".join(x + "\n" for x in words)
        return get_display(arabic_reshaper.reshape(combined_words)).split("\n")[1:]

    def add_stop_words(self, stop_words: Iterable) -> None:
        for stop_word in stop_words:
            self.stopwords.add(stop_word)

    def process_text(self, text):
        if self.persian_normalize:
            normalizer = Normalizer()
            text = normalizer.normalize(text)
        if not self.include_numbers:
            text = sub(r"[0-9\u06F0-\u06F9\u0660-\u0669]", "", text)
        return super().process_text(text)

    def generate_from_frequencies(self, frequencies, max_font_size=None):
        words: List[str] = list(frequencies.keys())
        values: List[float] = list(frequencies.values())
        stopwords: Set[str] = set([i.lower() for i in self.stopwords])
        combined_words = "".join(x + "\n" for x in words if x not in stopwords)
        reshaped_words: List[str] = get_display(arabic_reshaper.reshape(combined_words)).split("\n")
        new_frequencies = dict(zip(reshaped_words, values))
        return super().generate_from_frequencies(new_frequencies, max_font_size)

    def generate(self, text):
        return self.generate_from_text(text)

    def to_html(self):
        pass

