FROM python:3.7.4-slim-buster

RUN apt-get update && apt-get install -y gnupg\
    curl apt-utils apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

RUN apt-get update && apt-get install -y unixodbc-dev
RUN apt-get update && apt-get install -y libgssapi-krb5-2

# install SQL Server Python SQL Server connector module - pyodbc
RUN apt-get update && apt-get install python python-pip gcc g++ build-essential -y
RUN pip install pyodbc

# install additional utilities
RUN apt-get update && apt-get install nano vim -y

WORKDIR /sqldatadog
COPY . /sqldatadog

CMD ["python3", "/sqldatadog/select.py"]