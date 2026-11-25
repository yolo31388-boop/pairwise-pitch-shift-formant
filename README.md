# pairwise-pitch-shift-formant

## 领域

游戏、图形与多媒体

## 主题

变调与共振峰保持

## 说明

共振峰保持、按采样率定块与相位冻结。

初始状态下 `av/pitch_shift_formant.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
