# Master Thesis SDG greenwashing detection

## scripts

### pdf_extractor.py
Extract paragraphs of text from PDF files

### article_scraper.py
Scrape paragraphs of online news articles from a list of links

### aurora.py
Implementation of The Aurora Universities Network SDG classifier.
Requires queries.py to work. This classifier drops the windowing constrains from the original classifier.

### combine_columns.py
Combines the output of aurora and OSDG from two columns into an extra column

### filter_data.py
Only keep texts that are at least 20 tokens

### gn_links.py
Collect all article urls from a Google News page.

### osdg.py
Label text with OSDG classifier. Requires that the OSDG docker container is running.

### sentiment.py
Add a column with a senitment score from VADER.

## links
This folder contains files with all the links to news articles that were used for the research.

## csv
This folder contains all the data that was used for the research

## html
This folder contains the saved HTML search results from Google News that were used for the research
