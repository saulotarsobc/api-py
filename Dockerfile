# Utiliza a imagem oficial do Python baseada no Alpine
FROM python:3.9-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Define o comando padrão para execução do contêiner
CMD ["flask", "run", "--host=0.0.0.0"]
