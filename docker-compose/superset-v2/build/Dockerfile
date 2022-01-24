# https://hub.docker.com/r/apache/superset
FROM apache/superset
# Switching to root to install the required packages
USER root
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead
RUN pip install mysqlclient
# Example: installing a driver to connect to Redshift
# Find which driver you need based on the analytics database
# you want to connect to here:
# https://superset.apache.org/installation.html#database-dependencies
#RUN pip install sqlalchemy-redshift
RUN pip install Authlib
RUN pip install clickhouse-driver>=0.2.0
RUN pip install clickhouse-sqlalchemy>=0.1.6
RUN pip install redis
RUN pip install s3werkzeugcache
# Switching back to using the `superset` user
USER superset
