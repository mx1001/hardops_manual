<kbd>Alt</kbd>![header](img/banner.gif)

### Essential Hotkeys

## What is tilda or <kbd>~</kbd>?

![hotkey](img/hotkeys/h13.png)

## HOPS Hotkeys

# <kbd>Q</kbd> / <kbd>Shift</kbd> + <kbd>Q</kbd> - Menu / Pie Menu

These are the core of Hard Ops and are the intended  method for choosing and finding functions for Hard Surface Operations.

![hotkey](img/hotkeys/h4.gif)

# <kbd>Ctrl</kbd> + <kbd>~</kbd> - HOPS Helper

The HOPS helper is a series of helpers for using Blender quickly in fullscreen.

The Helper is used for working most aspects of 3d.

![hotkey](img/hotkeys/h5.gif)

The Hops helper is one of my favorites in Hard Ops and has it's own page.

See [HOPS Helper](helper.md)

# <kbd>Alt</kbd> + <kbd>Shift</kbd> + W hopsTool

see [hopstool](hopsTool.md)

# Dots ([hopstool](hopsTool.md))

Holding ctrl will make dots show in hops tool for a selected object depending on which mods are present.

![hotkey](img/hotkeys/h26.gif)

Dots allow for easy adjustment in the 3d view while hopstool is active.

![hotkey](img/hotkeys/h27.gif)

# View Modifier - Ctrl + Right Click Dot

While in [hopstool](hopsTool.md), Ctrl + right clicking a dot will show the mod in a nice little window. 

![hotkey](img/hotkeys/h28.gif)

# Ctrl + Shift + <kbd>~</kbd> - [Mira](https://github.com/mifth/mifthtools/tree/master/blender/addons/mira_tools/) Helper

**[Mira](https://github.com/mifth/mifthtools/tree/master/blender/addons/mira_tools) Tools must be installed**

Mira Tools has been a favorite tool of mine for the longest. Curve Stretch remains one of my favorite tools and as a result we have added a front end to as well.

![hotkey](img/hotkeys/h12.png)

In this example I will use the hotkey <kbd>Alt</kbd> + <kbd>~</kbd>

![hotkey](img/hotkeys/h13a.png)

![hotkey](img/hotkeys/h14.gif)

# <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd> - Bevel helper

The bevel helper can come in handy for making quick bevel adjustments on the fly.
For this to come up the bevel must already be present.

![hotkey](img/hotkeys/h15.png)

In this example I'll build a shape and then add multiple bevels to adjust in the helper.
![hotkey](img/hotkeys/h20.gif)

The bevel helper will already show up in the mini helper and N panel if bevels are present.

Even though I could adjust the dots I could also use the helper for the multiply divide controls.

# <kbd>Alt</kbd> + <kbd>M</kbd> - Material Menu

The material menu was a happy accident that showed much potential in the click and go workflow of Hard Ops.
This will assign a material to the selection with a list of shaders in the scene.

![hotkey](img/hotkeys/h6.gif)

**NO MATERIALS COME WITH HARD OPS**


# <kbd>Alt</kbd> + <kbd>V</kbd> - Viewport Menu

<kbd>Alt</kbd> + <kbd>V</kbd> has options for simplifying the viewport and is useful for quickly adjusting the viewport or render scene.

![hotkey](img/hotkeys/h7.gif)

# <kbd>Ctrl</kbd> + <kbd>Numpad (-/+//)</kbd> - Boolean Operators

Booltool started a revolution when it showed a quick way to get quick booleans non destructively and without many clicks or hotkeys. Over time the tool evolved far beyond its initial use and is no longer being developed by the same person. So in the end we built a simpler version in HOPS that has the drawing and is more aligned to the workflows utilized in HOPS.

>  Booltool is no longer needed for HOPS. If enabled we will respect its hotkeys and allow its usage alongside Hard Ops but that is not recommended.

When it comes to Hard Ops there is more than one way to perform a boolean operation.

![hotkey](img/hotkeys/h9.gif)

![hotkey](img/hotkeys/h8.gif)

The HOPS Boolean hotkeys are as follows.

- <kbd>Ctrl</kbd> + <kbd>NUMPAD</kbd> Minus - Cut

- <kbd>Ctrl</kbd> + <kbd>NUMPAD</kbd> Plus - Add

- <kbd>Ctrl</kbd> + <kbd>NUMPAD</kbd> Slash - Cslash / Cut and split

[It is also worth mentioning that you can also use hopsTool dots](hopsTool.md) for boolean operations which can also be quick.

![hotkey](img/hotkeys/h21.gif)

# Mirror Tool - (<kbd>Alt</kbd> + <kbd>X</kbd>)

Hard Ops interactive mirror is alt + X. This represents the near final solution in mirroring with Hard Ops and requires no 3rd party plugins. It mirrors on both meshes and curves. It can even mirror meshes across curves.

![hotkey](img/hotkeys/h3.gif)

3 mirrors available

- Modifier / mirrors mesh and bisects it on a mesh level. This makes this optimal for booleans.

- Bisect / useful for symmetry modelling. Not for booleans. Can cause issues in boolean workflows but is optimized for tradititional mirroring pipelines

- Symmetrize / one and done. Symmetrizes to the other side without further issue or interaction needed.

---

## Manual Hotkeys

There are many hotkeys that I set manually in Blender.

# Select Boundary - (<kbd>Shift</kbd> + <kbd>~</kbd>)

![hotkey](img/hotkeys/h1.gif)

Select boundary will convert a selection to the edge perimeter. This can be useful if you need to bevel a boundary and add an inset. This is something I do quite a bit in my work and is essential.

Select Boundary is in the Select Menu at the very top. To set the hotkey I right click and choose to change shortcut.

# Mark Sharp - (<kbd>Ctrl</kbd> + <kbd>~</kbd>)

![hotkey](img/hotkeys/h2.gif)

Marking sharps is essential in a Hard Ops workflow for fixing shading issues without bevelling or using mark ssharp in the edit mode <kbd>Q</kbd> menu. This is something that is only for edit mode. <kbd>Ctrl</kbd> + ~ in Object Mode brings up the Hard Ops Helper.

> Not setting this hotkey keeps <kbd>Ctrl</kbd> + <kbd>~</kbd> as the helper in edit mode.

# Shortest Path - <kbd>D</kbd> / Also <kbd>Ctrl</kbd> + left click by default in 2.8

I am quite happy with this function in blender and it comes in handy for selecting an area between two points. Sometimes when the edge flow is not optimal due to ngons or you want only a partial selection this option is for you.

![hotkey](img/hotkeys/h11.gif)

In the above image I located "shortest path" and right clicked it to set it to D and used it for a partial selection and then used the [Mira Tool](http://blenderartists.org/forum/showthread.php?366107-MiraTools) >> curve stretch to adjust that area. This is just one of the use cases but it's a custom hotkey worth knowing.

---

## Snapping Pies Addon

> [Snapping pies was not made by me. I just ported it to 2.8.](https://raw.githubusercontent.com/mx1001/power_snapping_pies/master/power_snapping_pies.py)

[Save the file](https://raw.githubusercontent.com/mx1001/power_snapping_pies/master/power_snapping_pies.py) as a .py and [install it.](install.md)

![hotkey](img/hotkeys/h23.png)

# Snap Pie - (<kbd>Shift</kbd> + <kbd>S</kbd>)

Object Mode contains options for adjusting origin and snapping the cursor etc.

![hotkey](img/hotkeys/h22.png)

Edit mode has options to set origin to selection which I use quite a bit. This probably my main use of the tool in edit mode.

![hotkey](img/hotkeys/h25.png)

Snapping pies offers options for both object and edit mode for various operations like setting origin to selection or recalculating origin from geometry while also being able retain snap cursor functionality.

![hotkey](img/hotkeys/h24.gif)

To install just [save the file](https://raw.githubusercontent.com/mx1001/power_snapping_pies/master/power_snapping_pies.py) as a .py and [install it.](install.md)
