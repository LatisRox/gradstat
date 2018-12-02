FROM python:3.6-onbuild

EXPOSE 8050

CMD gunicorn LoanProject:server --log-file - --bind 0.0.0.0:8050