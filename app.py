import tempfile
from typing import Optional

import gradio as gr
import numpy as np

from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import requests
from os.path import exists

MODEL_NAMES = [
    "belarusian"
]
MODELS = {}

manager = ModelManager()


def download(url, file_name):
    if not exists(file_name):
        print(f"Downloading {file_name}")
        r = requests.get(url, allow_redirects=True)
        with open(file_name, 'wb') as file:
            file.write(r.content)
    else:
        print(f"Found {file_name}. Skipping download...")


for MODEL_NAME in MODEL_NAMES:
    release_number = "0.0.1"
    model_link = f"https://github.com/robinhad/belarusian-tts/releases/download/v{release_number}/model.pth.tar"
    model_config_link = f"https://github.com/robinhad/belarusian-tts/releases/download/v{release_number}/config.json"

    model_path = "model.pth.tar"
    config_path = "config.json"

    download(model_link, model_path)
    download(model_config_link, config_path)

    synthesizer = Synthesizer(
        model_path, config_path, None
    )
    MODELS[MODEL_NAME] = synthesizer


def tts(text: str, model_name: str):
    print(text, model_name)
    synthesizer = MODELS.get(model_name, None)
    if synthesizer is None:
        raise NameError("model not found")
    wavs = synthesizer.tts(text)
    # output = (synthesizer.output_sample_rate, np.array(wavs))
    # return output
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        synthesizer.save_wav(wavs, fp)
        return fp.name


iface = gr.Interface(
    fn=tts,
    inputs=[
        gr.inputs.Textbox(
            label="Input",
            default="Лондан - сталіца Вялікабрытаніі.",
        ),
        gr.inputs.Radio(
            label="Choose TTS model",
            choices=MODEL_NAMES,
        ),
    ],
    outputs=gr.outputs.Audio(label="Output"),
    title="🐸💬Belarusian - Coqui TTS",
    theme="huggingface",
    description="Belarusian TTS using Coqui TTS",
    article="",
)
iface.launch()
