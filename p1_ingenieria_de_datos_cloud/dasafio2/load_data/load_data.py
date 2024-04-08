from azure.storage.blob import BlobServiceClient
import os

class LoadData:
    def __init__(self) -> None:
        pass

    def _upload_csv_files_to_azure_blob(self, folder_path, storage_account_name, storage_account_key, container_name):
        # Conectar al servicio de almacenamiento de blobs
        connect_str = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Obtener el cliente del contenedor
        container_client = blob_service_client.get_container_client(container_name)

        # Iterar sobre todos los archivos en la carpeta
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                target_folder = file.split('.')[0]
                if file.endswith('.csv'):
                    # Nombre del archivo en Azure Blob Storage
                    blob_name = os.path.join(target_folder, file)
                    
                    # Ruta completa del archivo local
                    file_path = os.path.join(root, file)

                    # Subir el archivo al contenedor
                    with open(file_path, "rb") as data:
                        container_client.upload_blob(name=blob_name, data=data)

                    print(f"Archivo {blob_name} subido exitosamente a Azure Blob Storage en el contenedor {container_name}.")