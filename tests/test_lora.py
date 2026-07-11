import pytest

from src.models.lora import LoRAConfig, attach_lora_to_dinov2, count_trainable_parameters


def test_lora_attaches_to_last_attention_blocks():
    torch = pytest.importorskip("torch")
    nn = torch.nn

    class Attn(nn.Module):
        def __init__(self):
            super().__init__()
            self.qkv = nn.Linear(8, 24)
            self.proj = nn.Linear(8, 8)

    class Block(nn.Module):
        def __init__(self):
            super().__init__()
            self.attn = Attn()

    class Model(nn.Module):
        def __init__(self):
            super().__init__()
            self.blocks = nn.ModuleList([Block(), Block(), Block()])

    model = Model()
    replaced = attach_lora_to_dinov2(model, LoRAConfig(rank=2, target_blocks=2))
    assert replaced == 4
    assert hasattr(model.blocks[-1].attn.qkv, "lora_a")
    assert count_trainable_parameters(model) > 0
