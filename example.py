# Here are typical usecases I plan to support:

import vfs

try:
    print(v["asdf"]) # This tries to print a non-existent ressource

    # In a nutshell:
    # root by itself does nothing but mounts filesystems
    # filesystems contains files
    # file contains data (bytes)
    # root
    # \-> FS
    #       \-> file
    #           \-> data
    # a File can be: a file (duh), a directory, a pointer


    # ROOT
    ######
    root = vfs.VFS()    # this root will mount filesystems


    # Creating a filesystem
    #######################

    # In memory
    # ---------
    fs = vfs.filesystems.FileSystemMemory(maxsize="1G")
    root.mount('/mem/', fs, mode='rw')

    # On Disk
    # -------
    fd = vfs.filesystems.FileSystemDisk(path="/home/phil")
    root.mount("/disk", fd, mode="ro")

    # raw file
    # --------
    fraw = vfs.filesystems.FileSystemRAW(path="/home/phil/test.bin")
    root.mount("/raw", fraw) #will be rw by default

    # FTP
    # ---
    fftp = vfs.filesystems.FileSystemFTP(url="ftps://host:1234", username="", password="", passive=True, binary=True)
    root.mount("/ftp", fftp)
    # NOTE: a read implies downloading the file, and write uploading.
    # A ls -R will NOT be performed in case of large structure


    # Creating a file
    #################

    # In a FS
    # -------
    f = fs.createfile(path="superdirectory/test.txt")
    f.writelines(["this", "is", "a", "multi lines", "file"])
    # Optionaly: (could be automatic, depends on FS and sync option)
    f.flush()

    # On root device directly
    # ----------------------
    fr = root["/disk/superdirectory/myfile.txt"]
    fr.writeline(b"Please keep your arms and legs inside the train")
    f.flush() # Should be called automagically if fs requires it.


    # Listing files
    # =============
    fs.list() # Will list root of filesystem
    fs.list("sub/folder") # will list a subfolder
    fs.list("sub/folder", recursive=True, columns="size,date,modif", indent=True) # recursively list a folder.

    root["/disk"].list(recursive=True)

    # Deleting a file
    # ===============
    fs.delete("path/to/file/or/folder", recursive=True)

    # Retreiving a file
    ###################
    print(fs.getfile("text.txt"))
    print(root['/mem/text.txt'])    # both lines will output the same content.
    print(f)    # prints file content (== print(f.getcontent()))
    print(repr(f))  #prints more infos 
    
    # commands
    ###############
    # Sometimes, it may be easier to simply send commands
    # Supported commands: LS, MKDIR, TOUCH, GET, PUT , DEL
    root.command("ls /disk")
    root.cmd("mkdir /ftp/well/okay")
    root.cmd("touch /mem/subfolder/filename.txt")
    root.cmd("put /mem/subfolder/filename.txt", content=b'huehuehuehue')
    content = str(root.cmd("get /mem/subfolder/filename.txt"))
    root.cmd("del -r /mem/subfolder")
    # OR ?
    root.cmd(cmdtype.DEL, "/mem/subfolder", options={"recursive": True})


    # Monitor a filesystem
    # --------------------
    # This allows to monitor changes from outside the Python on a filesystem
    def deleteNewFiles(fs, path):
        fs.delete(path, options={"recursive": True})

    root.monitor("/disk/sub/folder", interval=0, trigger=deleteNewFiles) # but could have been the entire FS
    # if interval = 0, then automatic (continuous for supported FS types) or never.
        
except Exception as e:
    print(repr(e))
