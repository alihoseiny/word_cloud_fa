from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wordcloud_fa',
    packages=['wordcloud_fa'],
    version='0.1.10',
    license='MIT',
    description='A wrapper for wordcloud module for creating persian (and other rtl languages) word cloud.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mohammadreza Alihoseiny',
    author_email='salam@alihoseiny.ir',
    url='https://github.com/alihoseiny/word_cloud_fa',
    download_url='https://github.com/alihoseiny/word_cloud_fa/archive/V0.1.10.tar.gz',
    keywords=['wordcloud', 'word cloud', 'Farsi', 'persian', 'Iran', 'nlp', 'National Language Processing',
              'text processing', 'data visualization'],
    install_requires=[
        'numpy>=1.18.1',
        'pillow>=7.0.0',
        'matplotlib>=3.1.2',
        'arabic_reshaper>=2.1.3',
        'python-bidi==0.4.2',
        'wordcloud==1.8.2.2',
        'hazm==0.9.1',
    ],
    package_data={'wordcloud_fa': ['stopwords', 'Fonts/font.ttf']},
)
