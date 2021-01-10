import cv2
import dropbox
import time
import random

startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(1,cv2.CAP_DSHOW)
    result=True
    while (result) :
        ret,frame=videoCaptureObject.read()
        print(frame)
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    return imageName
    print("snapshot taken")    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = "yN1GJmNdC3cAAAAAAAAAAddo1eikzYYGa99fbOutScx98vHsOj7ZJ3UDFAmo2NRW"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - startTime) >= 5):
            name = takeSnapshot()
            upload_file(name)

main()    
  
