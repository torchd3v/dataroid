## Installation
```sh
pip install dataroid
```

## Example Usage
```python3
from dataroid import Bot
import pandas as pd

data = pd.read_csv("shopping.csv")

model = Bot(data)
model.generate(5)
```

## Advanced Usage
```python3
from dataroid import Bot
import pandas as pd

data = pd.read_csv("shopping.csv")

params = {
    'epochs':5,
    'embedding_dim':64,
    'generator_dim':(256,256),
    'discriminator_dim':(256,256),
    'generator_lr':0.0002,
    'generator_decay':1e-06,
    'discriminator_lr':0.0002,
    'discriminator_decay':1e-06
}

model = Bot(data,**params,sampling=True)
model.generate(5)
```

## Dependencies
- [pandas - A Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. ](https://pandas.pydata.org/)
- [ctgan - CTGAN is a collection of Deep Learning based synthetic data generators for single table data, which are able to learn from real data and generate synthetic data with high fidelity.](https://sdv.dev/)

## Citation
*Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, Kalyan Veeramachaneni.* **Modeling Tabular data using Conditional GAN**. NeurIPS, 2019.

```LaTeX
@inproceedings{ctgan,
  title={Modeling Tabular data using Conditional GAN},
  author={Xu, Lei and Skoularidou, Maria and Cuesta-Infante, Alfredo and Veeramachaneni, Kalyan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2019}
}
```