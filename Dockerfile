FROM continuumio/miniconda3:4.7.12

RUN conda create --name MIPy python=3.6

RUN conda activate MIPy

WORKDIR /usr/app

ADD https://github.com/blester125/MIPy-Talk-Jan-2-2019/archive/master /usr/app/MIPy.tar.gz
RUN tar xzvf MIPy.tar.gz && \
    cd ./MIPy-Talk-Jan-2-2019-master && \

RUN conda install --file requirements.txt && \
    conda install --file requirements-dev.txt && \
    pip install -e .[test] && \
    pytest \

ENTRYPOINT ["jupyter", "notebook", "scripts/cython-jupyter-example.ipynb"]
