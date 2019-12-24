FROM continuumio/miniconda3:4.7.12

RUN apt-get update && \
    apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*

RUN conda create --name MIPy python=3.6

WORKDIR /usr/app

COPY . .

RUN /bin/bash -c ". activate MIPy && \
    conda install --file requirements.txt && \
    conda install --file requirements-dev.txt && \
    pip install -e .[test] && \
    pytest"

ENTRYPOINT ["./preexec.sh"]
CMD ["python"]
