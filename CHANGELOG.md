# 0.1.4
- `add_stop_words_from_file` method added to the class for simple adding stopwords from file.
- Add English stop words of `wordcloud` module to the default stopwords plus persian ones.
- Improve the speed of the WordcloudFa by implementing the `process_text` method and don't calling the `Wordcloud` version of that.
