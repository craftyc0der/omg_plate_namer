# Gerardo Lab
## Plates Photo Importer

### Setup Anaconda Environment
```bash
conda env create --file plates.yaml
```
#### or
```bash
conda create --name plates python=3.7.6
conda install -c conda-forge zbarlight
conda install -c anaconda pillow
```

### Start Jupyter Lab
```bash
conda activate plates
export PATH=$HOME/anaconda3/bin:$PATH
python -m ipykernel install --user --name=plates;
jupyter lab
```

### Priors
The assumption here is that there is a folder that contains raw images. Adjacent to that folder should be a csv file with the same name as the folder.

### How to run program from terminal

```bash
$ ls -al
drwxrwxr-x 2 josh josh 28672 Oct 24 13:33 milkweed_foliar_fungal_endophytes
-rw-rw-r-- 1 josh josh 16269 Oct 24 13:35 milkweed_foliar_fungal_endophytes.csv
-rw-rw-r-- 1 josh josh  4876 Oct 25 11:03 plates.py
```

The program is called like this: `python plates.py --help`
`python plates.py -s <source-path> -d <destination-path> -m (files will be moved rather than copied) -f (run without prompt for automated scripting)`

Then, you will call the program like this:
```bash
$ python plates.py -s ./milkweed_foliar_fungal_endophytes -d ./sorted
Source path is ./milkweed_foliar_fungal_endophytes
Destination path is ./sorted
Images will be copied.
Would you like to proceed? (yes|no) yes
./milkweed_foliar_fungal_endophytes/IMG_0863.JPG -> ./sorted/MW209_1__1.jpg
./milkweed_foliar_fungal_endophytes/IMG_0876.JPG -> ./sorted/MW111_1__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0821.JPG -> ./sorted/MW225_2__1.jpg
./milkweed_foliar_fungal_endophytes/IMG_0778.JPG -> ./sorted/MW199_5__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0829.JPG -> ./sorted/MW136_5__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0834.JPG -> ./sorted/MW185_7__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0766.JPG -> ./sorted/MW188_5__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0818.JPG -> ./sorted/MW223_1__1.jpg
./milkweed_foliar_fungal_endophytes/IMG_0857.JPG -> ./sorted/MW100_1__1.jpg
./milkweed_foliar_fungal_endophytes/IMG_0890.JPG -> ./sorted/MW215_3__2.jpg
./milkweed_foliar_fungal_endophytes/IMG_0061.JPG -> ./sorted/MW006_4__1.jpg
./milkweed_foliar_fungal_endophytes/IMG_0769.JPG -> ./sorted/MW199_5__2.jpg
```