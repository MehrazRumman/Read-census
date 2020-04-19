#! python3
# calculate population and number of census tracts for each county
import pprint
import openpyxl
print("Opening WordBook... ... ...")
wb=openpyxl.load_workbook("d:\\censuspopdata.xlsx")
sheet=wb["Population by Census Tract"]
countydata={}
# TODO: Fill in countyData with each county's population and tracts
print("Reading Rows... ... ...")
for row in range(2,sheet.max_row+1):

    # each row in the spreadsheet has data for one census tract
    state=sheet["B" +str(row)].value
    county=sheet["C" + str(row)].value
    pop=sheet["D" + str(row)].value
    # Make sure the key for this state exists.
    countydata.setdefault(state,{})
    # Make sure the key for this county in this state exists.
    countydata[state].setdefault(county,{"tracts":0, "pop":0})
    # Each row represents one census tract, so increment by one.
    countydata[state][county]["pop"] += 1
    # Increase the county pop by the pop in this census tract
    countydata[state][county]["pop"] += int(pop)
# todo : open a new text file and write the contents of countyData to it
print("writing results")
resultfile=open("d:\\xkcd\census2010.py","w")
resultfile.write("alldata= " +pprint.pformat(countydata))
resultfile.close()
print("Done")

