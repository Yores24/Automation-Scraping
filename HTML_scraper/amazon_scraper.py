from datetime import datetime
import requests
import csv
import bs4


if __name__=="__main__":
    with open('amazon_products_urls.csv',newline=',') as csvfile:
        