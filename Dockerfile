FROM python:3.8 
COPY . .
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
CMD $1