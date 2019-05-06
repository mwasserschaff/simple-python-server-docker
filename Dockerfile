FROM library/python:3-slim

COPY server.py /

CMD ["python", "/server.py"]