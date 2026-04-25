from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# JSON oxuma funksiyası
def read_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# CSV oxuma funksiyası
def read_csv(filepath):
    products = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError:
        return []

# --- ƏVVƏLKİ ROUTE-LAR (Sistemin yoxlaması üçün saxlamaq məsləhətdir) ---
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
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)
# --------------------------------------------------------------------------

# YENİ ROUTE: /products
@app.route('/products')
def products():
    # URL-dən 'source' və 'id' parametrlərini alırıq
    source = request.args.get('source')
    product_id = request.args.get('id')
    # 1. Edge Case: 'source' səhvdirsə (nə json, nə csv deyil)
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error_msg="Wrong source")
    # Məlumatı müvafiq mənbədən oxuyuruq
    data = []
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    # 2. Edge Case: 'id' verilibsə süzgəcdən keçiririk
    if product_id:
        # Həm JSON-dakı rəqəm, həm də CSV-dəki mətn tipli ID-ləri müqayisə edə bilmək üçün hamısını string-ə(mətni) çeviririk.
        filtered_data = [p for p in data if str(p.get('id')) == str(product_id)]
        # Əgər o ID-də məhsul tapılmadırsa
        if not filtered_data:
            return render_template('product_display.html', error_msg="Product not found")
        # Tapıldısa yalnız onu siyahı olaraq təyin edirik
        data = filtered_data

    # Heç bir xəta yoxdursa, məlumatları şablona göndəririk
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
