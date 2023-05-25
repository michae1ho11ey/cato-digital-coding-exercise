FROM alpine:latest

# APK to install Python 3 and script dependencies

COPY ship_lookup.py /ship_lookup.py
CMD ["python", "/ship_lookup.py"]