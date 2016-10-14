## How To Install Hard Ops
________________

![img](img\smack.gif)

> Using install from file will more than likely **not work**. I would recommend
installing the add-on manually by copying the contents of the zip into the add-on
directory.

Here is where you would locate it on your system. It goes without saying that putting the zip you received in your add ons folder will also not work.

# Windows 10 / 7
>When using Blender a folder is created deeply in your PC for add-ons. Putting it
here instead of the branch you are using ensures the next updates also have it
installed.

C:\Users\ **USERNAME** \AppData\Roaming\Blender Foundation\Blender\ **2.XX** \scripts\addons\HOps

# Mac
>Locate Blender in your applications folder

RMB on the blender.app and select show package contents

# Linux:
>I assume linux users know their PC.

~/.config/blender/ **2.XX** /scripts/addons

__________________________________

Most of this will be assuming Windows is used. So once you open the zip you should
see just one folder.

![image](img/zip_contents.png)

This is what the contents of the zip look like. Its just a folder called HOps.
Which is also the internal codename.

All you do is copy the folder into the add ons folder. Then upon opening Blender
you are able to go into add-ons.

>ctrl + alt + u >> is the hotkey to access use preferences.
You can then search for Ops and you will isolate Hard Ops. From here you can
enable the plugin.

![image](img/installandenable.gif)

Now onto discussing the preferences and setup inside of Hard Ops.

___

## Add-On Tab

![img](img\start1\ad2.png)

The recommended addons will show checkboxes when the supported plugins are present.

This can have issues if the naming is different than what it is looking for.
BoxCutter for example requires the folder is named "BoxCutter"
The namings being searched for are as follows.

- ["BoxCutter"](https://gumroad.com/l/BoxCutter/iamanoperative)
- ["Auto Mirror"](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html)
- ["Mira Tools"](http://blenderartists.org/forum/showthread.php?366107-MiraTools)

This can be an issue to some however it is recommended to just check the folder naming. We are currently looking into improving it but it was intended to be a quick checklist to assist with troubleshooting.

To troubleshoot further you also can run the following command in the scripting area of the scripting tab.

**bpy.context.user_preferences.addons.keys()**

![img](img\start1\chkadd.gif)

This will show a list of all the add ons present. This is how we troubleshoot this area when the plugin detection is not working.
___

## Additional Notes

![img](img\stab.gif)

# Auxillary Addons

There might be a zip file inside of Hard Ops called auxiliary addons.

![img](img\start1\files.png)

This has some of the auxiliary add-ons that are recommended. They are able to be installed by placing the contents of that zip in your add-ons folder similar to Hard Ops or BoxCutter.

![img](img\start1\installing_aux.gif)

# Enable Looptools

![img](img\start1\loop1.gif)

Looptools is a plugin that is already built into Blender. It comes in handy for a variety of things however for Hard Ops it powers the circle tool behavior.

In fact here is how you can make a circle manually using loop tools and vertex bevel.

![](img\start1\circlem.gif)

  - ctrl + shift + b >> vertex bevel
  - w >> looptools >> circle
  - ctrl + tab >> face mode
  - ctrl + x >> dissolve faces
  - ctrl + . >> set origin point to individual
  - e >> alt + s >> e

  That can be a large amount of hotkeys so instead Meshtools Circle exists. Which utilizes looptools.

![](img\start1\circlet.gif)

With circle I can add circle in multifold the speed which I was doing it in the previous image.

[Now you're ready to begin! ](https://www.youtube.com/playlist?list=PL0RqAjByAphGEVeGn9QdPdjk3BLJXu0ho)
