from googletrans import Translator

#3 translate_contents 함수
def translate_contents(text, dest='ko'):
    translator = Translator()
    translated = translator.translate(text, dest=dest)
    return translated.text
