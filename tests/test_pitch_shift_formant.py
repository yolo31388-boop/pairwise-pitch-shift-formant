import pytest
import av.pitch_shift_formant as mod

CASES = [
    ("formant_preserve", (1,)),
    ("block_by_rate", (1,)),
    ("pitch_smooth", (1,)),
    ("switch_clear_buffer", (1,)),
    ("shared_f0", (1,)),
    ("pause_freeze_phase", (1,)),
    ("load_audio", (1,)),
    ("analyze", (1,)),
    ("shift", (1,)),
    ("present", (1,)),
    ("validate_pitch", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
