from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

class Data:
    def __init__(self, id, end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood):
        self.id = id
        self.end_year = end_year
        self.intensity = intensity
        self.sector = sector
        self.topic = topic
        self.insight = insight
        self.url = url
        self.region = region
        self.start_year = start_year
        self.impact = impact
        self.added = added
        self.published = published
        self.country = country
        self.relevance = relevance
        self.pestle = pestle
        self.source = source
        self.title = title
        self.likelihood = likelihood

    @classmethod
    def from_json(cls, from_data):
        with open(from_data, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return cls(**data)

    @classmethod
    def from_json(cls, from_data):
        with open(from_data, 'r') as file:
            data = json.load(file)
        return cls(**data)

# Usage example:
data_instance = Data.from_json('jsondata.json')

# Accessing attributes of the data instance
print("Title:", data_instance.title)
print("Intensity:", data_instance.intensity)
print("Country:", data_instance.country)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/allinfo', methods=['GET'])
def info():
    cursor = mysql.get_db().cursor()
    cursor.execute('select * from telanganagov')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        # Assuming the data is read from a JSON file
        data_instance = Data.from_json('jsondata.json')
        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/list_data', methods=['GET'])
def list_data():
    # Assuming you want to list the attributes of the data instance
    return jsonify(data_instance.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
