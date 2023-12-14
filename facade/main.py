# main.py

from facade import CompressionFacade

def main():
    facade = CompressionFacade()

    file_to_compress = "example.txt"
    file_to_decompress = "example.zip"

    print("Compressing and Decompressing Using Facade:")
    facade.compress_zip(file_to_compress)
    facade.decompress_zip(file_to_decompress)
    facade.compress_rar(file_to_compress)
    facade.decompress_rar(file_to_decompress)

if __name__ == "__main__":
    main()
