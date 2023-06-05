build:
	docker build -t market-model:0.0.1 .
learn:
	docker run -it --rm --name market-learning -v ./src:/app -v ./data:/data -v ./models:/models market-model:0.0.1 python /app/learn.py
test:
	docker run -it --rm --name market-learning -v ./src:/app -v ./data:/data -v ./models:/models market-model:0.0.1 python /app/test.py
chart:
	docker run -it --rm --name market-learning -v ./src:/app -v ./data:/data market-model:0.0.1 python /app/chart.py
