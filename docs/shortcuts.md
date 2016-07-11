## Hard Ops Hotkeys and Key Setup Tips

> Hard Ops started with the single hotkey of Q and has expanded into much more. I hope explain the hotkeys and the way I work using them.

# Q - Hard Ops menu / Shift + Q - Pie Menu

This menu is the foundation of Hard Ops and is the main way to choose options and operators.

![img](hotkey\h2.gif)

The pie menu no longer has icons due to issues with quickly loading. However there may come a time when these two functions will be alternating via preferences but in the meantime you are able to load both.

The hard ops Q menu also shows different options based off of context. For example if one object is selected. Or more or none.



# Alt + Shift + X/Y/Z - MirrorMirror

> MirrorMirror is integrated into Hard Ops as of Version 8.

With one object selected you can mirror an object across itself. To put it simply: it just adds a mirror modifier to the object. This does not do any bisection to the mesh. That falls under [AutoMirror](http://blenderaddonlist.blogspot.com/2014/07/addon-auto-mirror.html) however we might look into that in the future.

![img](hotkey\h3.gif)

With two objects selected you can mirror one object across another object.

![img](hotkey\h4.gif)

This is normally how I use MirrorMirror. I enjoy the fact that with two objects selected it can populate the mirror modifier with the name of the first object saving on work.

# Ctrl + ~ - Modifier Helper / Material Helper / HOPS Helper

> Modifer helper will display the modifiers currently on the object. The idea was to provide options during full screen working without interruption.

![img](hotkey\h5.gif)

The HOPS helper has multiple sections for other areas like materials and misc as well.

> As of this writing the misc tab doesn't contain anything yet. We may expand upon this in later releases.

# Ctrl + **numpad** - / + / * - Boolean Operations

> When the booltool was created it started a revolution. Before the introduction of the aforementioned hotkeys, using booleans was a complicated and unintuitive process. The creation of the booltool put booleans on the map and made them and intergal part of modelling once again.

With multiple objects selected you can do boolean operations with the following hotkeys.

- ctrl + **numpad** minus / Subtractive Boolean
- ctrl + **numpad** plus / Additive Boolean
- ctrl + **numpad** multiplication / Slice Operation via Cslice

![img](hotkey\h6.gif)

As you can see there is also an F6 menu with options for different boolean behaviors. Those are covered more in depth on the boolean page.

![img](hotkey\h7.gif)

The additive boolean is pretty much the same as the difference boolean except in reverse. However The Cslice is much different.

Cslice is actived via ( ctrl + **numpad** * )

![img](hotkey\h9.gif)

![img](hotkey\h8.gif)
___

## Custom Hotkeys

> This area will discuss hotkeys that I use often but are not related to Hard Ops. These will require you set them up manually by right clicking and choosing to set hotkey.

# D - shortest path

I am quite happy with this function in blender and it comes in handy for selecting an area between two points. Sometimes when the edge flow is not optimal due to ngons or you want only a partial selection this option is for you.

 ![img](hotkey\h1.gif)

 In the above image I located "shortest path" and right clicked it to set it to D and used it for a partial selection and then used the [Mira Tool](http://blenderartists.org/forum/showthread.php?366107-MiraTools) >> curve stretch to adjust that area. This is just one of the use cases but it's a custom hotkey worth knowing.
