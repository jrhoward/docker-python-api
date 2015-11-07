FROM python:2.7.10
MAINTAINER Jason "jrhowd@gmail.com"
COPY requirements.txt /app/
WORKDIR /app
RUN apt-get update && apt-get -y autoremove && \
    apt-get install -y fortune-mod fortunes\
    fortunes-bofh-excuses fortunes-mario && \
    pip install -r requirements.txt
RUN ln -sf /usr/games/fortune /usr/bin/fortune
COPY app.py /app/
COPY ddict /usr/share/games/fortune/
COPY ddict.u8 /usr/share/games/fortune/
COPY ddict.dat /usr/share/games/fortune/
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
