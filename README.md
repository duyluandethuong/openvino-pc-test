
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

## Stable Diffusion

```
python3 -m stable_diff --device <device_name>
```

The device_name is the name of detected Pytorch devices.

Tested with device_name = `mps` (for macOS), `cpu`, `cuda`
