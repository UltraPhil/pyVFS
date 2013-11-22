class VFSBaseError(Exception):
    """Base exception class for VFS errors."""
    pass

class VFSFileSystemError(VFSBaseError):
    """The requested filesystem doesn't exist!
    
    Parameters:
    ===========
    errno : int
        The error number
    msg : string
        The name of the requested filesystem.
    """
    errno = None

    def __init__(self, msg=None):
        self.errno = 100
        if msg is None:
            self.strerror = str(errno)
        else:
            self.strerror = msg

    def __str__(self):
        return self.strerror

    def __repr__(self):
        return "VFSFileSystemError('%s')"%self.strerror
