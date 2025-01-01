FROM python:3.10
WORKDIR /app
COPY src/app.py /app/
COPY models/model.pkl /app/models/
COPY docrequirements.txt /app/
RUN pip install -r docrequirements.txt
CMD streamlit run app.py