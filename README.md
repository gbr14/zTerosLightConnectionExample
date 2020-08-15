# zTerosLightConnectionExample

zTerosLightConnectionExample is a python example for connecting to a zTeros Light instance and aims to assist developers create applications using our API.

## What is zTeros Light
zTeros Light is a REST API which offers the encryption of "Records" (data, it can be anything, well anything encoded as a string) using a system where each record is uniquely encrypted under its own key, using a transparent Key Management system.   
For more information please see [our website](https://gbr14.com/gbr14-products/)  

## Prerequisites
* python3  
* a zTeros Light installation (Link to follow)  

## Example workflow
* Generate a record  
```
    python3 EncClientGenerateRecord.py --Address 192.168.0.1:8080  
    {"RecordUID": "9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf"}  
    (Use the generated RecordUID for the below commands, this is just an example)  
```
* Update record with a file to encrypt  
```
    python3 EncClientGenerateRecord.py --Address 192.168.0.1:8080 --UID 9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf --File sample-test-file.json  
    { "Completed": "True", "RecordUID": "9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf"}  
```
* Retrieve the record (and save it as a file)  
```
    python3 EncClientGenerateRecord.py --Address 192.168.0.1:8080 --UID 9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf --File Outfile.json  
    (Nothing is printed from this command, but outfile.json should have been created and should be identical to sample-test-file.json)  
```
* Delete the record  
```
    python3 EncClientGenerateRecord.py --Address 192.168.0.1:8080 --UID 9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf  
    { "Completed": "True", "RecordUID": "9bb7RcIRWD6UUy3pxmnciTA2AhkA6WIZ~m5ZSQ_rHGR6C1P3Yt9UIg5Hzq8lAhkAzCmYA6EiDaz_QrmlC1ya4jnZA7RvF8Gf"}  
```
