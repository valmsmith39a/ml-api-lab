import os 
import openai
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from fastapi import FastAPI

openai.api_key = os.environ['CHATGPT_API_KEY']
ibm_nlu_emotion_detection_api_key = os.environ['IBM_NLU_EMOTION_DETECTION_API_KEY']
ibm_nlu_emotion_detection_url = os.environ['IBM_NLU_EMOTION_DETECTION_URL']

app = FastAPI()

@app.get("/")
async def root():
	return { "message": "Hello Metaverse" }

@app.get("/sentiment/emotion-detection")
async def get_sentiment_emotion_detection(text: str):
	endpoint = ibm_nlu_emotion_detection_url 
	authenticator = IAMAuthenticator(ibm_nlu_emotion_detection_api_key)
	natural_language_understanding = NaturalLanguageUnderstandingV1(version='2021-03-25', authenticator=authenticator)
	natural_language_understanding.set_service_url(endpoint)
	
	text = "I am so happy today!"
	emotion_features = Features(emotion=EmotionOptions())
	
	response = natural_language_understanding.analyze(text=text, features=emotion_features).get_result()
	print(response)
	emotions = response['emotion']['document']['emotion']
	print(emotions)

	# messages = [
	# 	{"role": "system", "content": "You are a helpful assistant."},
	# 	{"role": "user", "content": "Who won the world series in 2020?"},
	# 	{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
	# 	{"role": "user", "content": "Where was it played?"}
	# ]
	# response = call_chatgpt(messages)
	# if 'choices' in response:
	# 	assistant_response = response['choices'][0]['message']['content']
	# 	print(f"Assistant: {assistant_response}")
	# else: 
	# 	print("Error: API response is not as expected")

	return { "message": "Hello from sentiment emotion-detection" }
	
@app.get("/twitter/tweets/summary")
async def get_tweets_summary(text: str):
	return { "message": f"User text input is: {text}"}
	
def call_chatgpt(messages):
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=messages
	)
	return response 
	