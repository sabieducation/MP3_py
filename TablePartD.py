import happybase as hb

conn = hb.Connection()
table = conn.table('powers')

row = table.row(b'row1')
value1 = row[b'personal:hero']
value2 = row[b'personal:power']
value3 = row[b'professional:name']
value4 = row[b'professional:xp']
value5 = row[b'custom:color']

print('hero: {},  power: {},  name: {},  xp: {},  color: {}'.format(value1, value2, value3, value4, value5))

row = table.row(b'row19')
value1 = row[b'personal:hero']
value2 = row[b'custom:color']

print('hero: {},  color: {}'.format(value1, value2))

row = table.row(b'row1')
value1 = row[b'personal:hero']
value2 = row[b'professional:name']
value3 = row[b'custom:color']

print('hero: {},  name: {},  color: {}'.format(value1, value2, value3))



