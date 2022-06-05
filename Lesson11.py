from pydantic import BaseModel
import json, urllib.request, sqlite3
from collections import namedtuple


Currency = namedtuple('Currency', ['USD', 'EUR', 'RUB'])
Currs = Currency('431', '451', '456')


class NbrbResponse(BaseModel):
    Cur_ID: int
    Date: str
    Cur_Abbreviation: str
    Cur_Scale: int
    Cur_Name: str
    Cur_OfficialRate: float

request_url = 'https://www.nbrb.by/api/exrates/rates/'
sql_db = sqlite3.connect('currency.db')
sql_db.execute("create table if not exists currency (date text, curr text, rate real, unique(date,curr))")
db_cur = sql_db.cursor()
for curr in Currs:
    resp = urllib.request.urlopen(request_url+curr).read()
    answer = NbrbResponse(**json.loads(resp))
    answer.Date = answer.Date[:10]
    print(f'На дату {answer.Date} курс валюты {answer.Cur_Abbreviation} составляет {answer.Cur_OfficialRate}')
    db_cur.execute("replace into currency (date, curr, rate) values (?, ?, ?)", (answer.Date, answer.Cur_Abbreviation, answer.Cur_OfficialRate))
sql_db.commit()
sql_db.close()
