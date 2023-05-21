from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_account_sas, AccountSasPermissions, ResourceTypes,AccountSasServices
from django.http import HttpResponse
import os
from dotenv import load_dotenv
load_dotenv()

# Get the Azure Storage account name and key from environment variables
account_name = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
account_key = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)


def get_url(blob):
    sas_token = create_account_sas()
    
    container_name = os.getenv('CONTAINER_NAME')
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob)
    
    return blob_client.url


def create_account_sas():
    # Set the SAS token options
    expiry_time = datetime.utcnow() + timedelta(minutes=10)  # 10 minutes from now
    permissions = AccountSasPermissions(read=True, write=True, delete=True, list=True)
    resource_types = ResourceTypes(service=True, container=True, object=True)
    services = AccountSasServices(b=True, q=True, t=True, f=True)
    
    # Generate the SAS token
    sas_token = generate_account_sas(
        account_name=account_name,
        account_key=account_key,
        resource_types=resource_types,
        permissions=permissions,
        services=services,
        start=datetime.utcnow(),
        expiry=expiry_time,
    )
    
    return sas_token


def upload(file, path):
    sas_token = create_account_sas()
    
    container_name = os.getenv('CONTAINER_NAME')
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob=file)
    
    with open(path, "rb") as data:
        blob_client.upload_blob(data)
    
    return HttpResponse("File uploaded successfully")


def add(request):
    if request.method == 'POST':
        # Retrieve the form data
        name = request.POST.get('CaseStudyName')
        account = request.POST.get('Account')
        vertical = request.POST.get('Vertical')
        solution = request.POST.get('SolutionName')
        sof = request.POST.get('ServiceOfferingMapping')
        status = request.POST.get('Status')
        dep = request.POST.get('Dependency')
        remarks = request.POST.get('Remarks')
        meta = request.POST.get('MetaData')
        FileName = request.POST.get('FileName')
        rating = request.POST.get('Rating')
        
        if 'File' in request.FILES:
            file = request.FILES['File']
            file_name = file.name
            file_path = file.temporary_file_path() if hasattr(file, 'temporary_file_path') else ''
            upload(file_name, file_path)
            url = get_url(file_name)
            # Process or save the file and URL as needed
        
        return HttpResponse("added")
    
    return HttpResponse("Invalid request method")
