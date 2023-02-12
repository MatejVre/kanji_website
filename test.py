import xml.etree.ElementTree as ET
import sqlite3
from sqlite3 import Error
import requests
# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('Kanji_20230101_213736.xml')

# getting the parent tag of
# the xml document
root = tree.getroot()

# printing the root (parent) tag
# of the xml document, along with
# its memory location
print(root[1][1].text)
        
conn = None
try:
    conn = sqlite3.connect("db.sqlite3")
except Error as e:
    print(e)

for i in range(1,2137):
    id = root[i][0].text
    symbol = root[i][1].text
    response = requests.get("https://kanjiapi.dev/v1/kanji/%s" % symbol)
    meanings = ", ".join(response.json().get("meanings"))
    kun_readings = ", ".join(response.json().get("kun_readings"))
    on_readings = ", ".join(response.json().get("on_readings"))
    name_readings = ", ".join(response.json().get("name_readings"))
    strokes = root[i][2].text
    grade = root[i][3].text
    kanji_classification = root[i][4].text
    JLPT = root[i][5].text
    radical = root[i][6].text
    joyo_reading = root[i][8].text
    non_joyo_reading = root[i][9].text

    on_within_joyo = root[1][11].text
    kun_within_joyo = root[1][17].text
    sql = "INSERT INTO kanjinator_kanji(id,kanji,grade,strokes,meanings,kun_readings,on_readings,name_readings,kanji_classification,JLPT) VALUES (?,?,?,?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,(id,symbol,grade,strokes,meanings,kun_readings,on_readings,name_readings,kanji_classification,JLPT))
    conn.commit()
