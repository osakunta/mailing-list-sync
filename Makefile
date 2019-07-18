NAME   := osakunta/mailing-list-sync
TAG    := $$(git log -1 --pretty=%h)
IMAGE  := ${NAME}:${TAG}
LATEST := ${NAME}:latest
EXEC   := mailing-list-sync

docker-build:
	sudo docker build -t ${IMAGE} .
	sudo docker tag ${IMAGE} ${LATEST}

docker-run:
	sudo docker run -it --name ${EXEC} ${LATEST}

docker-rm:
	sudo docker rm ${EXEC}

docker-push:
	sudo docker push ${NAME}

docker-bash:
	sudo docker exec -it ${EXEC} /bin/sh

run:
	python -m src

test:
	ENV=test python -m unittest

coverage:
	ENV=test coverage run -m unittest

coverage-upload:
	ENV=test coverage run -m unittest
	coverage xml
	python-codacy-coverage -r coverage.xml
