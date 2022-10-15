import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('2x6deEzYbXZ8qzKxJQ8t5-63RqVXFwLNv2eCy0XubjEh')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/cb7275f5-30ed-4396-94f8-9e2bc15e3766')

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    translation = language_translator.translate(text=englishText, model_id="en-fr").get_result()
    frenshText=translation['translations'][0]['translation']
    return frenshText

def frenchToEnglish(frenshText):
    translation = language_translator.translate(text=frenshText, model_id="fr-en").get_result()
    englishText=translation['translations'][0]['translation']
    return englishText