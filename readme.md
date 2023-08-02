1. `conda create VENV_NAME python=3.10`
2. `conda activate VENV_NAME`
2. `conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia`
3. `conda install openai`
4. `conda install transformers`

```commandline
# use anaconda pls
conda create VENV_NAME python=3.10
conda activate VENV_NAME
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install openai
conda install transformers

# c19 whisper
pip install openai-whisper
pip install setuptools-rust

# c20 azure
pip install azure-cognitiveservices-speech
pip install soundfile
pip install git+https://github.com/huggingface/transformers sentencepiece datasets

# c22 transformer stable diffusion
pip install diffusers --upgrade
pip install invisible-watermark\>=0.2.0
pip install accelerate
pip install opencv-python
```