import java
from java.io import File

curdir = '.'
pardir = '..' 

def mkdir(dir_name):
    ''' <None> jp_os.mkdir(dir_name)
    mkdir make a new directory in the current path.
    '''
    if not File(dir_name).mkdir():
	raise error, "couldn't make directory"
    

def rm(file):
    ''' <None> jp_os.rm(file)
    rm delete a file or directory in the current path
    '''
    if not File(file).delete():
	raise error, "couldn't delete file or directory"
    

def rename(file, new_file):
    ''' <None> jp_os.rename(file, new_file)
    rename change a file- or directory-name in the current path.
    '''
    if not File(file).renameTo(File(new_file)):
	raise error, "couldn't rename file or directory"
    
    
def pwd():
    ''' <string> jp_os.pwd()
    pwd displays and return the current path.
    For example:
    - my_path = pwd()
    '''
    foo = File(File(path+"/foo").getAbsolutePath())
    print foo.getParent()
    return foo.getParent()
    
def getPath():
    ''' <string> jp_os.getPath()
    getPath return the current path.
    '''
    foo = File(File("foo").getAbsolutePath())
    return foo.getParent()
    


def setPath(new_path):
    ''' <None> jp_os.setPath(new_path)
    change the current path to new_path
    '''
    global path
    path = new_path
    print path


def ls():
    ''' <None> jp_os.ls()
    ls displays all files in the current path.
    '''
    print curdir
    print pardir
    l = File(path).list()
    for file in l:
	if ((java.io.File(file)).isDirectory()):
	    print "%-30s %-20s" %(file+"/", stat(file))
	else:
	    print "%-30s %-20s" %(file, stat(file))


def cd(new_path):
    ''' <None> jp_os.cd(new_path)
    cd change the current directory to new_path.
    '''
    import string
    if (new_path == ".."):
	tmp = string.split(path, "/")
	up_path = string.join(tmp[0:-1], "/")
	setPath(up_path)
    else:
	setPath(path+"/"+new_path)



def stat(file):
    ''' <string> jp_os.stat(file)
    stat get all file infos of a file, the format is:
    readable, writable, size, date
    '''
    file = java.io.File(file)
    readable = file.canRead()
    writeable = file.canWrite()
    d = str(java.util.Date(file.lastModified()))
    date = d[3:16]
    size = file.length().toString()
    result = "%-2s %-2s %-10s %s" %( str(readable),str(writeable),str(size[:-1]),date )
    return result

# init the path
path = getPath()




