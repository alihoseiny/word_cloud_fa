from distutils.core import setup

setup(
    name='wordcloud_fa',
    packages=['wordcloud_fa'],
    version='0.1',
    license='MIT',
    description='A wrapper for wordcloud module for creating persian word cloud.',
    author='Mohammadreza Alihoseiny',
    author_email='salam@alihoseiny.ir',
    url='https://github.com/alihoseiny/word_cloud_fa',
    download_url='https://github.com/alihoseiny/word_cloud_fa/archive/0.1.tar.gz',
    keywords=['wordcloud', 'word cloud', 'Farsi', 'persian', 'Iran'],
    install_requires=[
        'arabic_reshaper',
        'python-bidi',
        'wordcloud',
        'hazm'
    ]
)
