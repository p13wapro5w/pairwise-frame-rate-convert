import pytest
from video import frame_rate_convert as mod

CASES = [
    ("ratio_23976", 'm.frame_ratio(24000, 1001) == approx(23.976, rel=1e-3)'),
    ("ratio_30", 'm.frame_ratio(30, 1) == approx(30.0)'),
    ("motion_sum", 'm.motion_magnitude(1.0, -2.0, 3.0, -4.0) == approx(10.0)'),
    ("occlusion_true", 'm.occlusion_mask(True, False) is True'),
    ("occlusion_false", 'm.occlusion_mask(True, True) is False'),
    ("cut_true", 'm.scene_cut(0.5, 0.3) is True'),
    ("cut_false", 'm.scene_cut(0.2, 0.3) is False'),
    ("align_exact", 'm.align_time(1.0, 60) == approx(1.0)'),
    ("align_round", 'm.align_time(1.01, 60) == approx(1.0166667, rel=1e-3)'),
    ("dedupe_true", 'm.dedupe_frames(1.0, 1.01, 0.02) is True'),
    ("dedupe_false", 'm.dedupe_frames(1.0, 1.10, 0.02) is False'),
    ("low_tex_true", 'm.low_texture_fallback(0.2, 0.5) is True'),
    ("transition_clamp", 'm.transition_alpha(1.5) == approx(1.0)'),
    ("resample_ts", 'm.resample_timestamp(1000, 24, 60) == 2500'),
    ("reset_same", 'm.reset_segment(3) == 3')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
