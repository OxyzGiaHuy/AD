from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LoRAConfig:
    rank: int = 4
    alpha: float = 1.0
    target_blocks: int = 2


def _torch():
    try:
        import torch
        import torch.nn as nn
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for LoRA adapters.") from exc
    return torch, nn


class LoRALinearMixin:
    pass


def make_lora_linear(linear, rank: int, alpha: float):
    torch, nn = _torch()

    class LoRALinear(nn.Module, LoRALinearMixin):
        def __init__(self, base):
            super().__init__()
            self.base = base
            for param in self.base.parameters():
                param.requires_grad_(False)
            self.rank = rank
            self.scale = alpha / max(rank, 1)
            self.lora_a = nn.Linear(base.in_features, rank, bias=False)
            self.lora_b = nn.Linear(rank, base.out_features, bias=False)
            nn.init.kaiming_uniform_(self.lora_a.weight, a=5**0.5)
            nn.init.zeros_(self.lora_b.weight)

        def forward(self, x):
            return self.base(x) + self.scale * self.lora_b(self.lora_a(x))

    return LoRALinear(linear)


def attach_lora_to_dinov2(model, config: LoRAConfig) -> int:
    """Attach LoRA to qkv/proj linear layers in the last DINOv2 blocks.

    Returns the number of replaced linear layers. The function assumes the
    common DINOv2/timm block structure: `model.blocks[-n:].attn.qkv/proj`.
    """
    _, nn = _torch()
    blocks = getattr(model, "blocks", None)
    if blocks is None:
        raise ValueError("DINOv2 model does not expose a `blocks` attribute.")
    replaced = 0
    for block in list(blocks)[-config.target_blocks :]:
        attn = getattr(block, "attn", None)
        if attn is None:
            continue
        for name in ("qkv", "proj"):
            module = getattr(attn, name, None)
            if isinstance(module, nn.Linear):
                setattr(attn, name, make_lora_linear(module, rank=config.rank, alpha=config.alpha))
                replaced += 1
    if replaced == 0:
        raise ValueError("No DINOv2 attention linear layers were replaced by LoRA.")
    return replaced


def count_trainable_parameters(model) -> int:
    return sum(param.numel() for param in model.parameters() if param.requires_grad)
