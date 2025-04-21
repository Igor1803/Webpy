from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_quote():
    # Отправляем запрос к API
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = data.get('content', 'Цитата не найдена')
        author = data.get('author', 'Автор неизвестен')
    else:
        quote = "Ошибка при получении цитаты"
        author = "Попробуйте позже"
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)