# Gerardo Lab
## Plates Photo Importer

### Setup Anaconda Environment
```bash
conda env create --file plates.yaml
conda activate plates
```
#### or
```bash
conda create --name plates python=3.7.6
conda activate plates
conda install -c conda-forge zbarlight
conda install -c anaconda pillow
```

### Start Jupyter Lab
```bash
export PATH=$HOME/anaconda3/bin:$PATH
python -m ipykernel install --user --name=plates;
jupyter lab
```