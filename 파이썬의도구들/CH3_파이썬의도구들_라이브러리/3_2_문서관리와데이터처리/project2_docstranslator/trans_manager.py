from googletrans import Translator

def translate_contents(text, dest='ko'):
    translator = Translator()
    translated = translator.translate(text, dest=dest)
    return translated.text
