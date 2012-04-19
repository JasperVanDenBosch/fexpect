import os, shutil

if len(sys.argv)<2:
    sys.exit('No keyword given to cleanup.')
keyword = sys.argv[1]

if os.path.exists('env'):
    shutil.rmtree('env')

for f in os.listdir(os.getcwd()):
    if keyword in f:
        print('Cleaning up '+f)
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)
