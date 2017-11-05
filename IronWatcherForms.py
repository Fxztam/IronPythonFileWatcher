#
# Demo FormsFileWatcherPJC: Get File exchanges in directory.
# Watching for file exchanges in the ..\formswatch\\forms directory, change this !
# Adapted from Friedhold Matz, October 2017.
# From origin: http://www.ironpython.info/index.php?title=Watching_the_FileSystem
#
from System.IO         import FileSystemWatcher
from System.Threading  import Thread
import clr 
clr.AddReference('System.Windows.Forms')  

global _switch
watcher = FileSystemWatcher()
watcher.Path = 'C:\\Users\\fmatz\\AppData\\Local\\Temp\\formswatch\\forms'

def readFile(filen):
    f = open(filen, 'r')
    print f.read()
    f.close()

def onChanged(source, event):
    global _switch
    if _switch:       
       readFile(event.FullPath)
       _switch = False
    else:
       _switch = True

if __name__ == '__main__':
    WinForms.MessageBox.Show('Iron Watcher 1 is starting !', 'Watcher on default.') 
    _switch = False
    watcher.Changed += onChanged
    watcher.EnableRaisingEvents = True 
    print '--- Watching for Forms default File Watcher directory (..\\formswatch\\forms) --- \n'  
    # wait for one hour
    Thread.CurrentThread.Join(60 * 1000 * 60)    
    WinForms.MessageBox.Show('The End of Watching here !', 'Watcher on default.') 
