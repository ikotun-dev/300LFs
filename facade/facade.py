# facade.py

from compression.zip_compressor import ZipCompressor
from compression.rar_compressor import RarCompressor

class CompressionFacade:
    def __init__(self):
        self.zip_compressor = ZipCompressor()
        self.rar_compressor = RarCompressor()

    def compress_zip(self, file):
        self.zip_compressor.compress(file)

    def decompress_zip(self, file):
        self.zip_compressor.decompress(file)

    def compress_rar(self, file):
        self.rar_compressor.compress(file)

    def decompress_rar(self, file):
        self.rar_compressor.decompress(file)


