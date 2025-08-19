import csv
import requests
from io import StringIO

def get_word_pairs(csv_url):
    response = requests.get(csv_url)
    response.raise_for_status()
    data = response.content.decode("utf-8")
    reader = csv.reader(StringIO(data))
    
    # assume first row is headers: English, Afrikaans
    word_pairs = {row[0].strip(): row[1].strip() for row in reader if len(row) >= 2}
    return word_pairs