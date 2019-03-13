import os, ftplib
from ftplib import FTP

ftp_155 = ['140.116.228.155','geodac_uav','geodac5;4cl4','/GEODAC_UAV/2018/20180709_臺南市七股區青鯤鯓扇形鹽田/1.測繪產品/1.1.Ortho_正射影像(包含附加檔)/20180709_臺南市七股區青鯤鯓扇形鹽田']

def try_(info):
    ftp = FTP(info[0])
    ftp.login(info[1], info[2])
    ftp.encoding='utf-8'
    ftp.cwd(info[3])
    ftp_155 = ftp.nlst(info[3])

    file_list = []
    ftp.retrlines('LIST', lambda x: file_list.append(x.split()))
    
    for info in file_list:
        ls_type, name = info[0], info[-1]
        if not ls_type.startswith('d'):
            with open(name, 'wb') as f:
                ftp.retrbinary('RETR {}'.format(f), f.write)
        
try_(ftp_155)


import ftplib
import os



def _is_ftp_dir(ftp_handle, name, guess_by_extension=True):
    """ simply determines if an item listed on the ftp server is a valid directory or not """

    # if the name has a "." in the fourth to last position, its probably a file extension
    # this is MUCH faster than trying to set every file to a working directory, and will work 99% of time.
    if guess_by_extension is True:
        if len(name) >= 4:
            if name[-4] == '.':
                return False

    original_cwd = ftp_handle.pwd()     # remember the current working directory
    try:
        ftp_handle.cwd(name)            # try to set directory to new name
        ftp_handle.cwd(original_cwd)    # set it back to what it was
        return True
    
    except ftplib.error_perm as e:
        return False
    
    except:
        return False


def _make_parent_dir(fpath):
    """ ensures the parent directory of a filepath exists """
    dirname = os.path.dirname(fpath)
    while not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
            print("created {0}".format(dirname))
        except:
            _make_parent_dir(dirname)


def _download_ftp_file(ftp_handle, name, dest, overwrite):
    """ downloads a single file from an ftp server """
    _make_parent_dir(dest.lstrip("/"))
    if not os.path.exists(dest) or overwrite is True:
        try:
            with open(dest, 'wb') as f:
                ftp_handle.retrbinary("RETR {0}".format(name), f.write)
            print("downloaded: {0}".format(dest))
        except FileNotFoundError:
            print("FAILED: {0}".format(dest))
    else:
        print("already exists: {0}".format(dest))


def _mirror_ftp_dir(ftp_handle, name, overwrite, guess_by_extension):
    """ replicates a directory on an ftp server recursively """
    for item in ftp_handle.nlst(name):
        if _is_ftp_dir(ftp_handle, item, guess_by_extension):
            _mirror_ftp_dir(ftp_handle, item, overwrite, guess_by_extension)
        else:
            _download_ftp_file(ftp_handle, item, item, overwrite)


def download_ftp_tree(ftp_handle, path, destination, overwrite=False, guess_by_extension=True):
    """
    Downloads an entire directory tree from an ftp server to the local destination
    :param ftp_handle: an authenticated ftplib.FTP instance
    :param path: the folder on the ftp server to download
    :param destination: the local directory to store the copied folder
    :param overwrite: set to True to force re-download of all files, even if they appear to exist already
    :param guess_by_extension: It takes a while to explicitly check if every item is a directory or a file.
        if this flag is set to True, it will assume any file ending with a three character extension ".???" is
        a file and not a directory. Set to False if some folders may have a "." in their names -4th position.
    """
    path = path.lstrip("/")
    original_directory = os.getcwd()    # remember working directory before function is executed
    os.chdir(destination)               # change working directory to ftp mirror directory
    _mirror_ftp_dir(ftp_handle, path, overwrite, guess_by_extension)
    os.chdir(original_directory)        # reset working directory to what it was before function exec



# play around here
if __name__ == "__main__":
    import ftplib

    mysite = r""
    username = r""
    password = r""
    remote_dir = r""
    local_dir = r""
    ftp = ftplib.FTP(mysite, username, password)
    download_ftp_tree(ftp, remote_dir, local_dir)