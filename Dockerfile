FROM python:3.7-alpine

RUN mkdir /LANBook
COPY . /LANBook
WORKDIR /LANBook
RUN pip3 install -r requrements.txt
EXPOSE 5000
ENTRYPOINT ["python", "."]



