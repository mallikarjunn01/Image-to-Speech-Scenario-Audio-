# Image-to-Speech-Scenario-Audio-
The Image-to-Speech that generates an audio Scenario Audio based on the context of an uploaded image.

## Run website with Streamlit

## Approach
An app that uses Hugging Face AI models to generate text from an image, which then generates audio from the text.

Execution is divided into 2 parts:
- **Image to text:**
  an image-to-text transformer model ([Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)) is used to generate a text scenario based on the on the AI understanding of the image context
- **Text to speech:**
  A text-to-speech transformer model ([facebook/mms-tts-eng](https://huggingface.co/facebook/mms-tts-eng)) is used to convert the generated text into a voice-narrated audio file
- A user interface is built using streamlit to enable uploading the image and playing the audio file


## Requirements

- os
- python-dotenv
- transformers
- torch
- langchain
- openai
- requests
- streamlit
  

## Usage

- Before using the app, the user should have personal tokens for Hugging Face.
- The user should set venv environment and install ipykernel library for running app on local system ide.
- The user should save the personal tokens in an ".env" file within the package as string objects under object names: HUGGINGFACE_TOKEN
- The user can then run by using the command: streamlit run app.py
- Once it start running on streamlit, the user can upload the target image
- Execution will start automatically and it may take a few minutes to complete
- Once completed, the app will display:
  - The scenario text generated by the image-to-text transformer HuggingFace model
  - The audio file generated by the text-to-speech transformer model
