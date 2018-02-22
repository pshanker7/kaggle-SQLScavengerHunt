import bq_helper #import BigQuery Helper
open_aq = bq_helper.BigQueryHelper(active_project="bigquery-public-data", dataset_name="openaq")
query = """SELECT country 
           FROM `bigquery-public-data.openaq.global_air_quality` 
           WHERE unit !=  'µg/m³' """
countries = open_aq.query_to_pandas_safe(query)
countries.country.value_counts().head()
query2 = """ SELECT pollutant 
              FROM `bigquery-public-data.openaq.global_air_quality` 
              WHERE value = 0"""
pollutants = open_aq.query_to_pandas_safe(query2)
pollutants.pollutant.value_counts().head()
