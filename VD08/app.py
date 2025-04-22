from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    try:
        # Получаем случайную цитату из ZenQuotes API
        response = requests.get('https://zenquotes.io/api/random')
        quote_data = response.json()[0]  # API возвращает массив с одним элементом

        quote = {
            'text': quote_data['q'],
            'author': quote_data['a']
        }
    except Exception as e:
        quote = {
            'text': f'Ошибка: {str(e)}',
            'author': 'Система'
        }

    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True)