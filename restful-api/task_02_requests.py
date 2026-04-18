#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder and prints titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    # Status kodunu çap edirik
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        # JSON məlumatını lüğət siyahısına çeviririk
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts and saves specific columns into a CSV file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == 200:
        posts = r.json()
        # Yalnız lazım olan sütunları seçirik
        filtered_data = []
        for post in posts:
            filtered_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })
        # CSV faylına yazma prosesi
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_data)
