from distutils.core import setup

setup(
    name='wordcloud_fa',
    packages=['wordcloud_fa'],
    version='0.1.2',
    license='MIT',
    description='A wrapper for wordcloud module for creating persian word cloud.',
    author='Mohammadreza Alihoseiny',
    author_email='salam@alihoseiny.ir',
    url='https://github.com/alihoseiny/word_cloud_fa',
    download_url='https://github.com/alihoseiny/word_cloud_fa/archive/0.1.2.tar.gz',
    keywords=['wordcloud', 'word cloud', 'Farsi', 'persian', 'Iran', 'nlp', 'National Language Processing',
              'text processing', 'data visualization'],
    install_requires=[
        'numpy>=1.6.1',
        'pillow',
        'matplotlib',
        'arabic_reshaper',
        'python-bidi',
        'wordcloud',
        'hazm'
    ],
    package_data={'wordcloud_fa': ['stopwords', 'Fonts/font.ttf']},
)
