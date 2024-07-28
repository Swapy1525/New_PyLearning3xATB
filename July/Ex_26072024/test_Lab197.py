import csv
import pandas
import pandas as pd

# pip install pandas
class Test_CRUD(object):
    def test_update_1(self):
        # Read the file
        with open('July/Ex_26072024/testdata.csv') as csvfile:
            reader= csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('July/Ex_26072024/testdata.csv')
        print(df)