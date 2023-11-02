from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from random import randint
from os import getenv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Application config
app.config.from_object(Config)

@app.route('/api/pokemon', methods=['POST'])
def create_a_pokemon():
    data = request.get_json()
    pokemon1 = data['pokemon1']
    pokemon2 = data['pokemon2']
    pokemon_type = data['type']
    skill = data['skill']

    # a random number between 1 and 4
    random_number = randint(1, int(getenv("GENERATION_PROMPT_COUNT") or 4))

    # load a prompt from .env file
    prompt = getenv(f"GENERATION_PROMPT_{random_number}")

    if (not prompt):
        return jsonify({
            "data": {
                "message": f"Error: No prompt found for {random_number}"
            }
        })

    # replace the placeholders with the values
    prompt = prompt.replace("{pokemon1}", pokemon1)
    prompt = prompt.replace("{pokemon2}", pokemon2)
    prompt = prompt.replace("{type}", pokemon_type)
    prompt = prompt.replace("{skill}", skill)

    return jsonify({
        "data": {
            "message": f"{prompt}"
        }
    })
