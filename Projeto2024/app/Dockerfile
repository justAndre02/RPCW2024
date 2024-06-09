FROM python
RUN pip install flask
RUN pip install requests
RUN pip install SPARQLWrapper

WORKDIR /app

COPY app.py .
COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]