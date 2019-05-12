FROM python

RUN mkdir -p /app

COPY config/.aws-credentials /root/.aws/credentials

WORKDIR /app

RUN pip3 install awscli --upgrade --user

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir ml

COPY . .

CMD ./run.sh
