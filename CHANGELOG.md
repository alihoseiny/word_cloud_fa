# 0.1.6
- Adding symbols to the stopwords file.
- Adding `no_reshape` parameter for disabling reshaping words.
- Updating examples
- Fix problem of invalid frequency calculation when using stopwords.
# 0.1.4
- `add_stop_words_from_file` method added to the class for simple adding stopwords from file.
- Add English stop words of `wordcloud` module to the default stopwords plus persian ones.
- Improve the speed of the WordcloudFa by implementing the `process_text` method and don't calling the `Wordcloud` version of that.
