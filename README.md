![Banner](banner.png)

# XTTS-Server-MacOS-Guide
Install xtts-server guide for macOS: https://github.com/daswer123/xtts-api-server && https://docs.sillytavern.app/extensions/xtts/

I put this guide together from my own Mac setup, so I wrote down the pieces my machine needed rather than repeating the upstream docs at the links above. It assumes Homebrew, a zsh shell, and an Apple Silicon machine. That last part is why the Docker route further down builds an arm64 image instead of pulling a ready made one.

# Chromium based browser
use chromium based browsers as other browsers seem to have issues with this.

```
mkdir xtts
cd xtts
mkdir speakers
mkdir output
brew install miniconda
conda init zsh
source ~/.zshrc
conda create -n xtts
conda activate xtts
conda install python=3.10
pip install xtts-api-server pydub
pip install torch==2.1.1 torchaudio==2.1.1 torchvision --index-url https://download.pytorch.org/whl/cu118
python -m xtts_api_server --streaming-mode-improve
```

Platform note: the torch line above uses the cu118 CUDA wheel index, which does not match the macOS and Apple Silicon setup this guide describes. On a Mac that line needs the default torch install instead of the cu118 index. That Mac step was not run in this pass (no Mac test run here), so it is flagged, not rewritten, and the cu118 line is left as written for CUDA machines.

The folders I create at the start of that block are not decoration: speakers and output are where the server expects its speaker files and its generated audio to live, and the last line is the point the whole setup builds toward, starting the server with the improved streaming mode on.

# Docker Build
Need to build for arm64:
```
https://docs.docker.com/engine/install/ (Install Docker Engine)
git clone https://github.com/daswer123/xtts-api-server.git
cd docker
docker build --platform linux/arm64 -t xtts-api-server-arm .
python -m xtts_api_server --streaming-mode --use-cache -ms local -d cpu
```

Route note: the block above builds an arm64 image but its last line starts the host install, not the container, so the Docker route and the host route are mixed here. No container start command is given in this guide, and none was added in this pass because Docker was not run here.
