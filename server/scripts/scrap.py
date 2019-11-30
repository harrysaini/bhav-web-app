import requests
import html5lib
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os 

url = 'https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx'
print(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), './data')) + '/'
print(data_dir)

class BhavCopy:

    def __init__(self):
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, 'html5lib')

    def get_bhav_copy_url(self):
        print("Fetching csv link from site")
        btn_li = self.soup.find(
            'li', attrs={'id': 'ContentPlaceHolder1_liZip'})
        a_link = btn_li.find('a')
        return a_link['href']

    def save_csv_zip(self):
        csv_link = self.get_bhav_copy_url()
        print("Downloading csv zip from: " + csv_link)
        zip_file = requests.get(csv_link, stream=True)
        file_name = csv_link.split('/')[-1]

        with open(data_dir + file_name, 'wb') as file:
            for chunk in zip_file.iter_content(chunk_size=1024):
                # writing chunk at a time to zip file
                if chunk:
                    file.write(chunk)

        return file_name

    def extract_csv_file_zip(self, file_name):
        files = []
        print('Extracting zip file')
        # opening the zip file in READ mode
        with ZipFile(data_dir + file_name, 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()

            for info in zip.infolist():
                files.append(info.filename)

            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall(data_dir)
            print('Extracting Done!')

        return files

    def download_csv_file(self):
        file_name = self.save_csv_zip()
        files = self.extract_csv_file_zip(file_name)
        return files
