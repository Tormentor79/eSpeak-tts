from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
def generate_tts():
    texto = request.args.get('text', 'Hola')
    audio_path = "audio.wav"
    
    try:
        # Ejecuta eSpeak NG para generar el archivo WAV en español
        subprocess.run(["espeak-ng", "-v", "es", "-w", audio_path, texto], check=True)
        response = send_file(audio_path, mimetype="audio/wav")
        return response
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/')
def home():
    return "Servidor eSpeak activo para ESP8266"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
