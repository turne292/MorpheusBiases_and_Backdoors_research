export ITS490_PROJECT_ROOT=/home/dhigley/its490ai
docker run --name triton -d -ti --gpus=all --restart=unless-stopped -p8000:8000 -p8001:8001 -p8002:8002 -v $ITS490_PROJECT_ROOT/Morpheus/models:/models nvcr.io/nvidia/tritonserver:22.08-py3 tritonserver --model-repository=/models/triton-model-repo --exit-on-error=false --log-info=true --strict-readiness=false --disable-auto-complete-config
