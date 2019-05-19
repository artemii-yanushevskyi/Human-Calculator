hellomake:
	echo 'hi'

clean:
	# recursively remove "__pycache__" files, even if not empty 
	find . -name "__pycache__" -exec rm -r "{}" \; 

test:
	python -m unittest discover -v