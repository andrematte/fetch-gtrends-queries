# Fetch data from Google Trends

![](https://img.shields.io/github/license/andrematte/fetch-gtrends-queries?color=red&label=License&style=for-the-badge) ![](https://img.shields.io/github/stars/andrematte/fetch-gtrends-queries?logo=github&style=for-the-badge)

## 💬 Description:

Easily fetch a list of queries from Google Trends using the [PyTrends](https://github.com/GeneralMills/pytrends) library. 

## 🛠  Requirements

This script requires the [PyTrends](https://github.com/GeneralMills/pytrends) library. To install this library run the following command:

`pip install pytrends`

## 💡  How to use
1 - Edit the config.py file to set the following items:
   - `TIME_FRAME`: Start end End dates for the query search;
   - `queries`: List of queries that will be run separately;
   - `locations`: List of locations to fetch data from;
   
2 - Run the `fetch_gtrends.py` script

3 - Results will be saved on the data folder:
  - Interest Over Time: returns historical, indexed data for when the keyword was searched most as shown on Google Trends' Interest Over Time section.
  - Related Queries: returns data for the related keywords to a provided keyword shown on Google Trends' Related Queries section.
