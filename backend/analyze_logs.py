from openai import OpenAI
import os

def analyze_logs(file_path):
    # Lade den API-Schlüssel aus der Umgebung
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)

    # Lese den Inhalt der Logdatei
    with open(file_path, 'r') as file:
        log_text = file.read()

    # Erstelle eine Anfrage an die OpenAI API mit den Logdaten
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an intelligent assistant, skilled in analyzing software logs."},
            {"role": "user", "content": f"Analyze this log and identify any errors: \n{log_text}"}
        ]
    )

    # Überprüfe die Struktur des Antwortobjekts und greife entsprechend darauf zu
    if completion.choices:
        first_choice = completion.choices[0]
        return first_choice.message if first_choice else "No completion found."
    else:
        return "No choices available in completion."

# Beispielverwendung, wenn als Hauptskript ausgeführt
if __name__ == "__main__":
    import sys
    log_file_path = sys.argv[1]  # Erwartet den Pfad zur Logdatei als erstes Argument
    print(analyze_logs(log_file_path))
