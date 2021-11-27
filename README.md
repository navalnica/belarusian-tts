---
title: "Belarusian TTS"
emoji: 🐸
colorFrom: green
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# Belarusian TTS 📢🤖
Belarusian TTS (text-to-speech) using Coqui TTS.

Trained on [Belarusian language corpus](https://knihi.com/none/Korpus_bielaruskaha_maulennia_dla_trenirouki_niejronnych_sietak_zip.html).  

Link to online demo -> [https://huggingface.co/spaces/robinhad/belarusian-tts](https://huggingface.co/spaces/robinhad/belarusian-tts)

# Example

https://user-images.githubusercontent.com/5759207/143675901-f35dd351-3e18-421a-8283-60bfbf1c6b42.mp4

# How to use :
1. `pip install -r requirements.txt`.
2. Download model from "Releases" tab.
3. Launch as one-time command:  
```
tts --text "Text for TTS" \
    --model_path path/to/model.pth.tar \
    --config_path path/to/config.json \
    --out_path folder/to/save/output.wav
```
or alternatively launch web server using:
```
tts-server --model_path path/to/model.pth.tar \
    --config_path path/to/config.json
```

# How to train:
1. Refer to ["Nervous beginner guide"](https://tts.readthedocs.io/en/latest/tutorial_for_nervous_beginners.html) in Coqui TTS docs.
2. Instead of provided `config.json` use one from this repo.


# Attribution
Code for `app.py` taken from https://huggingface.co/spaces/julien-c/coqui
