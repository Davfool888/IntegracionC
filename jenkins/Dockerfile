FROM jenkins/jenkins:lts

# Cambiar a root para instalar dependencias y modificar grupos
USER root

# Crear el grupo docker y agregar jenkins a él
RUN groupadd docker || true && \
    usermod -aG docker jenkins

# Instalar Python 3, pip y venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Instalar Node.js y npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Instalar docker-compose plugin
RUN curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Volver a usuario Jenkins
USER jenkins
