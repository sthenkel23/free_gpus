def loadDrive():
  from google.colab import drive
  drive.mount('/content/drive/')
  

def getDriveLoc( fileLoc ):
  return "/content/drive/My Drive/{}".format( fileLoc )


def getLocalFiles():
    from google.colab import files
    _files = files.upload()
    if len(_files) >0:
       for k,v in _files.items():
         open(k,'wb').write(v)

def setWorkspace( workdir ):
  import sys,os
  _drivedefault = '/content/drive'
  if not workdir:
    workdir='My Drive/'
    print("INFO :: default into the head of your g-drive")
  print("INFO :: Now mounting your g-drive ... ")
  workdir = '{}/{}/{}/'.format(_drivedefault, "My Drive", workdir)
  
  if not os.path.exists( workdir ):
    os.makedirs( workdir )
    print("INFO :: Workspace does not exist... Create workspace {}".format( workdir ) )  
  else:
    os.chdir( workdir )
    print("INFO :: You are now transferred to the existent workspace {}".format( workdir ))
  sys.path.append( workdir )
  return workdir
  