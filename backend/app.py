from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data structures simulating database
users = {}
recipes = {
    1: {
        "id": 1,
        "title": "Chocolate Cake",
        "ingredients": ["flour", "sugar", "cocoa powder", "eggs"],
        "steps": ["Mix", "Bake"],
        "nutrition": {"calories": 350, "fat": 15},
        "mood_tags": ["happy", "celebration"]
    },
    2: {
        "id":2,
        "title": "Avocado Toast",
        "ingredients": ["bread", "avocado", "salt"],
        "steps": ["Toast bread", "Add avocado"],
        "nutrition": {"calories": 150, "fat": 10},
        "mood_tags": ["relaxed", "healthy"]
    }
}

saved_recipes = {}
comments = {}

@app.route('/mood', methods=['POST'])
def mood_input():
    data = request.json
    mood = data.get('mood')
    # Simple mood matching to recipe
    matched = [r for r in recipes.values() if mood in r['mood_tags']]
    return jsonify(matched)

@app.route('/user/<user_id>/preferences', methods=['GET', 'POST'])
def user_preferences(user_id):
    if request.method == 'POST':
        data = request.json
        users[user_id] = users.get(user_id, {})
        users[user_id]['preferences'] = data
        return jsonify({'message': 'Preferences saved'}), 201
    else:
        return jsonify(users.get(user_id, {}).get('preferences', {}))

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def recipe_details(recipe_id):
    recipe = recipes.get(recipe_id)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'}), 404

@app.route('/user/<user_id>/saved', methods=['POST'])
def save_recipe(user_id):
    data = request.json
    recipe_id = data.get('recipe_id')
    if user_id not in saved_recipes:
        saved_recipes[user_id] = set()
    saved_recipes[user_id].add(recipe_id)
    return jsonify({'message': 'Recipe saved'})

@app.route('/user/<user_id>/saved', methods=['GET'])
def saved_list(user_id):
    saved = saved_recipes.get(user_id, set())
    recs = [recipes[rid] for rid in saved if rid in recipes]
    return jsonify(recs)

@app.route('/recipe/<int:recipe_id>/share', methods=['POST'])
def share_recipe(recipe_id):
    # Dummy share function
    return jsonify({'message': f'Recipe {recipe_id} shared on social media (simulated)'}), 200

@app.route('/recipe/<int:recipe_id>/comments', methods=['POST'])
def post_comment(recipe_id):
    data = request.json
    comment = data.get('comment')
    if recipe_id not in comments:
        comments[recipe_id] = []
    comments[recipe_id].append(comment)
    return jsonify({'message': 'Comment added'}), 201

@app.route('/recipe/<int:recipe_id>/comments', methods=['GET'])
def get_comments(recipe_id):
    return jsonify(comments.get(recipe_id, []))

if __name__ == '__main__':
    app.run(debug=True)
