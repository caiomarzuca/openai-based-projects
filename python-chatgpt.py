import requests
import openai
import argparse
import os
import shutil

# Adicionando argumentos para processamento 
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="The Nme of the file to save python code")
arg = parser.parse_args()

# Endpoint, api key and request (headers and data) to be send
# See OpenAI doc's
api_endpoint = "https://api.openai.com/v1/completions"

# Confi. section varible for api key
api_key = os.getenv("OPENAI_API_KEY")
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
# Requested data
request_data = {
    "model": "text-davinci-003",
    "prompt": f"Escreva um código python {arg.prompt}",
    "max_tokens": 1000,
    "temperature": 0.5,
}

# Getting the response
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

# Path for the code folder
generated_codes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python-codes")

if not os.path.exists(generated_codes_path):
        os.makedirs(generated_codes_path)

# Checking if everything it's ok and create a file by the arg file_name
if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(f"{arg.file_name}", "w") as file:
        file.write(response_text)
    file.close()
else: 
    print(f"Request failed, error: {str(response.status_code)}")

# Moving the created python code file
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{arg.file_name}")
shutil.move(file_path, generated_codes_path)