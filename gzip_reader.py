import zlib


class GzipReader(object):
    def __init__(self, fileobj, blocksize=8192):
        self.fileobj = fileobj
        self.blocksize = blocksize
        self.decompress = zlib.decompressobj(16 + zlib.MAX_WBITS)
        self.data = ""

    def _fill(self, n):
        if self.decompress:
            # read until we have enough bytes in the buffer
            while not n or len(self.data) < n:
                data = self.fileobj.read(self.blocksize)
                if not data:
                    self.data += self.decompress.flush()
                    self.decompress = None # no more data
                    break
                self.data += self.decompress.decompress(data)

    def read(self, n=0):
        self._fill(n)
        if n:
            data = self.data[:n]
            self.data = self.data[n:]
        else:
            data = self.data
            self.data = ""
        return data

    def readline(self):
        # make sure we have an entire line
        while self.decompress and "\n" not in self.data:
            self._fill(len(self.data) + 512)
        i = self.data.find("\n") + 1
        if i <= 0:
            return self.read()
        return self.read(i)

    def readlines(self):
        return list(self)

    def __iter__(self):
        return iter(self.readline, '')
