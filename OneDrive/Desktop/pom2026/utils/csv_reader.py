import csv
import os


class CSVReader:
    
    @staticmethod
    def read_csv_data(file_path = "test_data.csv"):
        if not os.path.exists(file_path):
            raise FileNotFoundError
        
        data_list = []
        
        with open(file_path, mode='r',encoding="utf-8-sig") as files:
            reader = csv.DictReader(files, delimiter="|")
            for row in reader:
                data_list.append(row)
                
        return data_list
        