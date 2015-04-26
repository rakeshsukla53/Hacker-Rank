__author__ = 'rakesh'

import urllib2
import json
import xlrd, xlwt
from xlutils.copy import copy
import os, time
#fullAddress = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber=' + str(house) + '&street=' + str(street) + '&borough=' + str(borough) + '&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

file_location = "/home/rakesh/Downloads/Ontodia_Data/Brooklyn_Jobs_and_Economic_Mobility/data/Processed_OpenRefine/borough.xls"
workbook = xlrd.open_workbook(file_location, formatting_info=True)
sheet = workbook.sheet_by_index(0)
wb = copy(workbook)
w_sheet = wb.get_sheet(0)

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]



def fullAddress():

    for i in range(1, sheet.nrows):

        address = (str(sheet.cell_value(i, 7)) + " " + str(sheet.cell_value(i, 0))).split()

        urlAddress = "%20".join(address)

        address = 'https://api.cityofnewyork.us/geoclient/v1/search.json?input='+str(urlAddress)+'&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

        a = urllib2.urlopen(address)

        try:
            location = json.load(a)['results'][0]['response']
        except:
            pass

        for key, value in location.iteritems():

                print key

        time.sleep(20)

        print location

        try:
            w_sheet.write(i, 12, location['latitude'])

            w_sheet.write(i, 9, location['longitude'])

            w_sheet.write(i, 11, location['communityDistrict'])

            w_sheet.write(i, 10, location['bbl'])

        except:
            pass


    wb.save('test.xls')

fullAddress()

