import csv
from msilib.schema import IniFile

infile = open('Student_Scores.csv', 'r')
outfile = open('student_avg.csv', 'w')

scores = csv.reader(infile, delimiter = ',')

next(scores)

for record in scores:
    score1 = int(record[1])
    score2 = int(record[2])
    score3 = int(record[3])
    avg_score = round((score1 + score2 + score3),2)

    outfile.write(str(avg_score) + '\n')

outfile.close()

