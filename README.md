# Text Mining for Sustainability: Detecting Corporate Greenwashing with The Sustainable Development Goals

## [scripts](https://github.com/dyonende/SDG/tree/master/scripts)
The following scripts were used for my thesis.
There were run in order as listed below as they require the output of the previous step.
The PDFs are not stored on this repository but can be found on the websites of the companies.

1. [pdf_extractor.py](https://github.com/dyonende/SDG/blob/master/scripts/pdf_extractor.py)
Extract paragraphs of text from PDF files

2. [gn_links.py](https://github.com/dyonende/SDG/blob/master/scripts/gn_links.py)
Collect all article urls from a Google News page.

3. [article_scraper.py](https://github.com/dyonende/SDG/blob/master/scripts/article_scraper.py)
Scrape paragraphs of online news articles from a list of links

4. [filter_data.py](https://github.com/dyonende/SDG/blob/master/scripts/filter_data.py)
Only keep texts that are at least 20 tokens

5. [aurora.py](https://github.com/dyonende/SDG/blob/master/scripts/aurora.py)
Implementation of The Aurora Universities Network SDG classifier.
Requires queries.py to work. This classifier drops the windowing constrains from the original classifier.

6. [osdg.py](https://github.com/dyonende/SDG/blob/master/scripts/osdg.py)
Label text with OSDG classifier. Requires that the OSDG docker container is running.

7. [combine_columns.py](https://github.com/dyonende/SDG/blob/master/scripts/combine_columns.py)
Combines the output of aurora and OSDG from two columns into an extra column.

8. [sentiment.py](https://github.com/dyonende/SDG/blob/master/scripts/sentiment.py)
Add a column with a senitment score from VADER.

## [links](https://github.com/dyonende/SDG/tree/master/links)
This folder contains files with all the links to news articles that were used for the research.

## [classifier evaluation](https://github.com/dyonende/SDG/tree/master/classifier%20evaluation)

- [Annotation_Guidelines.pdf](https://github.com/dyonende/SDG/blob/master/classifier%20evaluation/Annotation_Guidelines.pdf)
The annotation guidelines that were used for the evaluation task.
- [corpus.csv](https://github.com/dyonende/SDG/blob/master/classifier%20evaluation/corpus.csv)
The questions from the evaluation with gold labels.

## [csv](https://github.com/dyonende/SDG/tree/master/csv)
This folder contains all the data that was used for the research

## [html](https://github.com/dyonende/SDG/tree/master/html)
This folder contains the saved HTML search results from Google News that were used for the research
