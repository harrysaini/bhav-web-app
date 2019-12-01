from scripts.scrap import BhavCopy, data_dir
from scripts.redisConn import redisConnection
import csv

# [code, name, open, high, low, close]
fields_to_save = ['SC_CODE', 'SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']
defaults = {
    'SC_CODE': "invalid", 
    'SC_NAME': "invalid", 
    'OPEN': '0', 
    'HIGH': '0', 
    'LOW': '0', 
    'CLOSE': '0'
}
int_fields = ['OPEN', 'HIGH', 'LOW', 'CLOSE']
MAX_TO_SAVE = 10000

class SaveCSV:
    def __init__(self, files):
        self.file_name = files[0]

    def parse_csv_file(self):
        print('Parsing csv file')
        rows = []
        fields = []
        rows_to_save = []

        with open(data_dir + self.file_name, 'r') as file:
             # creating a csv reader object
            csv_reader = csv.reader(file)

            # extracting field names through first row
            fields = next(csv_reader)

            # extracting each data row one by one
            for row in csv_reader:
                rows.append(row)

            # get total number of rows
            print("Total no. of rows: %d" % (csv_reader.line_num))

        print(len(rows))

        # convert to dict
        for row in rows[0:MAX_TO_SAVE]:
            row_dict = {}
            for i in range(len(row)):
                row_dict[fields[i]] = row[i].strip().lower()

            rows_to_save_dict = {field: (row_dict[field] if row_dict[field] else defaults[field]) for field in fields_to_save}

            for field in int_fields:
                rows_to_save_dict[field] = float(rows_to_save_dict[field])
            
            rows_to_save.append(rows_to_save_dict)

        return rows_to_save


    
    
def setup_db():
    bhavCopy = BhavCopy()
    files = bhavCopy.download_csv_file()
    csv_saver = SaveCSV(files)
    stocks = csv_saver.parse_csv_file()
    print("Saving stocks to db")
    redisConnection.save_stocks(stocks)


