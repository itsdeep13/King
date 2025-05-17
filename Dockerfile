FROM sailvessel/ubuntu:latest
WORKDIR /app
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    ffmpeg \
    aria2 \
    mkvtoolnix \
    wget \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m venv /venv
ENV PATH="/usr/local/bin:/venv/bin:$PATH"
COPY master.txt .
RUN /venv/bin/pip install -r master.txt
COPY . .
RUN chmod +x spayee.py
RUN python3 spayee.py
RUN cp Tools/mp4decrypt /usr/local/bin/mp4decrypt && \
    cp Tools/N_m3u8DL-RE /usr/local/bin/N_m3u8DL-RE && \
    cp Tools/appxdl /usr/local/bin/appxdl && \
    cp Tools/hls64 /usr/local/bin/hls64 && \
    chmod +x /usr/local/bin/mp4decrypt /usr/local/bin/N_m3u8DL-RE /usr/local/bin/appxdl /usr/local/bin/hls64
CMD ["python3", "main.py"]