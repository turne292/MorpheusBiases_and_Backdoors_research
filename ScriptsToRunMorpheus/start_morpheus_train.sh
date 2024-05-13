export ITS490_PROJECT_ROOT=/home/dhigley/its490ai
docker run --name morpheus-dev --rm -ti -d --cap-add=sys_nice --runtime=nvidia --gpus=all --net=host -v $ITS490_PROJECT_ROOT/morpheus_data:/workspace/morpheus_data -v /var/run/docker.sock:/var/run/docker.sock nvcr.io/nvidia/morpheus/morpheus:23.03-runtime bash
