from flask import Flask, jsonify
import pandas as pd
import urllib.parse

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    sheet_id = "1CrupWIBU3NP49ORN3AxC6ave7SD01ds_odu7NVBOIoI"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=Sheet1"
    df = pd.read_csv(url)
    # Mengembalikan data dalam format JSON agar bisa dibaca di dashboard
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run()
