from .vfsexceptions import *


class VFS(object):
    """
    VFS main class.  This class represents a file system in an object.  You can mount filesystems to it.
    The format for mounting filesystem is a standard URI:
    type:path?params=value&param2=value2
    i.e.
    /home/user?readonly=True
    file:/home/user/file.bin?readonly=True&encoding=UTF-8
    ftp://myuser@myserver:990?passive=True&ssl=True
    http://www.example.com:8080/exampleFile?format=zip&readonly=True
    """
    __mounts = dict()   # mounts are a dictionary of form: mountpoint => FS pointer


    def __init__(self):
        #return super().__init__()
        pass

    def __getitem__(self, item):
        try:
            return self.__mounts[item]
        except :
            raise VFSFileSystemError("FS %s is non-existent" % item)

    def mount(self, mountpoint, filesystem, mode="rw"):
        pass

    def umount(self, mountpoint):
        pass
    def getFileSystem(self, mountpoint):
        pass
    def mounts(self):
        return self.__mounts.keys()
