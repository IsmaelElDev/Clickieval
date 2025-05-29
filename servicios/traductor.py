import json

class TranslationManager:
    def __init__(self, idioma):
        self.idioma = idioma
        self.translations = self.cargar_traducciones(idioma)

    def cargar_traducciones(self, idioma):
        try:
            with open(f'locales/{idioma}.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[WARN] Archivo de traducción '{idioma}' no encontrado. Usando español por defecto.")
            with open('locales/es.json', 'r', encoding='utf-8') as f:
                return json.load(f)

    def t(self, clave):
        return self.translations.get(clave)
