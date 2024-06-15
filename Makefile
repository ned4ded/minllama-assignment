.PHONY: requirements check_and_download

WEIGHTS_URL := "https://www.cs.cmu.edu/~vijayv/stories42M.pt"
WEIGHTS_FILE_NAME := stories42M.pt

default: .PHONY

download_weights: 
	wget $(WEIGHTS_URL) -O $(WEIGHTS_FILE_NAME)

requirements: test_environment
	poetry install

check_and_download:	
	@if [ ! -f "$(WEIGHTS_FILE_NAME)" ]; then \
		echo "No weights found, downloading"; \
		$(MAKE) download_weights;\
	else \
		echo "Has weights, skipping download. You could manually reload weights."; \
	fi
test_environment:
	python test_environment.py