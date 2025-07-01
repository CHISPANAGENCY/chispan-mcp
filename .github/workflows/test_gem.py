import os
import google.generativeai as genai

# --- Configuración ---
# El script leerá la clave secreta que guardamos en GitHub
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Elige el modelo a utilizar
model = genai.GenerativeModel('gemini-1.5-flash')

# --- La Tarea del GEM ---
# Este es el "briefing" o la orden que le damos a la IA
prompt = "Actúa como un GEM - Redactor Creativo. Dame 3 eslóganes publicitarios para una marca de vino español de alta gama que quiere entrar en el mercado chino."

# --- Ejecución y Resultado ---
print("🤖 GEM Redactor Creativo contactando a Gemini...")
response = model.generate_content(prompt)
print("✅ ¡Respuesta recibida! Aquí están los resultados:")
print("---")
print(response.text)
print("---")