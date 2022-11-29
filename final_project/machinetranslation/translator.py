""" Watson translators """

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
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
def english_to_french():
    """ To french traduction """
    french_text = language_translator.translate(
        text='Hello',
        model_id='en-fr').get_result()
    
    return french_text["translations"][0]["translation"]
def french_to_english():
    """ To english traduction """
    english_text = language_translator.translate(
        text='Bonjour',
        model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]

english_to_french()
