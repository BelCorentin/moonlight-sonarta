# Installation



## Easy install

```
conda create -n sonar python=3.10
conda activate sonar
pip install sonar-space
```

## Manual install

### Clone SONAR

```
git clone git@github.com:facebookresearch/SONAR.git

cd SONAR
```

### Install the dependencies

```
conda create -n sonar python=3.10
pip install --upgrade pip
pip install -e .
```