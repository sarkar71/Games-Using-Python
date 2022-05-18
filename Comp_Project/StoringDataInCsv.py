import csv

def StoreScoreToCsv(name, n, score):
    f = open("Score.csv","a+",newline='')
    FileWriter = csv.writer(f)
    FileWriter.writerow([name,n,score])
    f.close()

def CalculateHighestScore(n):
    f = open("Score.csv","r")
    FileReader = csv.reader(f)
    HighestScore = 0
    ScorerName = ''
    for row in FileReader:
        if int(row[2]) > HighestScore and int(row[1]) == n:
            HighestScore = int(row[2])
            ScorerName = row[0]
    f.close()
    return (ScorerName,HighestScore)


