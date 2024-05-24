import requests
import json

def run_llama(input_text):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama2",
        "prompt": json.dumps(input_text),
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return response.json().get('response', 'No response field in JSON')
    else:
        return f"Error: {response.status_code} - {response.text}"
