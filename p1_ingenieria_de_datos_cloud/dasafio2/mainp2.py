from load_data.load_data import LoadData

def main():
    load_data = LoadData()
    # Datos de la cuenta de almacenamiento
    storage_account_name = input("ingrese su storage_account_name: ")
    storage_account_key = input("ingrese su storage_account_key: ")

    # Nombre del contenedor en Azure Blob Storage
    container_name = "rawdata"

    # Ruta local del archivo que deseas subir
    file_path = "C:/Users/edwin/Documents/Repos/DataEngTestGlobalMVM/p1_ingenieria_de_datos_cloud/desafio1/data_resources"

    # Subir el archivo al contenedor de Azure Blob Storage
    load_data._upload_csv_files_to_azure_blob(file_path, storage_account_name, storage_account_key, container_name)


if __name__ == "__main__":
    main()