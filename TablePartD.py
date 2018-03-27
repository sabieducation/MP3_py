import happybase as hb

conn = hb.Connection()
table = conn.table('powers')

row = table.row(b'row1')
value1 = row[b'personal:hero']
value2 = row[b'personal:power']
value3 = row[b'professional:name']
value4 = row[b'professional:xp']
value5 = row[b'custom:colors']

print('hero: {} power: {} name: {} xp: {} color: {}'.format(value1, value2, value3, value4, value5))



