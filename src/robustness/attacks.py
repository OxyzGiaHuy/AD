from __future__ import annotations


def parse_epsilon(value: str | float) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    if "/" in value:
        num, den = value.split("/", 1)
        return float(num) / float(den)
    return float(value)


def fgsm_attack(images, labels, model, epsilon: float):
    """Torch FGSM hook for image-space robustness experiments.

    The actual differentiable path depends on the DINOv2/HeadPCA torch training
    implementation. This function is intentionally explicit about that contract
    instead of silently producing invalid attacks.
    """
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for FGSM.") from exc
    if not hasattr(model, "loss_on_images"):
        raise NotImplementedError("Model must expose loss_on_images(images, labels) for FGSM.")
    images = images.detach().clone().requires_grad_(True)
    loss = model.loss_on_images(images, labels)
    loss.backward()
    return torch.clamp(images + epsilon * images.grad.sign(), 0.0, 1.0).detach()

