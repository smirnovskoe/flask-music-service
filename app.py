from flask import Flask, jsonify, abort

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


@app.route('/api/tracks')
def get_tracks():
    return jsonify({'tracks': inner_db})


@app.route('/api/tracks/<int:track_id>', methods=['GET'])
def get_track_by_id(track_id):
    track = list(filter(lambda x: x['id'] == track_id, inner_db))
    if(len(track) == 0):
        abort(404)

    return jsonify({'track': track})


if __name__ == "__main__":
    app.run(debug=True, port=9999)
