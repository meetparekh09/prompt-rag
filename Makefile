IMAGE_NAME := prompt-rag-app
CONTAINER_NAME := prompt-rag-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -v $(PWD):/app --name $(CONTAINER_NAME) -it --rm $(IMAGE_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) bash

clean:
	docker rmi -f $(IMAGE_NAME)

