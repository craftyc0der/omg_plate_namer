import zbarlight
import os 
from PIL import Image
import sys
import getopt

def decode_barcode( file_path ) :
    if os.path.isfile( file_path ) :
        with open(file_path, 'rb') as image_file:
            image = Image.open(image_file)
            image.load()
            codes = zbarlight.scan_codes(['qrcode', 'code128'], image)
            if len(codes) == 2 :
                day = codes[0]
                plate = codes[1]
                if len(day) > 2 :
                    day = codes[1]
                    plate = codes[0]
                day = day.zfill(2)
                return plate.decode("utf-8"), day.decode("utf-8")
    print ('barcode image scan failed [ %s ] is not a file.' % file)

def rename_files( from_path, to_path, move ) :
    if not os.path.exists( to_path ):
        os.makedirs( to_path );
    directory = os.fsencode( from_path )
    for file in os.listdir( directory ) :
        filename = os.fsdecode( file )
        if filename.lower().endswith(".jpg") :
            from_file = from_path + "/" + filename
            plate, day = decode_barcode( from_file )
            to_file = '%s/%s_%s.jpg' % (to_path, plate, day)
            if move:
                # move the file
                os.rename(from_file, to_file)
            else :
                # copy the file
                os.popen('cp %s %s' % (from_file, to_file))
            print ('%s -> %s' % (from_file, to_file))
            
def main(argv):
    source = ''
    destination = ''
    move = False
    force = False
    try:
        opts, args = getopt.getopt(argv,"hs:d:mf",["source=","dest=","move","force"])
    except getopt.GetoptError:
        print ('plates.py -s <source-path> -d <destination-path> -m (files will be moved) -f (run without prompt)')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('plates.py -s <source-path> -d <destination-path> -m (files will be moved) -f (run without prompt)')
            print ('Renames images in <source-path> based on barcodes found in image.')
            sys.exit()
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-d", "--dest"):
            destination = arg
        elif opt in ("-m", "--move"):
            move = True
        elif opt in ("-f", "--force"):
            force = True
    if not force:
        print ('Source path is ' + source)
        print ('Destination path is ' + destination) 
        if move:
            print ('Images will be moved.')
        else:
            print ('Images will be copied.')
    if force:
        proceed = 'yes'
    else:
        proceed = input('Would you like to proceed? (yes|no) ').lower()
    if proceed == 'yes':
        rename_files( from_path=source, to_path=destination, move=move )

if __name__ == "__main__":
    main(sys.argv[1:])