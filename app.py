from flask import Flask, jsonify, abort, make_response, request

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


@app.route('/api/music', methods=['GET', 'POST'])
def get_tracks():
    """List or create tracks"""
    if request.method == 'POST':
        print(request.json)
        if 'singer' not in request.json or 'song' not in request.json:
            abort(400)
        track = {
            'id': inner_db[-1]['id'] + 1,
            'singer': request.json['singer'],
            'song': request.json['song']
        }
        inner_db.append(track)
        return jsonify({"track": track},)
    # request.method == 'GET'
    return jsonify({'tracks': inner_db})


@app.route('/api/music/<int:track_id>', methods=['GET'])
def get_track_by_id(track_id):
    track = list(filter(lambda x: x['id'] == track_id, inner_db))
    if not track:
        abort(404)

    return jsonify({'track': track})


@app.route('/api/music/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    """Delete track from Db by it id"""
    track = list(filter(lambda x: x['id'] == track_id, inner_db))
    if not track:
        abort(404)
    inner_db.remove(track[0])

    return jsonify({'track': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}))


if __name__ == "__main__":
    app.run(debug=True, port=9998)
