## Hard Ops Instalation     
        
        
1.  Download [Hard Ops](https://gumroad.com/l/hardops/)     
        
2.  Unzip folder to     
        
    global path (we suggest to use that one)        
        
    # Windows 10 / 7        
    >When using Blender a folder is created deeply in your PC for add-ons. Putting it       
    here instead of the branch you are using ensures the next updates also have it      
    installed.      
        
    C:/Users/ **USERNAME** /AppData/Roaming/Blender Foundation/Blender/ **2.XX** /scripts/addons        
        
    # Mac       
    >Locate Blender in your applications folder     
        
    RMB on the blender.app and select show package contents     
        
    # Linux:        
    >I assume linux users know their PC.        
        
    ~/.config/blender/ **2.XX** /scripts/addons     
        
    ..      
3. in blender settings enable the addon     
        
    ![install](..\installation/img/ins1.png)        
        
4. save user settings       
        
    ![install](..\installation/img/ins2.png)        
        
Always save user prefs or they wont be enabled next open.       
        
### Support     
        
Q: I can't install Hard Ops 9!      
        
>Make sure you copied the contents of the zip into the directory mentioned above. Also try reopening blender. Install from file does not work most of the time so manual installation is recommended.       
        
Q: Hard Ops won't enable!       
        
>Try reopening Blender! Also check installation. Hard Ops latest version only works with Blender 2.78 and above. The api changes before will cause issues with old blender.     
        
Q: The prefs panel wont show the add on I have it installed help! Omygerd!      
        
The way the addons are detected is the naming.      
        
>Running the following line in the script editor of blender will show all enabled add ons and their name in the system.     
        
> bpy.context.user_preferences.addons.keys()        
![install](..\installation/img/ins3.gif)        
        
If the naming is not exact this will cause issues. Just rename the .py to resolve the issue.        
        
The naming is as follows.       
        
- [BoxCutter](https://gumroad.com/l/BoxCutter/)     
- [Group Pro](https://gumroad.com/l/GroupPro/)      
- [DECALmachine](https://gumroad.com/l/DECALmachine/)       
- [Mira Tools](http://blenderartists.org/forum/showthread.php?366107-MiraTools)     
- [Batch Operations](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/BatchOperations)        
- [Pipe Nightmare](https://blenderartists.org/forum/showthread.php?414316-Addon-Pipe-Nightmare-0-3-31)      
- [Easy Lattice](http://blenderaddonlist.blogspot.com/2013/10/addon-quick-easy-lattice-object.html)     
- [Auto Mirror](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html)        
        
Also the above texts are hyperlinks to their locations.