import os
import google.generativeai as genai

# Configura la API key desde los 'secrets' de GitHub
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Elige el modelo a utilizar
model = genai.GenerativeModel('gemini-1.5-flash')

# La tarea para nuestro GEM
prompt = "Actúa como un GEM - Redactor Creativo. Dame 3 eslóganes publicitarios para una marca de vino español de alta gama que quiere entrar en el mercado chino."

# Ejecución y resultado
print("🤖 GEM Redactor Creativo contactando a Gemini...")
response = model.generate_content(prompt)
print("✅ ¡Respuesta recibida! Aquí están los resultados:")
print("---")
print(response.text)
print("---")