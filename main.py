# Импорт
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Первая страница
@app.route('/')
def index():
    return render_template('index.html')

# Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', result=result_calculate(int(size), int(lights), int(device)))

# Форма
@app.route('/form')
def form():
    return render_template('form.html')

# Обработка данных из формы и вывод результатов
@app.route('/submit', methods=['POST'])
def submit_form():
    # Создай переменные для сбора информации
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    # Сохранение данных в файл
    with open('form.txt', 'a') as f:
        f.write(f'Имя: {name}\n')
        f.write(f'Email: {email}\n')
        f.write(f'Адрес: {address}\n')
        f.write(f'Дата приезда: {date}\n')
        f.write('\n')

    # Перенаправление на страницу с результатами
    return render_template('form_result.html', name=name, email=email, address=address, date=date)

app.run(debug=True)