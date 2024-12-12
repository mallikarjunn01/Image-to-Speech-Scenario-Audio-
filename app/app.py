# import os
# import time
# from typing import Any
# import requests
# import streamlit as st
# from dotenv import find_dotenv, load_dotenv
# from transformers import pipeline

# # Load environment variables
# load_dotenv(find_dotenv())
# HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# def main() -> None:
#     """
#     Main function for the Image-to-Scenario Audio Converter app.
#     """
#     st.set_page_config(page_title="Image-to-Scenario Audio Converter", page_icon="🖼️")
#     st.title("Image-to-Scenario Audio Converter")

#     # File uploader for the image
#     uploaded_file: Any = st.file_uploader("Upload an image file (JPG)", type="jpg")

#     if uploaded_file is not None:
#         # Display uploaded image
#         st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)


#         # Save uploaded file
#         with open(uploaded_file.name, "wb") as file:
#             file.write(uploaded_file.getvalue())

#         # Show progress bar
#         st.text("Processing the image...")
#         progress_bar(100)

#         # Generate text from the uploaded image
#         scenario = generate_text_from_image(uploaded_file.name)
#         if scenario.strip():
#             st.success("Scenario generated successfully!")
#             with st.expander("Generated Image Scenario"):
#                 st.write(scenario)

#             # Generate speech from the scenario
#             if generate_speech_from_text(scenario):
#                 st.audio("generated_audio.flac", format="audio/flac")
#             else:
#                 st.error("Failed to generate audio.")
#         else:
#             st.error("Failed to generate scenario text from the image.")

# def progress_bar(duration: int) -> None:
#     """
#     Display a progress bar for a specified duration.
#     """
#     progress_text = "Please wait, Generative models hard at work"
#     my_bar = st.progress(0, text=progress_text)
#     for percent_complete in range(duration):
#         time.sleep(0.04)
#         my_bar.progress(percent_complete + 1, text=progress_text)
#     time.sleep(1)
#     my_bar.empty()

# def generate_text_from_image(image_path: str) -> str:
#     """
#     Generate descriptive text from an image using the BLIP model.
#     """
#     try:
#         image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
#         result = image_to_text(image_path)
#         generated_text = result[0]["generated_text"]
#         print(f"Generated scenario: {generated_text}")
#         return generated_text
#     except Exception as e:
#         print(f"Error in image-to-text generation: {e}")
#         return ""

# import time

# def generate_speech_from_text(message: str) -> bool:
#     """
#     Generate speech from text using HuggingFace API with retry logic.
#     """
#     API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
#     headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
#     payloads = {"inputs": message}
#     max_retries = 3
#     retry_delay = 5  # seconds

#     for attempt in range(max_retries):
#         try:
#             response = requests.post(API_URL, headers=headers, json=payloads)
#             if response.status_code == 200:
#                 with open("generated_audio.flac", "wb") as file:
#                     file.write(response.content)
#                 print("Audio generated successfully.")
#                 return True
#             elif response.status_code == 503:
#                 print(f"Model loading, retrying in {retry_delay} seconds...")
#                 time.sleep(retry_delay)
#             else:
#                 print(f"Error in TTS API: {response.status_code}, {response.text}")
#                 return False
#         except Exception as e:
#             print(f"Exception during TTS generation: {e}")
#             time.sleep(retry_delay)
#     print("Failed to generate audio after multiple attempts.")
#     return False



# if __name__ == "__main__":
#     main()


import os
import time
from typing import Any
import requests
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def main() -> None:
    """
    Main function for the Image-to-Scenario Audio Converter app.
    """
    st.set_page_config(page_title="Image-to-Scenario Audio Converter", page_icon="🖼️")
    st.title("Image-to-Scenario Audio Converter")

    # File uploader for the image
    uploaded_file: Any = st.file_uploader("Upload an image file (JPG)", type="jpg")

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Save uploaded file
        with open(uploaded_file.name, "wb") as file:
            file.write(uploaded_file.getvalue())

        # Show progress bar
        st.text("Processing the image...")
        progress_bar(100)

        # Generate text from the uploaded image
        scenario = generate_text_from_image(uploaded_file.name)
        if scenario.strip():
            st.success("Scenario generated successfully!")
            with st.expander("Generated Image Scenario"):
                st.write(scenario)

            # Generate speech from the scenario
            if generate_speech_from_text(scenario):
                st.audio("generated_audio.flac", format="audio/flac")
            else:
                st.error("Failed to generate audio.")
        else:
            st.error("Failed to generate scenario text from the image.")

    # Add social media links immediately after content
    add_social_links()
    # Add "About Us" section
    add_about_us()

def add_about_us() -> None:
    """
    Add an "About Us" section with content and links.
    """
    with st.expander("About Us", expanded=False):
        st.markdown(
            """
            Welcome to the **Image-to-Scenario Audio Converter App**!  
            This app is designed to seamlessly convert images into descriptive scenarios and provide audio output for accessibility and creative use cases.
            
            ### Features:
            - **Image-to-Text Conversion**: Generate meaningful scenarios from images.
            - **Text-to-Speech**: Convert generated text into audio format.
            - **Seamless Experience**: Easy-to-use interface for uploading and converting files.

            ### Our Mission:
            To make AI-powered solutions accessible and engaging for everyone.


            For queries, reach out at **mallikarjunmyadawad@gmail.com**.
            """
)


def add_social_links() -> None:
    """
    Add social media links to the app.
    """
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://www.instagram.com/mallikarjun_m_y/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png" alt="Instagram" width="30">
            </a>
            &nbsp;&nbsp;
            <a href="https://github.com/mallikarjunn01" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub" width="30">
            </a>
            &nbsp;&nbsp;
            <a href="https://www.linkedin.com/in/mallikarjun-y/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def progress_bar(duration: int) -> None:
    """
    Display a progress bar for a specified duration.
    """
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(duration):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def generate_text_from_image(image_path: str) -> str:
    """
    Generate descriptive text from an image using the BLIP model.
    """
    try:
        image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
        result = image_to_text(image_path)
        generated_text = result[0]["generated_text"]
        print(f"Generated scenario: {generated_text}")
        return generated_text
    except Exception as e:
        print(f"Error in image-to-text generation: {e}")
        return ""

def generate_speech_from_text(message: str) -> bool:
    """
    Generate speech from text using HuggingFace API with retry logic.
    """
    API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payloads = {"inputs": message}
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payloads)
            if response.status_code == 200:
                with open("generated_audio.flac", "wb") as file:
                    file.write(response.content)
                print("Audio generated successfully.")
                return True
            elif response.status_code == 503:
                print(f"Model loading, retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Error in TTS API: {response.status_code}, {response.text}")
                return False
        except Exception as e:
            print(f"Exception during TTS generation: {e}")
            time.sleep(retry_delay)
    print("Failed to generate audio after multiple attempts.")
    return False

if __name__ == "__main__":
    main()

