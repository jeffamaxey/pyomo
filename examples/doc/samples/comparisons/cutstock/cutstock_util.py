def getCutCount():
    cutCount = 0
    with open('WidthDemand.csv', 'r') as fout1:
        for _ in fout1:
            cutCount += 1
    return cutCount
    
def getPatCount():
    patCount = 0
    with open('Waste.csv', 'r') as fout2:
        for _ in fout2:
            patCount += 1
    return patCount

def getPriceSheetData():
    return 28
    
def getSheetsAvail():
    return 2000
    
def getCuts():
    cutcount = getCutCount()
    Cuts = range(cutcount)
    for i in range(cutcount):
        nstr = str(i+1)
        Cuts[i] = f'w{nstr}'
    return Cuts

def getPatterns():
    patcount = getPatCount()
    Patterns = range(patcount)
    for j in range(patcount):
        pstr = str(j+1)
        Patterns[j] = f'P{pstr}'
    return Patterns 
    
def getCutDemand():
    i = 0
    cutcount = getCutCount()
    CutDemand = range(cutcount)
    with open('WidthDemand.csv', 'r') as fout1:
        for eachline in fout1:
            str = eachline.rstrip("\n")
            CutDemand[i] = int(str)
            i += 1
    return CutDemand

def getCutsInPattern():
    cutcount = getCutCount()
    patcount = getPatCount()
    CutsInPattern = [[0 for _ in range(patcount)] for _ in range(cutcount)]
    with open('Patterns.csv', 'r') as fout2:
        for eachline in fout2:
            str = eachline
            lstr = str.split(",")
            pstr = lstr[0]
            wstr = lstr[1]
            cstr = lstr[2]
            pstr = pstr.replace("P","")
            wstr = wstr.replace("w","")
            cstr = cstr.rstrip("\n")
            p = int(pstr)
            w = int(wstr)
            c = int(cstr)
            CutsInPattern[w-1][p-1] = c
    return CutsInPattern
