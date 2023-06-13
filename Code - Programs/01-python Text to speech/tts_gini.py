from gtts import gTTS
import playsound
import os
def talk(text):
    # create audio data
    file_name = r"C:\manos\python\tts_gini\audio_data_gini_1.wav"
    tts = gTTS(text=text, lang='el')                   # κείμενο σε ομιλία (text to speech) απο google και επιλογή ελληνικών 
    tts.save(file_name)                                # Αποθήκευση ως αρχείου ήχου της μετατροπής
    # playsound.playsound("audio_data_gini+music.wav") 
    playsound.playsound("audio_data_gini_1.wav")       # Αναπαραγωγή αρχείου ήχου
    os.remove(file_name)
talk("Ούφφ,επιτέλους βγήκα!! Είμαι το τζίνι του εργαστηρίου!Αφού με βρήκες,μπορώ να εκπληρώσω τις επιθυμίες σου .... Τι θέλεις να κάνω;")
playsound.playsound("gini.wav")