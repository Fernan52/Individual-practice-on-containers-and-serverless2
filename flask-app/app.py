from flask import Flask, render_template
import subprocess
import shutil

app = Flask(__name__)

def run_docker(container_name):
    # Check if Docker is installed and available
    if not shutil.which("docker"):
        return "Error: Docker no está disponible en este sistema actualmente."
    
    try:
        # Attempt to run the Docker container and capture output
        result = subprocess.check_output(["docker", "run", container_name], text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        # Provide detailed error output
        return f"Error: No se pudo ejecutar el contenedor '{container_name}'. Detalles: {e.output} (Código: {e.returncode})"

@app.route('/')
def home():
    # Define the containers you want to run
    containers = ["lenguaje-python", "lenguaje-javascript", "lenguaje-java", "lenguaje-ruby", "lenguaje-go"]
    results = {container.split('-')[-1].capitalize(): run_docker(container) for container in containers}
    
    # Render the updated template with results
    return render_template('index.html', results=results)

if __name__ == "__main__":
    # Run the Flask app on all available network interfaces at port 5000
    app.run(host="0.0.0.0", port=5000)
