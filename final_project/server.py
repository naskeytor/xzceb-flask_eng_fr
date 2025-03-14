from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    
    french_text = language_translator.translate(
        text=textToTranslate,
        model_id='en-fr').get_result()
    
    return french_text["translations"][0]["translation"]

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = language_translator.translate(
        text=textToTranslate,
        model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]
    

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
