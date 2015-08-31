FROM python:3-onbuild
EXPOSE 8080
ADD ../ /usr/src/app/
WORKDIR /usr/src/app/
VOLUME /usr/src/app/
CMD [ "python", "./start.py" ]