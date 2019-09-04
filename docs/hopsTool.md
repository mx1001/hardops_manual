![header](img/banner.gif)

# hopsTool

HardOps version 983 introduces the first active tool of Hard Ops called hopsTool. We intend for this tool to provide a simple ui to assist with modifier management for non destructive modelling in the 3d view.

![hotkey](img/hopstool/h1_1.gif)

When hopsTool is active pressing ctrl will show up dots that can be adjusted for quick manipulation on the fly. Clicking the dot brings up the modifier for fine edit.

![hotkey](img/hopstool/h7.gif)

If boxcutter is not installed the hotkey is alt + shift + W.
![hotkey](img/hopstool/h1.gif)

If boxcutter is installed then hopsTool is swapable with alt + W.
![hotkey](img/hopstool/h2.gif)

# Breaking down the UI

[hopsTool will need the topbar to show.](https://twitter.com/mxeon1001/status/1123820309168177154)
![hotkey](img/hopstool/h3.gif)

- Display - options dictating what shows when ctrl is held.
- hShapes - procedural shapes for users to insert and get started with
- Modifiers - add modifiers on the fly w/ adjustable dots for certain ones
- Misc - mirror is the only option here for now.

You are also able to simplify the topbar.

![hotkey](img/hopstool/h17.gif)

---

# Boolean dots

While hopsTool is active users can select 2 objects and hold ctrl to bring up boolean dots.

- cut
- join
- slice

are available at this time.

![hotkey](img/hopstool/h8.gif)

Boolshapes also get their own dot which is where the view can get cluttered quickly.

Fade distance can be adjusted if needed and booldots can be turned off if they are getting in the way.

![hotkey](img/hopstool/h9.gif)

---

## Non-Destructive stepping

Using the [hopsTool](hopsTool.md) you can stack up bevels easily in the viewport.

![](img/step/l1.png)

There are 3 bevel icons.

- corner bevel (intended for planes and vertice beveling
- chamfer (bevel w/ 1 segment)
- rounded bevel (3 segments default angle 30 / ctrl + click angle 60)

To showcase each in action.

![](img/step/s2s.gif)

In this mode holding ctrl shows modifier dots. LMB clicking one shows the modifier information.

![](img/step/s2.png)

![](img/step/s3s.png)

Levels can be added very quickly this way.

![](img/step/s4s.gif)

Also working this way is possible using the Q menu add modifier system.
A few things to note:

- first bevel can be an angle 30 or 60
- second bevel cannot be an angle 30 or else it will catch the first bevel
- bevels from here on are 60 and above to keep simplicity.

The gif shows me adjusting bevels that aren't showing to set up levels I did moments later. Also the shading was incorrect due to not holding shift as well as ctrl to set it to 60 and not 30. But this is a good example of how the angles can work against you if you aren't mindful.

![](img/step/s5s.gif)

---

# Building from a vert

Collapsing a cube to a vert and using handles to guide spins and then add mirroring, decimation, solidification, and 3 levels of bevels can be a fun way to wrap your head around the process.

![hotkey](img/hopstool/h4.gif)

![hotkey](img/hopstool/h16.gif)

# Try making a tire from a plane.

![hotkey](img/hopstool/h6.gif)

By adding a displace, screw and solidify a rim can be made in short time and be dynamically adjustable.

# Things to know

## The topbar can be simplified
![hotkey](img/hopstool/h5.gif)

## Ctrl + shift clicking dots allow for alternative modification.

Bevel dot adjusts the width but ctrl + shift allows for segment adjust.
The info text up top lets users know whats being adjusted.

![hotkey](img/hopstool/h10.gif)

On screw ctrl + shift left click dragging adjusts the steps in screw

![hotkey](img/hopstool/h11.gif)

Simple deform also gets dots for making large adjustments on the fly.

![hotkey](img/hopstool/h12.gif)

When using hops tool w/ boxcutter and racking bevels the ctrl + add mod behavior adds a mod at 60 degrees which is smoother for going to box city.

![hotkey](img/hopstool/h13.gif)

## The n panel can display your modifier stack so get in there and look at the mods.

![hotkey](img/hopstool/h14.gif)

## If you get confused about how a shape is constructed just mod scroll it.

![hotkey](img/hopstool/h14.gif)
