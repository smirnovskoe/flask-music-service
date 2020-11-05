from flask import Flask

app = Flask(__name__)

inner_db = [
    {
        'id': 1,
        'singer': 'Sting',
        'song': 'Desert Rose'
    },
    {
        'id': 2,
        'singer': 'Boney M',
        'song': 'Rasputin'
    },
    {
        'id': 3,
        'singer': 'Bob Dylan',
        'song': 'Knockin\'On Heaven\'s Door'
    },
    {
        'id': 4,
        'singer': 'Guns & Roses',
        'song': 'November Rain'
    },
]

@app.route('/')
def index():
    return "Test"


if __name__ == "__main__":
    app.run(debug=True)
