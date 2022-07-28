def Git_init(folder_name):

"""Drive Mount (Colab Notebooks/NLH) and Git Celon
        Git/tyokokur/utilities into Colab/(0)_GitUtils""""

#### Mount Google Drive
from google.colab import drive # import drive from google colab

ROOT = "/content/drive"     # default location for the drive
drive.mount(ROOT)           # we mount the google drive at /content/drive

#### Clone github repository setup
from os.path import join 
# Note: if there are spaces in the path, you need to preceed them with a backslash '\'
MY_GOOGLE_DRIVE_PATH = 'My Drive/Colab Notebooks/(0)_GitUtils'
GIT_USERNAME = 'tyokokur'
GIT_TOKEN = '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'
GIT_REPOSITORY = 'utilities'

PROJECT_PATH = join(ROOT, MY_GOOGLE_DRIVE_PATH)
# It's good to print out the value if you are not sure 
print("PROJECT_PATH: ", PROJECT_PATH)   
# In case we haven't created the folder already; we will create a folder in the project path 
!mkdir "{PROJECT_PATH}"    

GIT_PATH = "https://" + GIT_TOKEN + "@github.com/" + GIT_USERNAME + "/" + GIT_REPOSITORY + ".git"
print("GIT_PATH: ", GIT_PATH)
!git clone "{GIT_PATH}" ./temp      # clone github repository to temp folder
!mv ./temp/colab/* "{PROJECT_PATH}" # move colab files in temp folder to folder defined in project path
!rm -rf ./temp                      # remove all the files/folders in temp folder
#!rsync -aP --exclude=data/ "{PROJECT_PATH}"/*  ./   # use remote sync to copy from google drive to local runtime google colab
                                                    # but exclude data folder
                                                    # https://www.computerhope.com/unix/rsync.htm
%cd /content/drive/My\ Drive/Colab\ Notebooks/"{folder_name}"
