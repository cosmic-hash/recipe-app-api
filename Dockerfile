FROM python:3.7-alpine
MAINTAINER Sai Gautham

ENV PYTHONUNBUFFERED 1
 # this will run in unbuffered mode which is recommended 
 #when running python within dockett containers 
 #this will not buffer the outputs this prints them directly

COPY ./requirements.txt /requirements.txt
 #this will copy the requirements.txt file to docker requirements.txt
RUN apk add --update --no-cache postgresql-client
# here apk is the package manager comes with alpine and add it and update 
#the registry before we add it
#with no cache to have less no. of files
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
#temporary build dependencies
RUN pip install -r /requirements.txt
 #this will install the requirements using pip
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app
#this creates the empty folder on our docker in th edge called forward slash at this location
#/app
#and then switches to that as the default directory
#and also the application will start at this position /app
#copy will copy over app to there

RUN adduser -D user
USER user
#-D this for only running the other not for anything else



