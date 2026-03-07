from flask import Flask, render_template, request, send_from_directory
from ultralytics import YOLO
import os
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO("best.pt")


@app.route("/", methods=["GET", "POST"])
def index():

    image_name = None
    prediction = None
    confidence = None

    if request.method == "POST":

        file = request.files["image"]

        if file.filename != "":

            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)

            results = model(path)
            r = results[0]

            annotated = r.plot()

            output_path = os.path.join(RESULT_FOLDER, filename)
            cv2.imwrite(output_path, annotated)

            image_name = filename

            if len(r.boxes) > 0:

                cls_id = int(r.boxes.cls[0])
                prediction = model.names[cls_id]

                conf = float(r.boxes.conf[0])
                confidence = round(conf * 100, 2)

            else:
                prediction = "Healthy"
                confidence = 100

    return render_template(
        "index.html",
        image=image_name,
        prediction=prediction,
        confidence=confidence
    )


@app.route("/results/<filename>")
def result(filename):
    return send_from_directory(RESULT_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)