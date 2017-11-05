from System.IO         import FileSystemWatcher
from System.Threading  import Thread

# From origin: http://www.ironpython.info/index.php?title=Watching_the_FileSystem
# This File Watcher Service is watching for file exchanges in the ..\formswatch\\forms directory.
# F.Matz October 2017.

import clr 
clr.AddReference('System.Windows.Forms') 
import System.Windows.Forms as WinForms 

global _switch
watcher = FileSystemWatcher()
watcher.Path = 'C:\\Users\\fmatz\\AppData\\Local\\Temp\\formswatch\\forms'

def readFile(filen):
    f = open(filen, 'r')
    print f.read()
    f.close()

def onCreated(source, event):
    print 'Created:', event.ChangeType, event.FullPath

def onChanged(source, event):
    global _switch
    if _switch:       
       #print 'Changed:', event.ChangeType, event.FullPath
       readFile(event.FullPath)
       _switch = False
    else:
       _switch = True

def onRenamed(source, event):
    print 'Renamed:', event.OldFullPath, event.FullPath

if __name__ == '__main__':

    WinForms.MessageBox.Show('Watcher 1 is starting', 'Watcher on default.') 

    _switch = False
    watcher.Changed += onChanged
    #watcher.Created += onChanged
    #watcher.Deleted += onChanged
    #watcher.Renamed += onRenamed   
    watcher.EnableRaisingEvents = True 
    print '--- Watching for Forms default File Watcher directory (..\\formswatch\\forms) --- \n'
    # wait for an hour
    Thread.CurrentThread.Join(60 * 1000 * 60)
    
    WinForms.MessageBox.Show('The End of Watching here !', 'Watcher on default.') 

#Thread.Sleep(60 * 1000 * 60)
# http://www.ironpython.info/index.php?title=Watching_the_FileSystem

