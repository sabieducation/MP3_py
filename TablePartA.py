import happybase as hb
# Add a new line

conn = hb.Connection()

cf1 = {
    'personal': dict(),
    'professional': dict(),
    'custom': dict()
}

conn.create_table('powers', cf1)

cf2 = {
    'nutrition': dict(),
    'taste': dict()
}

conn.create_table('food', cf2)

conn.close()


