From python

#set working directory INSIDE CONTAINER

WORKDIR /app
#ADD EVERYTHING IN THE PROJECT TO APP

ADD . /app

COPY ./requirement.txt /app/requirement.txt
RUN pip install -r requirement.txt
COPY . /app



