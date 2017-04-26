import csv
import sys
datas = csv.DictReader(open(str(sys.argv[1])))
ws = int(sys.argv[2])
shift = int(sys.argv[3])
OHLC = []
Volume = []

for data in datas :
    OHLC.append((float(data['Open'])+float(data['High'])+float(data['Low'])+float(data['Close']))/4)
    Volume.append(float(data['Volume']))

fieldnames =[]
for i in range(ws):
    fieldnames.append("OHLC"+str(i+1))
fieldnames.append("Label")
writer = csv.DictWriter(open(str(sys.argv[1])[:-4]+"-OHLC.csv",'w'),fieldnames=fieldnames)
writer.writeheader()
fieldnames2 =[]
for i in range(ws):
    fieldnames2.append("Volume"+str(i+1))
fieldnames2.append("Label")
writer2 = csv.DictWriter(open(str(sys.argv[1])[:-4]+"-Volume.csv",'w'),fieldnames=fieldnames2)
writer2.writeheader()
for i in range(len(OHLC)-ws-shift) :
    rowOHLC = {}
    rowVolume ={}
    for j in range(ws+shift):
        rowOHLC[fieldnames[j]] = OHLC[i+j]
        rowVolume[fieldnames2[j]] = Volume[i+j]
    writer.writerow(rowOHLC)
    writer2.writerow(rowVolume)
