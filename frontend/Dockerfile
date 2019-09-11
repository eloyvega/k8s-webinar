FROM node:10.16.2-alpine

EXPOSE 3000
ENV VUE_APP_TODO_API http://localhost:5000/api
WORKDIR /app
COPY . .
RUN ls -la
RUN npm install
ENTRYPOINT [ "npm", "run", "serve" ]