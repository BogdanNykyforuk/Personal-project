FROM amazon/aws-lambda-python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN pip install -r requirements.txt
EXPOSE 80

# Run app.py when the container launches
CMD ["main.handler"]

