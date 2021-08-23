import subprocess
import requests
import tarfile
import os

class SteamCMD():
    def __init__(self,dsm):
        self.dsm=dsm

    def check_for_steamcmd(self):
        if self.dsm.platform=='linux':
            return os.path.isfile(os.path.join(self.path,'linux32','steamcmd'))

        
    def get_steamcmd(self):
    
        if not os.path.exists(self.dsm.path_steamcmd):
            os.mkdir(self.dsm.path_steamcmd)
            
        if self.dsm.platform=='linux':
            result=requests.get("https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz")
            with open(os.path.join(self.dsm.path_steamcmd,'steamcmd_linux.tar.gz'),'wb') as o:
                o.write(result.content)
                o.close()
            tar=tarfile.open(os.path.join(self.dsm.path_steamcmd,'steamcmd_linux.tar.gz'))
            tar.extractall(self.dsm.path_steamcmd)
            tar.close()
        else:
            print('ERROR: Sorry, but we only have linux support')
            return
            
    def DST_download(self):
        if not os.path.exists(self.dsm.path_dstds):
            os.mkdir(self.path_dstds)
    
        if self.dsm.platform=='linux':
            steamcmd_executable=os.path.join(self.path,"steamcmd.sh")
            dst_path=5
        #/home/gustavo/Extra/DontStarve/DedicatedServer/steamcmd_linux/steamcmd.sh +@ShutdownOnFailedCommand 1 +@NoPromptForPassword 1 +login anonymous +force_install_dir /home/gustavo/Extra/DontStarve/DedicatedServer/DST +app_update 343050 validate +quit
        pass
    
    def DST_update(self):
        pass
            
            

