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
conda install nb_conda
```

### Start Jupyter Lab
```bash
conda activate plates
export PATH=$HOME/anaconda3/bin:$PATH
python -m ipykernel install --user --name=plates;
echo "Use the plates kernel in jupyter!"
jupyter lab
```

### Priors
The assumption here is that there is a folder that contains raw images. Adjacent to that folder should be a csv file with the same name as the folder.

```bash
$ ls -al
drwxrwxr-x 2 josh josh 28672 Oct 24 13:33 milkweed_foliar_fungal_endophytes
-rw-rw-r-- 1 josh josh 16269 Oct 24 13:35 milkweed_foliar_fungal_endophytes.csv
-rw-rw-r-- 1 josh josh  4876 Oct 25 11:03 plates.py
```

CSV contents look like this:
```
photoID,sampleID
100000,MW001_1
100001,MW003_2
100002,MW003_1
100003,MW002_5
100004,MW003_3
100005,MW006_4
```

Image folder contains `jpg` images.
```
$ ls ./milkweed_foliar_fungal_endophytes
IMG_0055.JPG  IMG_0078.JPG  IMG_0753.JPG
```

Images have a `Code-128` barcode and a `QRCode`. The barcode is the photoID. The QRCode is the image series modified (such as week of experiment).

![Example Image](example.jpg?raw=true)
#### The QRCode must be 1 or 2 characters. The barcode should be longer than 5 characters. Both need to have plenty of white space around them to be found by the program.


The program will rename the images as `sampleID__QRCode.jpg`

### How to run program from terminal

The program is called like this:
```bash
$ python plates.py --help
python plates.py -s <source-path> -d <destination-path> -m (files will be moved rather than copied) -f (run without prompt for automated scripting)
```

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