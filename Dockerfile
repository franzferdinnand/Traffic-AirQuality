FROM python:slim

WORKDIR app/

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/addons/commands/entrypoint.sh src/addons/commands/entrypoint.sh

ENTRYPOINT ["src/addons/commands/entrypoint.sh"]