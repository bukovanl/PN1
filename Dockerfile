FROM python:3
ADD getweather.py /
RUN pip install pyowm
CMD ["python3","./getweather.py"]
