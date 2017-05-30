![header](img/banner.gif)

### Preferences

After enabling Hard Ops a series of preferences will be shown.

![p1](img\prefs\pref1.gif)

---

### UI Tab

![p2](img\prefs\p2.png)

Below is a description of the following options.

- Modal Scale: determines the mouse distance for movement. Useful for scale modelling or large scale operations. Also located in the misc tab of the HOPS helper.

- Pro Mode: always enable when enabling Hard Ops. This enables all the options and unlocks all the limits on the tools. Without this it is Hard Ops for Kids.

- Right Handed: Symmetry will behave on the right or left side with hard ops and if you work on the opposite side you can change the default behavior without the F6 (only for symmetrize)

- Extra Options: this pref may or may not be shown but enables add on integration with certain tools. If it doesn't show it means it does not apply to you.

- Asset Management Integration - If using AM this will allow their loader in the insert menus.

- [Mira Tools](http://blenderartists.org/forum/showthread.php?366107-MiraTools) Expansion - with Hops 9 we attempted to create a frontend for the curve stretch and curve deform operators that are supported in HOPS. We may expand on it in the future.

---

### Drawing Tab
![p3](img\prefs\p3.png)

The drawing tab contains options that determine how the drawing system of Hard Ops displays.

Enable Tool Overlays: enables HOPS drawing in the 3d viewport. This should always be enabled.

Below are 3 custom themes color.
- Hard Ops (default theme used by myself)
- AR (theme set up by AR)
- Theme Grabber (themes hard ops based off of the theme set under themes)

Theme grabber can be a quick way to get hard ops to be the same as your viewport allowing for some interesting sci fi themed modelling.

![p4](img\prefs\p4.gif)

Display text status and display undefined sstaus are worth explanation here as well.

Display Text Sstatus: shows a text status in the corner letting users know the SStatus of the object.

![p4](img\prefs\p5.gif)

Display Undefined Sstaus: shows the sstatus in the corner even if a mesh is undefined.

There is a logo as well in the 3d view that shows up if the mesh is going through csharp / boolshape / cstep sstatus changes. The placement can be adjusted with the Logo x / y parameters.
![p7](img\prefs\p7.png)

Here you can see the logo changing in the corner as I work with the mesh and various operators.

![p4](img\prefs\p6.gif)

---

### Info Tab

Just info for goofs. Maybe time to update this area.

---

### Keymap

Keymap shows all the hotkeys that are associated via hard coding with HOPS.

![p8](img\prefs\p8.png)

> If you need to remove a hotkey it is recommended to uncheck it at the left instead of clicking the x on the right. That could cause you to permenantly lose the hotkey.

This screen is more for reference than adjustments. The hotkeys can be unpredicatble when edited externally.

---

### Links

![p7](img\prefs\p9.png)

Links contains buttons to assist users with locating documentation. Tutorials and sometimes exclusive content. These links sometimes change between updates and usually contains links for assisting users.

### Add-Ons

![p7](img\prefs\p10.png)

In the creation of Hard Ops there has come many tools that accentuate the workflow or provide essential functions outside the scope of Hard Ops. These options also change periodically depending on support amounts and integration.

>The only external tool required is Looptools which is in blender by default.
   ![p7](img\prefs\p11.gif)

The way the addons are detected is the naming.      

>Running the following line in the script editor of blender will show all enabled add ons and their name in the system. This can help with troubleshooting.    

 **bpy.context.user_preferences.addons.keys()**        

![install](img/install/ins3.gif)        

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

It is recommended to check them out and use them as you see fit or worth.
