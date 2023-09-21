FROM python:3.11-alpine

COPY app/ /opt/app/

EXPOSE 8000

WORKDIR /opt/app

RUN pip install --upgrade pip && \
    pip install -r .requirement.txt

ENTRYPOINT [ "flask" ]
CMD [ "run" ]
