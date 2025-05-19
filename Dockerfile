FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    apt-get install -y wget && \
    wget https://github.com/allure-framework/allure2/releases/download/2.34.0/allure-2.34.0.tgz && \
    tar -zxvf allure-2.34.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.34.0/bin/allure /usr/bin/allure && \
    rm allure-2.34.0.tgz && \
    apt-get remove -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

VOLUME ["/app/allure-results"]

CMD ["pytest", "--alluredir=allure-results"]