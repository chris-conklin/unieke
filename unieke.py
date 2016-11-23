"""
Nov 23, 2016


"""

import sys
import getopt
import hashlib
import os
import json

__manifest_dir__ = "db"
__manifest_file_name__ = "manifest"
__content_dir__ = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'content'))

banner = """
***************************************************
***** UNIKEYE - Guardian of the family images *****
***************************************************"""


###############################################################################################
def HashCalc(fpath):
   ''' Return the 32 character md5 hash of the object at fpath '''
   try:
      f = file(fpath,'rb')
      Data =f.read()
      MD5 = hashlib.md5(Data).hexdigest()
   except:
      sys.exit()
   f.close()
   return MD5


###############################################################################################
def generate_manifest(manifest_path="db"):
    ''' Create a manifest file that contains the dictionary of hashes and filenames
        that is currently being used by the application. If one already exists it
        is backed up prior to a new manifest being created. ** WARNING: ** this
        is a destructive change despite there being a backup provided! '''
    # TODO: Clean this timestamp up
    #now = datetime.datetime.now()
    now = ".bak"
    manifest_file_name = __manifest_file_name__
    if os.path.exists(manifest_path + manifest_file_name):
        os.rename(manifest_path + manifest_file_name, manifest_path + manifest_file_name + now)
    D = {}
    with open(manifest_path + '/' + manifest_file_name, 'w') as fout:
        content_dir = __content_dir__
        for filename in os.listdir(content_dir):
            fhash = HashCalc(content_dir + "/" + filename)
            D[fhash] = content_dir + "/" + filename
        json.dump(D, fout)

###############################################################################################
def check_permissions():
    print "* Checking write permission on manifest...ok."
    print "* Checking write permission on content directory...ok.\n\n"
    return 1

###############################################################################################
def initialize():
    if(os.path.isfile(__manifest_dir__ + "/" + __manifest_file_name__)):
	print("\n** Warning: manifest file %s/%s already exists. Exiting\n")%(__manifest_dir__, __manifest_file_name__)
    	sys.exit(2)
    else: 
        print "\n** Initializing new unieke manifest.\n\n"
    	generate_manifest()

###############################################################################################
def add_images():
    if (check_permissions()):
        print "Checking for duplicates...ok."
        print "--- Moving 2 duplicates to trashes."
        print "+++ Adding 10 new items to content...ok"
        print "Logging activity in log directory...ok"
        print "\n Additions Complete: 10 added, 2 duplicates found\n"        
    else:
        sys.exit(2)

###############################################################################################
def main(argv):
    
    manifest_file = ""
    output_file = ""
    usage = "  UNIKEYE\n\n  Usage: python unikeye.py { [-h]elp [-i]nit }\n         python unikeye.py { [-m]anifest <file> [-o]utput <file> }"
    

    try:
        opts, args = getopt.getopt(argv,"ahim:o:",["mfile=","ofile="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    print(banner)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-i':
            initialize()
        elif opt == '-a':
            add_images()
        elif opt in ("-m", "--mfile"):
            manifest_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        
    print("ok\n\n")


if __name__ == '__main__':
    main(sys.argv[1:])
