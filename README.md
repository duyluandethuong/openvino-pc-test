
# Installation instruction

On Windows: You can use Command Prompt
On MacOS: You can use Terminal, or Visual Studio Code Terminal is fine

Clone the project and `cd` to project root directory.

Create a virtual environment

```
python3 -m venv openvino_env
```

Activate the virtual env

```
source openvino_env/bin/activate
```

Install required tools

```
python3 -m pip install --upgrade pip wheel setuptools
pip3 install -r requirements.txt
```
# Run test

## Read this before you run the scripts
⚠️ For the first time you execute the script, the model will be downloaded and it may takes several minutes depends on your network. Please be patient and let the script finish it work.

⚠️ The execution time only accounts for the time the model is loaded into memory and perform inference. It does not count the time of model downloading.

## Stable Diffusion Test

This script use `stabilityai/stable-diffusion-2-1-base` text-to-image model (hosted on Huggingface) to perform inference.

```
python3 -m stable_diff --device <device_name>
```

The device_name is the name of detected Pytorch devices.

Tested with device_name = `mps` (for macOS), `cpu`, `cuda`

Example:

```
python3 -m stable_diff --device cpu
```

Example result

```
CPU: ARM CPU
Running on device cpu
Loading pipeline components...: 100%|████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:00<00:00, 13.04it/s]
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 17/17 [00:28<00:00,  1.68s/it]
/Users/duyluan/Desktop/pc-cv-test/openvino_env/lib/python3.11/site-packages/diffusers/image_processor.py:97: RuntimeWarning: invalid value encountered in cast
  images = (images * 255).round().astype("uint8")
Device: cpu - Inference time: 31.671626091003418
```