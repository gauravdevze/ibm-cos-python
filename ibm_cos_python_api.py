import os

import sys

import ibm_boto3

from ibm_botocore.client import Config




folder=sys.argv[1]
print("Folder name is %s",folder)

cos = ibm_boto3.client(service_name='s3',

                       ibm_api_key_id=os.getenv("MY_COS_IBM_KEY_TEMP"),

                       ibm_service_instance_id=os.getenv("MY_SVC_IBM_INST_ID_TEMP"),

                       config=Config(signature_version='oauth'),

                       endpoint_url='https://s3.us.cloud-object-storage.appdomain.cloud')




count=0
file=['ob-1','ob-2','ob-3','ob-4','ob-5','ob-6','ob-7','ob-8','ob-9','ob-10']

for file_to_upload in os.listdir(folder):
        print("Uploading File %s ....",file_to_upload)
        filename = os.path.join(folder, file_to_upload)
        if count > 9:
           break


        try:
                res = cos.upload_file(filename,'pixmedia', file[count])
                count = count + 1

        except Exception as e:

                print(Exception, e)

        else:

                print('File Uploaded')



k=0

print("here")
for key in file:
    try:
        print("here1")
        img=str("image-%s.png"%(k))
        print("Downloading image %s .....",img)
        res=cos.download_file('pixmedia',Key=file[k],Filename=img)
        print("Res is %s",res)
        k = k + 1
    except Exception as e:
        print(Exception, e)
    else:
        print('File Downloaded')


