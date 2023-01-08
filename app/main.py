import re
from fastapi import FastAPI
from tinydb import Query as q

from database import db

app = FastAPI()


@app.post('/get_form/{f_name1}={value1}&{f_name2}={value2}')
def get_form(f_name1: str, f_name2: str, value1: str, value2: str):
    # validation
    val1 = []
    val2 = []
    final_values = []
    while len(final_values) < 2:
        if f_name1.endswith('date') or f_name2.endswith('date'):
            date1 = re.search('^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$',
                              value1)
            date2 = re.search('^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$',
                              value2)
            if date1:
                final_values.append(date1.group(0))
                val1.append(date1.group(0))
            elif date2:
                final_values.append(date2.group(0))
                val2.append(date2.group(0))
        if f_name1.endswith('phone') or f_name2.endswith('phone'):
            phone1 = re.search('((\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',
                               value1)
            phone2 = re.search('((\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',
                               value2)
            if phone1:
                final_values.append(phone1.group(0))
                val1.append(phone1.group(0))
            elif phone2:
                final_values.append(phone2.group(0))
                val2.append(phone2.group(0))

        if f_name1.endswith('email') or f_name2.endswith('email'):
            email1 = re.search('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                               value1)
            email2 = re.search('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                               value2)
            if email1:
                final_values.append(email1.group(0))
                val1.append(email1.group(0))
            elif email2:
                final_values.append(email2.group(0))
                val2.append(email2.group(0))
        if f_name1.endswith('text') or f_name1.endswith('name') or f_name2.endswith('text') or f_name2.endswith('name'):
            if f_name1:
                final_values.append(value1)
                val1.append(value1)
            elif f_name2:
                final_values.append(value2)
                val2.append(value2)

    value1 = val1[0]
    value2 = val2[0]
    # searching for the form
    search = db.get((q()[f_name1] == value1) & (q()[f_name2] == value2))
    if search:
        return search.get('name')
    else:
        return {f_name1: value1, f_name2: value2}

#
# if __name__ == '__main__':
#     uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
