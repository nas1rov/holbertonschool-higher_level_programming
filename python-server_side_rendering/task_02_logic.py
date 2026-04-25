from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Əgər faylın içində "items" açarı varsa onu götürürük, yoxdursa boş siyahı veririk
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Əgər fayl yoxdursa və ya formatı səhvdirsə, yenə də boş siyahı veririk
        items_list = []
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
