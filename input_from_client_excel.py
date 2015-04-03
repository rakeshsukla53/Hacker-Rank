__author__ = 'rakesh'

import urllib2, re
import json
import xlrd,xlwt
from xlutils.copy import copy
import os,time

#fullAddress = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber=' + str(house) + '&street=' + str(street) + '&borough=' + str(borough) + '&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

file_location = "/home/rakesh/Downloads/Ontodia_Data/Brooklyn_Jobs_and_Economic_Mobility/data/Processed_OpenRefine/borough.xls"
workbook = xlrd.open_workbook(file_location, formatting_info=True)
sheet = workbook.sheet_by_index(0)
wb = copy(workbook)
w_sheet = wb.get_sheet(0)

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

def fullAddress():

    newColumns = []

    address = 'https://api.cityofnewyork.us/geoclient/v1/search.json?input=1%20Fordham%20Plaza%20Bronx&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

    a = urllib2.urlopen(address)

    location = json.load(a)['results'][0]['response']

    #for key, value in location.iteritems():
    #    print key

    #time.sleep(20)

    n = raw_input("How many new columns you want to add")

    for i in range(int(n)):
        a = raw_input("Enter the name of the columns you want to add in the sheet")
        w_sheet.write(0, sheet.ncols + i, str(a))
        newColumns.append(a)

    w_sheet.write(0, sheet.ncols, 'Normalized Address')

    for i in range(int(n)):
        w_sheet.write(0, sheet.ncols + i + 1, str(newColumns[i]))

    for i in range(1, sheet.nrows):
        print 'i = %d' %i
        address = (str(sheet.cell_value(i, 7)) + " " + str(sheet.cell_value(i, 0)))

        match = re.match(r'[0-9]* [0-9]+', str(address))

        if match:
            k = address.split()
            address = k[0] + "-" + k[1]
            try:
                for p in range(2, len(address)-1):
                    address = address + " " + k[p]
            except:
                pass

            address = address.split()

        else:
            address = address.split()

        urlAddress = "%20".join(address)
        urlAddress = "%20" + urlAddress

        address = 'https://api.cityofnewyork.us/geoclient/v1/search.json?input='+str(urlAddress)+'&app_id=e7df1765&app_key=bb80a97381a0fa916bb860768fa71b8f'

        a = urllib2.urlopen(address)

        try:
            print address
            print i, sheet.ncols
            location = json.load(a)['results'][0]['response']
            normalizedAddress = location['houseNumberIn'] + " " + location['boePreferredStreetName'] + " " + location['firstBoroughName'] + " " + location['zipCode']
            w_sheet.write(i, sheet.ncols, normalizedAddress)
            print normalizedAddress

        except:
            try:
                print "Rakesh"
                location = json.load(a)['results'][0]['response']
                normalizedAddress = location['houseNumberIn'] + " " + location['boePreferredStreetName'] + " " + location['firstBoroughName'] + " " + location['zipCode']
                w_sheet.write(i, sheet.ncols, normalizedAddress)
                print normalizedAddress
            except:
                pass

        for j in range(int(n)):
            try:
                print str(location[str(newColumns[j])])
                print sheet.ncols + j + 1
                w_sheet.write(i, sheet.ncols + j + 1, str(location[str(newColumns[j])]))

            except:
                pass

    wb.save('n.xls')

fullAddress()





