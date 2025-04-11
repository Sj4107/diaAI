import torch
import os

model_path = r'D:\diaAI\dia\diabetes\ml_models\tabnet_model.pkl'
cpu_model_path = r'D:\diaAI\dia\diabetes\ml_models\tabnet_model_cpu.pkl'

try:
    # Create a fake CUDA environment
    class FakeCUDA:
        def __getattr__(self, name):
            return None
        def __getitem__(self, key):
            return None
        def __call__(self, *args, **kwargs):
            return self
        def __bool__(self):
            return False

    # Temporarily patch torch.cuda
    original_cuda = torch.cuda
    torch.cuda = FakeCUDA()
    
    # Try loading with a custom unpickler
    import pickle
    class CudaUnpickler(pickle.Unpickler):
        def find_class(self, module, name):
            if module == 'torch.cuda':
                return FakeCUDA()
            return super().find_class(module, name)
    
    with open(model_path, 'rb') as f:
        model = CudaUnpickler(f).load()
    
    # Restore original cuda
    torch.cuda = original_cuda
    
    # Ensure all tensors are on CPU
    if hasattr(model, 'cpu'):
        model = model.cpu()
    
    # Save in CPU-compatible format
    torch.save(model, cpu_model_path)
    
    print("✅ CPU model saved to:", cpu_model_path)

except Exception as e:
    # Restore original cuda if needed
    if 'original_cuda' in locals():
        torch.cuda = original_cuda
    
    print("⚠️ Error:", e)
    import traceback
    traceback.print_exc()