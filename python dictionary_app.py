# dictionary_app.py
import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        meaning = data['meanings'][0]['definitions'][0]
        definition = meaning.get('definition', 'No definition found.')
        example = meaning.get('example', 'No example available.')
        synonyms = meaning.get('synonyms', [])
        
        print(f"\n📘 Word: {word.capitalize()}")
        print(f"📖 Definition: {definition}")
        print(f"💬 Example: {example}")
        if synonyms:
            print(f"🧠 Synonyms: {', '.join(synonyms[:5])}")
        else:
            print("🧠 Synonyms: None found.")
    else:
        print(f"❌ Sorry, '{word}' was not found in the dictionary.")

def main():
    print("📚 Welcome to the Python Dictionary App!")
    while True:
        word = input("\nEnter a word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("👋 Goodbye!")
            break
        get_definition(word)

if __name__ == "__main__":
    main()
