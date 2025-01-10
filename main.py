import datetime
from xml.etree.ElementTree import tostring

from dataParser import dataParser
from analiser import analiser
from openpyxl import Workbook
from openpyxl import load_workbook
if __name__ == '__main__':
    dist = dataParser('Km.xlsx' , [datetime.datetime, float])
    price = dataParser('ceny.xlsx' , [datetime.datetime, float])
    tmpanl = analiser(price.dataList, dist.dataList)
    testDate = datetime.datetime(2014, 12, 16)

