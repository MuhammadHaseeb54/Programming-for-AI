import pyttsx3
import os

def speak_text(text):
    """Generate a spoken audio file from text and return relative path for use in Flask."""
    engine = pyttsx3.init()
    audio_dir = 'static'
    audio_filename = 'voice_output.mp3'
    audio_path = os.path.join(audio_dir, audio_filename)

    # Save spoken text to file
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    # Return relative path used in HTML
    return audio_filename
