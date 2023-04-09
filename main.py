import os 
import openai 
from fastapi import FastAPI

openai.api_key = os.environ['CHATGPT_API_KEY']

app = FastAPI()

@app.get("/")
async def root():
	return { "message": "Hello Metaverse" }

@app.get("/sentiment/emotion-detection")
async def get_sentiment_emotion_detection(text: str):
	messages = [
		{"role": "system", "content": "You are a helpful assistant."},
		{"role": "user", "content": "Who won the world series in 2020?"},
		{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
		{"role": "user", "content": "Where was it played?"}
	]
	response = call_chatgpt(messages)
	if 'choices' in response:
		assistant_response = response['choices'][0]['message']['content']
		print(f"Assistant: {assistant_response}")
	else: 
		print("Error: API response is not as expected")

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
	