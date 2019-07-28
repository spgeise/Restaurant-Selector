from csv import reader

zipcodes = []
latlist = []
longlist = []


def openconverstionfile():
    file_name = 'Files\Zipcodelist.txt'
    with open(file_name) as zipdata:
        zipfile = reader(zipdata)
        for row in zipfile:
            zipcodes.append(row[0])
            latlist.append(row[1])
            longlist.append(row[2])