FROM node:20-alpine

WORKDIR /app

COPY web/package.json web/package-lock.json* ./ 
RUN npm install

COPY web/ ./web
WORKDIR /app/web

EXPOSE 3000
CMD ["npm", "start"]
