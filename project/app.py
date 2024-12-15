from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

shortened_urls = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['original_url']
    short_code = generate_short_code()
    shortened_urls[short_code] = original_url
    return f"短縮URL: <a href='/{short_code}' target='_blank'>http://localhost:5000/{short_code}</a>"

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = shortened_urls.get(short_code)
    if original_url:
        return redirect(original_url)
    return "URLが見つかりません", 404

if __name__ == '__main__':
    app.run(debug=True)
