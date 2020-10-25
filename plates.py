import zbarlight
import os 
from PIL import Image, ImageEnhance
import sys
import getopt
import csv


def decode_barcode( file_path ) :
    # validates that file_path is for a file (as opposed to a folder)
    if os.path.isfile( file_path ) :
        # read file into variable
        with open(file_path, 'rb') as image_file:
            # load file as image
            image = Image.open(image_file)
            image.load()
            # day is qr code
            day = None
            # plate is barcode
            plate = None
            # extracts qr and barcodes and returns as array
            codes = zbarlight.scan_codes(['qrcode', 'code128'], image)
            # extract latest values for day and plate
            day, plate = extract_codes (codes, day, plate)
            # the 3 following if statments say that if either the qr or barcodes are unreadable
            # enhance more and try again
            if day == None or plate == None :
                enhanced_image = enhance(image, 1.5)
                # enhanced_image.save('test1.5.jpg')
                codes = zbarlight.scan_codes(['qrcode', 'code128'], enhanced_image)
                day, plate = extract_codes (codes, day, plate)
            if day == None or plate == None :
                enhanced_image = enhance(image, 2.0)
                # enhanced_image.save('test2.0.jpg')
                codes = zbarlight.scan_codes(['qrcode', 'code128'], enhanced_image)
                day, plate = extract_codes (codes, day, plate)
            if day == None or plate == None :
                enhanced_image = enhance(image, 2.5)
                # enhanced_image.save('test2.5.jpg')
                codes = zbarlight.scan_codes(['qrcode', 'code128'], enhanced_image)
                day, plate = extract_codes (codes, day, plate)
            # if succesful, output the codes and the fuction is done
            if day != None and plate != None :
                return plate.decode("utf-8"), day.decode("utf-8")
            # if not, when the program runs, the row for the renaming of the image will show the error message below
            # it says that the scan has failed and that it isn't a file.
            print ('barcode image scan failed [ %s ] is not a file.' % image_file.name)
            return None, None

def extract_codes( codes, day, plate ):
    iday = None
    iplate = None
    # if codes an array
    if codes != None:
        # iterates over array codes
        for code in codes:
            # if the code is longer than two digits, that the code is a barcode. Otherwise, it is a qr code
            if len(code) > 2 :
                iplate = code
            else:
                iday = code
    # set day to iday if it has not been set before
    # sme for plate
    if day == None and iday:
        day = iday
    if plate == None and iplate:
        plate = iplate                
    return day, plate
            
# this describes what has to be done to the image to make it easier for the sccanner to read
def enhance( img, magnitude ):
    # it sharpens the image
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.5)
    # it deprives the image of it's color
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0)
    # modifys the brightness it by the amount requested  
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(magnitude)
    # modifys the contrast by the same amount 
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(magnitude)
    return img
# This simply renames the file        
def rename_files( from_path, to_path, move ) :
    # If there isn't any new name for the file, make it possible to rename it
    if not os.path.exists( to_path ):
        os.makedirs( to_path )
    # defines a dictionary
    # add the barcode and new filename from csv to dictionary
    fileDict = {}
    with open(from_path + '.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fileDict[row['photoID']] = row['sampleID']
    # list all files in the path
    directory = os.fsencode( from_path )
    # sends every file through here to become independent of one another
    for file in os.listdir( directory ) :
        filename = os.fsdecode( file )
        # If the file an image, then send the path of the image to the decode_barcode fuction(above)
        if filename.lower().endswith(".jpg") :
            from_file = from_path + "/" + filename
            plate, day = decode_barcode( from_file )
            # if the barcode is known, then 
            if plate != None:
                # if there is a filename in the dictionary (made above), remname the file with it
                try:
                    to_file = '%s/%s__%s.jpg' % (to_path, fileDict[plate], day)
                # if not, just run it with the barcode.
                except KeyError:
                    to_file = '%s/%s__%s.jpg' % (to_path, plate, day)
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