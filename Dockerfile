FROM alpine:latest

RUN apk add --no-cache python3 pip3
RUN pip3 install requests
COPY ship_lookup.py /ship_lookup.py
CMD ["python3", "/ship_lookup.py"]