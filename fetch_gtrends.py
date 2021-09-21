# Code to fetch Google Trends data 
# Query setup on file -> ./config.py

# %% Required Libraries
import pandas as pd
from pytrends.request import TrendReq
from config import TIME_FRAME, queries, locations

# %% Functions
def fetch_gtrends_queries(queries, location, timeframe="today 5-y"):
    '''
        Fetch and save data for all queries.
    '''
    gtrends_interest = pd.DataFrame()
    trend_request = TrendReq(hl = location, tz = 180, retries=4, backoff_factor=0.2)
    
    for query in queries:
        print(f"Fetching data. Location: * {location} *    Query: * {query.upper()} *")
        
        kw_list = [query]
        trend_request.build_payload(kw_list=kw_list, 
                                    timeframe=timeframe, 
                                    geo=location)
        
        # Fetch desired data
        interest_over_time = trend_request.interest_over_time()
        fetch_and_save_related_queries(trend_request, location, query)
                    
        # Process data
        try:
            gtrends_interest[query] = interest_over_time[query]
        except:
            gtrends_interest[query] = "NaN"
        
    gtrends_interest.fillna("NaN", inplace=True)
    gtrends_interest.to_csv(f'data/interest_over_time/iot_{location}.csv')
    
def fetch_and_save_related_queries(trend_request, location, query):
    if location == 'BR':
        path = "data/related_queries"
        related_queries = trend_request.related_queries()
        try:
            related_queries[query]['rising'].to_csv(f"{path}/rising/RQ-rising-{location}-{query.upper()}.csv")
            related_queries[query]['top'].to_csv(f"{path}/top/RQ-top-{location}-{query.upper()}.csv")    
        except:
            pass
        
# %% Main 
if __name__ == '__main__':
    
    for location in locations:
        fetch_gtrends_queries(queries, location, TIME_FRAME)