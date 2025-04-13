FROM python:3.10-slim

# Install tesseract and required libraries
RUN apt-get update && \
    apt-get install -y tesseract-ocr libgl1-mesa-glx && \
    pip install --no-cache-dir opencv-python-headless pytesseract numpy fpdf

COPY app.py /code/app.py
WORKDIR /code

CMD ["python", "app.py"]
