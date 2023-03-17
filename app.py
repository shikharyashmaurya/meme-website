from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Get a list of all jpg images in the static folder
    images = os.listdir("static")
    images = [img for img in images if img.endswith(".jpg")]

    # Pick a random jpg image from the list
    random_image = random.choice(images)

    # Render the index.html template and pass in the random image filename
    return render_template("index.html", random_image=random_image)

if __name__ == "__main__":
    app.run()
