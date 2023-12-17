# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:56:33 2023

@author: sucre
"""
import os
import pyttsx3
import pyttsx3.voice

class textspeaker():

    @staticmethod
    def text_to_speech_ssml(ssml_text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    
        # Set the voice properties to support SSML
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.name == 'Microsoft Zira Desktop - English (United States)':
                engine.setProperty('voice', voice.id)
                break
    
        engine.say(ssml_text)
        engine.runAndWait()
        
    @staticmethod
    def text_to_speech(text):
        engine = pyttsx3.init(engine='sapi5')
        engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
        engine.say(text)
        engine.runAndWait()
    
    def read_files_in_folder(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):  # Change the file extension if needed
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    print(f"Reading content of file: {file}\n")
                    print(content)
                    print("\n\nReading content through text-to-speech...\n")
                    textspeaker.text_to_speech(content)


ssml_text = f"""
<speak>
    <prosody volume="+50%">
        It's important to note that Bob Lazar's claims about Element 115 and his work at S-4 have been highly controversial and heavily debated.
        <break time="500ms" />
        Many skeptics and researchers in the scientific community have raised questions about the authenticity and credibility of his claims, and there is no concrete evidence to substantiate his assertions.
        <break time="2s" />
        <prosody rate="75%">
            As with any extraordinary claims, it's crucial to approach them with critical thinking and rely on evidence-based research and scientific consensus.
        </prosody>
        <break time="500ms" />
    </prosody>
</speak>
"""

ssml_text = 'The Pythagorean theorem is a statement in mathematics that states that in a right angled triangle'
# if __name__ == "__main__":
#     folder_path = "E:/Dropbox/Work/Self Study/python/Python With ChatGPT"  # Replace with the path to your folder containing the files
#     read_files_in_folder(folder_path)

#textspeaker.text_to_speech_ssml(ssml_text)