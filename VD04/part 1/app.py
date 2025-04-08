from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_current_time():
    # Получаем текущие дату и время и форматируем их
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # Возвращаем HTML с данными
    return f'''
    <html>
        <body>
            <h1>Текущая дата и время:</h1>
            <p>{current_time}</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)