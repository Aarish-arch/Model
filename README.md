# Model

This repository now includes a minimal, dependency-free Python model example.

## Build a model

The `LinearModel` in `model.py` can be trained and used for prediction:

```python
from model import LinearModel

x = [1, 2, 3, 4]
y = [3, 5, 7, 9]  # y = 2x + 1

model = LinearModel()
model.fit(x, y)
print(model.predict([5, 6]))  # [11.0, 13.0]
```

Run tests with:

```bash
python -m unittest -v
```
