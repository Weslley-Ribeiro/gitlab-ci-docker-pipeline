FROM ubuntu
# Utilizamos uma imagem Ubuntu (ultima disponivel).
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
