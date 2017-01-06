## Using The Add-On
___

> Below is an image of the plugin being enabled and configured. The main thing is
to check the addons tab to ensure all required plugins are present. Hard Ops is
able to be used without it however it does affect what options are available.

![gettingstarted](/img\start1\enable_addon.gif)

# UI Tab
___

![UI Tab](\img\start1\ui_tab.png)

- Pro Mode - this enables additional options that will be explained throughout the
guide. Leaving this unchecked is recommended for beginners however enabling it
enables all the options.

- Extra Options - this is a series of options ranging from right handed mirroring
to additional pie menu preferences such as a ghost button and the addition of the
 F6 menu. The F6 pie options is enabled by default. So really extra options is
 just for pie menu users.

- Pie: F6 Option at Top - adds F6 to the top of the pie menu. Enabled by default.

![Pie F6](\img\start1\pieF6.gif)

- Pie: Add Boolean Options - adds boolean options to the pie menu for cases in
which more than 1 mesh is selected.

![Pie Bool](\img\start1\pie_bool.gif)

- Asset Manager Expansion - for those who purchased the asset manager have the
option to allow it to connect to hard ops for easier usage. This options is
considered depreciated and may be changed in future releases.

# Drawing Tab
___

![Dtab](\img\start1\drawing_tab.gif)

- Enable tool overlays - enables the display of the drawing notification system
we use for operators. Csharpen / SSharpen / Cstep / Sstep / Merge / Mirror all
have a notification drawing system to allow you to see what is going on and then
proceed with working.

![](\img\start1\drawing_example.gif)

> Here's an example of the drawing system as of version 8 of Hard Ops.

Below are 3 buttons for themes you can use for Hard Ops.
- Hard Ops - My theme for Hard Ops. The default color system.
- AR - Adrian's Theme for Hard Ops. He uses a much plainer system of display
with his hard ops.
- Themegrabber - My favorite. This one will color Hard Ops according to your
personal theme. I recommend clicking this then saving user settings so the theme
is based on you.

You also can set the colors yourself manually and we have put forth many options
 to customize. The idea was to make this something you can customize and make your
 own.

# Info
___

This area contains just a note from me.

# Keymap Tab
___

This area tells you that Q is the basis of Hard Ops and that is pretty much it there.

\addons\HOps\keymap.py

>In the rare event you need to change the keymap you can drag the keymap.py file
into a text editor and edit the hotkey. Or use the button like the following gif.

![](\img\start1\keymap_edit.gif)

The hotkeys as of this writing are.

- Q - Hard Ops Menu
- Shift + Q - Hard Ops Pie Menu (may be changed in the future)
- Ctrl + ~ - Modifier/Material/Misc Helper



# Links / Help Tab
___
This area contains links to different areas.

![](\img\start1\links.png)

Clicking these will take you to the respective pages.

# Add Ons Tab
___

Hard Ops has become great due to the support of many great tools already existing
that are used to minimize certain tasks. Clicking these buttons will link you to
downloading them.

![](\img\start1\addontab.png)

# These plugins are highly recommended

-  [BoxCutter](https://gumroad.com/l/BoxCutter#) - is a separate plugin to Hard
Ops created by AR and is a secondary project focusing on just cutting alone. I
was not the creator of this project and therefore I was unable to add it
into Hard Ops.

- [Mira Tools](http://blenderartists.org/forum/showthread.php?366107-MiraTools) -
Mira Tools is a great too for managing lines of complicated points via curve based
interpolation. This hosts a plethora of immensely useful tools and is worth
checking into on its own.

# These plugins are not required but are recommended. They dont get checkboxes.

- [Batch Operations](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/3D_interaction/BatchOperations) -
Batch Operations is a one stop shop for managing multiple objects worth of modifiers, materials,
groups, and more. This is another tool that should be default in Blender but is
worth looking into just on it's own. Not to mention the creator has assisted our team
with Boxcutter and many other fine contributions.

- [AutoMirror](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html) -
Lapineige is the creator of this fine tool and is just the finest mirroring solutions. My
favorite aspect of this behavior is the bisect and deletion of one half in order to set up the mirroring.
This has been integrated under meshtools for quick access. This is one of my favorite tools.
However all of these tools are my favorites. Hence my efforts to put them together.

- [EasyLattice](http://blenderaddonlist.blogspot.com/2013/10/addon-quick-easy-lattice-object.html) -
Lattices are not the easiest thing to add to objects. This tools makes lattice application as easy as it would be to add a booltool.

- [Blender Updater](https://github.com/tobkum/BlenderUpdater/releases/tag/0.3) -
This is for windows users. Its just a quick updater for Blender. I love it. This is not an addon.
This is an application.

- [Edge Equalize](https://github.com/kroopson/blenderedgeequalize/blob/master/mesh_edge_equalize_operator.py) -
This is just an add on for equalizing edges. It has it's uses. I have come to enjoy it and
recommend it as well.

The rest of these links also point to their respective pages and provide links to acquiring them.
Having these present in hard ops will make the tools even better and we seek to support even more.
When it comes to making tools it became apparent that investing in remaking the wheel
when one already exists is less than optimal in the scheme of things.
