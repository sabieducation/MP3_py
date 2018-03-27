import happybase as hb
import csv

f = 'input.csv'
ufile = open(f)
reader = csv.reader(ufile, delimiter=',')
conn = hb.Connection()
table = conn.table('powers')

i = 0
for row in reader:
    i = i + 1
    print(row)
    table.put(row[0],
        {'personal:name': row[1],
         'personal:power': row[2],
         'professional:name': row[3],
         'professional:xp': row[4],
         'custom:color': row[5]
})


