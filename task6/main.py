from flask import Flask, render_template, request, redirect, url_for
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        day = request.form.get('day')
        month = request.form.get('month')
        year = request.form.get('year')
        value_id = request.form.get('currency')

        # Форматируем дату в нужный формат
        date_req = f"{day}/{month}/{year}"

        return redirect(url_for('get_currency_rate', date=date_req, value_id=value_id))

    # Получаем список валют
    currencies = get_currencies()
    return render_template('index.html', currencies=currencies)

@app.route('/currency_rate')
def get_currency_rate():
    # Получаем параметры даты и идентификатора валюты из запроса
    date_req = request.args.get('date', default='02/03/2002')
    value_id = request.args.get('value_id', default=None)

    if not value_id:
        abort(400, description="Please provide value_id parameter.")

    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}'
    response = requests.get(url)
    xml_data = response.content

    root = ET.fromstring(xml_data)
    # Ищем валюту по ValueID
    for valute in root.findall('.//Valute'):
        if valute.get('ID') == value_id:
            nominal = float(valute.find('Nominal').text)
            value = float(valute.find('Value').text.replace(',', '.'))
            rate = value / nominal
            char_code = valute.find('CharCode').text
            return f"Курс {char_code} на {root.attrib['Date']}: {rate}"

    return "Currency with the provided ValueID not found.", 404

def get_currencies():
    url = 'http://www.cbr.ru/scripts/XML_val.asp?d=0'
    response = requests.get(url)
    xml_data = response.content

    root = ET.fromstring(xml_data)
    currencies = [
        {'id': item.get('ID'), 'name': item.find('Name').text}
        for item in root.findall('Item')
    ]
    return currencies

if __name__ == '__main__':
    app.run(debug=True)