import bq_helper
hacker_news = bq_helper.BigQueryHelper(active_project="bigquery-public-data",dataset_name="hacker_news")
query = """ SELECT type, COUNT(id)
            FROM `bigquery-public-data.hacker_news.full`
            GROUP BY type
        """
delete = """ SELECT COUNT(*)
              FROM `bigquery-public-data.hacker_news.comments`
              WHERE deleted = True
            """
stories = hacker_news.query_to_pandas_safe(query)
deleted = hacker_news.query_to_pandas_safe(delete)
