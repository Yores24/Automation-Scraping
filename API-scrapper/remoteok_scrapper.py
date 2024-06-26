import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL='https://remoteok.com/api/'
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
REQUEST_HEADER={
    'User-Agent':USER_AGENT,
    'Accept-Language':'en-US, en;q=0.5',
}

def get_job_postings():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()

def output_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    
    headers = list(data[0].keys())
    for i in range(len(headers)):
        job_sheet.write(0, i, headers[i])
    
    for i in range(len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(len(values)):
            if isinstance(values[x], str) and len(values[x]) > 32767:
                values[x] = values[x][:32767]
            job_sheet.write(i + 1, x, values[x])
    
    wb.save('remote_jobs.xls')

if __name__ == "__main__":
    json = get_job_postings()[1:]
    output_xls(json)
