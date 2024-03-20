FROM node:18-alpine

WORKDIR /app

COPY public/ /app/
COPY src/ /app/

COPY package*.json ./

RUN npm i && mv node_modules /node_modules

COPY . .
