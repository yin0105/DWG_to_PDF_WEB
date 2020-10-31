import pyodbc
import json

conn = pyodbc.connect('DSN=scanned_master_bills')
cursor = conn.cursor()

sql_mbs = 'SELECT * FROM Masterbills'
sql_notes = 'SELECT id, masterbill_id, note FROM Masterbill_notes'

dMbs = {}
dNotes = {}

for row in cursor.execute(sql_mbs):
    dMbs[row.id] = {'masterbill': row.masterbill,
                    'description': row.description}

for row in cursor.execute(sql_notes):
    dNotes[row.id] = {'masterbill_id': row.masterbill_id, 'note': row.note}

dMasterbills = {}

for key_mb in dMbs:
    notes = []
    for key_note in dNotes:
        if dNotes[key_note]['masterbill_id'] == key_mb:
            notes.append(dNotes[key_note]['note'])
    dMasterbills[dMbs[key_mb]['masterbill']] = {
        'description': dMbs[key_mb]['description'], 'notes': notes}

# print json.dumps(dMasterbills, sort_keys=True, indent=4, separators=(',', ': '))
# print json.dumps(dMasterbills, sort_keys=True)

fJSON = open('mb_notes.json', 'w')
fJSON.write(json.dumps(dMasterbills))
fJSON.close()

cursor.close()
conn.close()
