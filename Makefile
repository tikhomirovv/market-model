build:
	docker build -t market-model:0.0.1 .
exec:
	docker run -it --rm --name market-learning -v ./src:/app market-model:0.0.1