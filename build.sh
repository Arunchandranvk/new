docker build -t freeapi .

docker tag freeapi:latest 727516060995.dkr.ecr.us-east-1.amazonaws.com/freeapi:latest

docker push 727516060995.dkr.ecr.us-east-1.amazonaws.com/freeapi:latest