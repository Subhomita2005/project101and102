import dropbox 
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
      
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(), file_to) 

def main():
    access_token = 'aIfmLXDhUJ4AAAAAAAAAAWUDHdbOQI7FS9T72AsTVLY4gApZcHeC_awg9aYc5GvB'
    transferData = TransferData(access_token)

    file_from = 'sample1.txt'
    file_to = '/test_dropbox/sample1.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()