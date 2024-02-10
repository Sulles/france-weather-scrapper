# france-weather-scrapper

Scrape Historical French Weather Data

## Scraping Data

Scraping data is done by calling `python scrape.py` with the necessary arguments. To see how to use `scrape.py`,
you can call `python scrape.py -h`.
`scrape.py` will scrape data from the website and store it in the `raw_data.csv`.
Data is scrapped from https://www.infoclimat.fr/observations-meteo/archives

## Creating a Stitching Guide

Creating a stitching guide pulls data from `raw_data.csv` and converts it into stitches (data, hot, cold) and saves that
data in `stitching_guide.csv`.
To convert the data from `raw_data.csv` to `stitching_guide.csv`, simply call `python create_stitiching_guide.py` (
without any arguments)
