FROM node:14

WORKDIR /src/DockerCourse/1_Jumping_In/app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "app.mjs"]
