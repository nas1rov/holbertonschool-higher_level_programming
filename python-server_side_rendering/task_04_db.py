from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- Məlumat oxuma funksiyaları ---

def read_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

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

def read_sqlite():
    products = []
    try:
        # Bazaya qoşuluruq
        conn = sqlite3.connect('products.db')
        # Sütun adları ilə məlumatı çəkə bilmək üçün sqlite3.Row istifadə edirik
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        # Row obyektlərini dictionary-yə (sözlüyə) çeviririk
        for row in rows:
            products.append(dict(row))
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None  # Xəta baş verərsə None qaytarırıq

# --- Əvvəlki tapşırıqlardan qalan route-lar ---
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

# --- Yenilənmiş /products route-u ---
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    # 1. Edge Case: 'source' səhvdirsə
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error_msg="Wrong source")
    # 2. Mənbəyə görə məlumatı oxuyuruq
    data = []
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite()
        # Bazada xəta olub-olmadığını yoxlayırıq
        if data is None:
            return render_template('product_display.html', error_msg="Database error")
    # 3. ID verilibsə məlumatı süzgəcdən keçiririk
    if product_id:
        filtered_data = [p for p in data if str(p.get('id')) == str(product_id)]
        if not filtered_data:
            return render_template('product_display.html', error_msg="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
