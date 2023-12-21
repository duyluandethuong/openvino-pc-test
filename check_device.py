from openvino.runtime import Core
import torch

def check_device():
    ie = Core()
    devices = ie.available_devices
    
    print('---------OpenVINO device report--------')
    for device in devices:
        device_name = ie.get_property(device, "FULL_DEVICE_NAME")
        print(f"{device}: {device_name}")
        
def check_device_pytorch():
    print('---------PyTorch device report--------')
    if torch.cuda.is_available():
        devices = [torch.cuda.device(i) for i in range(torch.cuda.device_count())]
        for device in devices:
            print(f'{torch.cuda.get_device_name(device)}')
    else:
        print('CUDA is not available')

    if torch.backends.mps.is_available():
        print('MPS is available')
    else:
        print('MPS is not available')

if __name__ == "__main__":
    check_device()
    check_device_pytorch()