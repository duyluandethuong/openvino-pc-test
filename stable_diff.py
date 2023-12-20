from openvino.runtime import Core
from diffusers import StableDiffusionPipeline
import gc
import time
import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--device", default=None, type=str)

args = parser.parse_args()

def check_device():
    ie = Core()
    devices = ie.available_devices

    for device in devices:
        device_name = ie.get_property(device, "FULL_DEVICE_NAME")
        print(f"{device}: {device_name}")
        
def run_stable_diffusion(run_on_device=None):

    # Set device
    if run_on_device is None:
        device = (
            "mps"
            if torch.backends.mps.is_available()
            else "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )
    else:
        device = run_on_device
    
    print(f'Running on device {device}')

    model_id = "stabilityai/stable-diffusion-2-1-base"
    pipe = StableDiffusionPipeline.from_pretrained(model_id).to(device)
    pipe.save_pretrained("./stabilityai_cpu")
    prompt = "A red car on a sunset beach with some tropical trees on the left"
    start_time = time.time()
    output_cpu = pipe(prompt, num_inference_steps=17).images[0]
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Device: {device} - Inference time: {elapsed_time}')
    
    output_cpu.save("img_result/image_cpu.png")
    output_cpu

    del pipe
    gc.collect()

if __name__ == "__main__":
    check_device()
    run_stable_diffusion(run_on_device=args.device)