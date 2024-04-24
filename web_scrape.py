import feedparser
from datetime import datetime
import pandas as pd


class GoogleNewsFeedScraper:
    def __init__(self, s_query):
        self.query = s_query

    def scrape_google_news_feed(self, df, a, b, c):
        # Formatting the query
        new_query = '%3A'.join(self.query.split(':'))
        formatted_query = '%20'.join(new_query.split())

        # Scraping link, title and date of publication using rss feed
        rss_url = f'https://news.google.com/rss/search?q={formatted_query}&hl=en-IN&gl=IN&ceid=IN%3Aen'
        feed = feedparser.parse(rss_url)
        titles = []
        site_names = []
        links = []
        pub_dates = []

        if feed.entries:
            for entry in feed.entries:
                # Title and Website
                title = entry.title
                title_site = title.split(' - ')
                titles.append(title_site[0])
                site_names.append(title_site[1])

                # URL link
                link = entry.link
                links.append(link)

                # Date
                pubdate = entry.published
                date_str = str(pubdate)
                date_obj = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
                formatted_date = date_obj.strftime("%Y-%m-%d")
                pub_dates.append(formatted_date)

        else:
            print("Nothing Found!")

        # Add the new column to the DataFrame
        df_new = pd.DataFrame({'URL link': links,
                               'Website': site_names,
                               'Title': titles,
                               'Date': pub_dates})
        if a == 0 and b == 0 and c == 0:
            df = df_new
        else:
            df = pd.concat([df, df_new], ignore_index=True)

        # Save the updated DataFrame back to the CSV file
        path = 'D:/NMIMS/Sem.6/Capstone/japan.csv'
        df.to_csv(path, index=False)
        return "csv updated"


if __name__ == "__main__":
    # List of countries: India, Japan, USA, UK
    # Query: indian forex rate news "forex" after:2023-01-01 before:2023-12-31
    news = ['forex', 'economy', 'political']
    year = ['2019', '2020', '2021', '2022', '2023', '2024']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    list1 = ['2020', '2024']
    list2 = ['01', '03', '05', '07', '08', '10', '12']
    for i in range(len(year)):
        for j in range(len(month)):
            for k in range(len(news)):
                df_1 = pd.read_csv('japan.csv')
                if month[j] in list2:
                    query = ('japan ' + news[k] + ' news "' + news[k] +
                             '" after:' + year[i] + '-' + month[j] + '-01 before:' +
                             year[i] + '-' + month[j] + '-31')
                    scraper = GoogleNewsFeedScraper(query)
                    print(i, j, k)
                    print(scraper.scrape_google_news_feed(df_1, i, j, k))
                elif month[j] == '02':
                    if year[i] in list1:
                        query = ('japan ' + news[k] + ' news "' + news[k] +
                                 '" after:' + year[i] + '-' + month[j] + '-01 before:' +
                                 year[i] + '-' + month[j] + '-29')
                        scraper = GoogleNewsFeedScraper(query)
                        print(i, j, k)
                        print(scraper.scrape_google_news_feed(df_1, i, j, k))
                    else:
                        query = ('japan ' + news[k] + ' news "' + news[k] +
                                 '" after:' + year[i] + '-' + month[j] + '-01 before:' +
                                 year[i] + '-' + month[j] + '-28')
                        scraper = GoogleNewsFeedScraper(query)
                        print(i, j, k)
                        print(scraper.scrape_google_news_feed(df_1, i, j, k))
                else:
                    query = ('japan ' + news[k] + ' news "' + news[k] +
                             '" after:' + year[i] + '-' + month[j] + '-01 before:' +
                             year[i] + '-' + month[j] + '-30')
                    scraper = GoogleNewsFeedScraper(query)
                    print(i, j, k)
                    print(scraper.scrape_google_news_feed(df_1, i, j, k))
