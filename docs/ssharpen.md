![header](img/banner.gif)

# Sharpen overview

<iframe width="560" height="315" src="https://www.youtube.com/embed/cz5BgWqGYLA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sharpen does the following things.

- set shading to smooth from flat
- enables autosmooth / sets angle to 30/45/60
- marks edges as crease / sharp / seam / bevel weight based off of sharp parameter.

For more information on how ssharpen came about see [sharpening](sharpening.md).

After using ssharpen there is a F9 menu where you can adjust parameters and make changes post operation. However this is antiquated and could possibly [crash in Blender 2.8](https://builder.blender.org/download).

F9 menu as well as noticiation is shown below.

![ssharpen](img/ssharpen/s12.png)

Additive mode will made ssharpen add new sharp edges
  - unchecking it will make it recalculate the sharps on the mesh
  - this is normally checked by default so manually marked edges won't be overwritten

  Additive mode on. Notice how edges I mark in edit mode remain marked.

  ![ssharpen](img/ssharpen/s13.gif)

  Additive mode off. Recalculated and marked based off of angle. Sometimes this is useful.

  ![ssharpen](img/ssharpen/s14.gif)

The global toggle on by default ensures the options set here will be repeated next time. Uncheck this to use these setting only once this instance. This remains on by default and we rarely turn it off if ever.

So in short ssharp is all the processes mentioned above combined into one tool for quick hard surface smoothing. This is considered soft smoothing. The majority of time. The edges I mark are marked for a reason. But if you ever need to recalculate all the option is there for you.

There is also a video on this topic specifically.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ogtEheuBTHA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---
# Sharpen Configuration Options

![ssharpen](img/ssharpen/s13.png)

As with all tools, the tooltip provides additional insight. 

By default the following controls apply.

- LMB - Sharpen
- Ctrl - Csharpen (Apply Modifiers)
- Shift - Autosmooth (Interactive Autosmooth Adjustment)
- Alt - Weighted Normal (Normal Hardening Modifier)
- Ctrl + Shift - Recalculate Sharp Marks (Resharp)

Pressing Ctrl + K brings up the keymap for preferences where Sharpen can be reconfigured.

![ssharpen](img/ssharpen/s14.png)

**This DOES NOT update the tooltip at this time.**

> For those who are fans of Smart Apply they could for example replace csharp with smart apply quite easily.

![ssharpen](img/ssharpen/s27.gif)

---

# Autosmooth Quickprefs

Autosmooth quickprefs can be found in either the hardOps:

- N panel
- HOPS Corner Button
- Ctrl + ~ Helper

Tool >> Sharp Options

![sharp](img/ssharpen/ss26.gif)

To make the autosmoothing workflow easier we added the ability to quickly choose an smoothing pref.

![sharp](img/ssharpen/ss23.gif)

> In the above example it can be visual how higher autosmooth amounts can cause issues with lesser angles on meshes. 45 and lower works but 60 degrees resulted in shading issues.

The global toggle ensures the autosmooth set by the user is not reset when the ssharpen / csharpen / step operations are performed.

![sharp](img/ssharpen/ss24.gif)

> Notice that with global unchecked the autosmooth set in the previous example remains despite the sharp markings happening on the 30 degree angle.

Autosmooth can be toggled off an on using the toggle button.

![sharp](img/ssharpen/ss25.gif)

> Choosing any autosmooth quick preset will set smooth in addition to turning on autosmooth.

---

## Ssharp In Action

When ssharp is used the mesh receives the above mentioned things. There is also an F6 menu for adjusting the behavior.

![ssharpen](img/ssharpen/s6.gif)

> It is not recommended to change the sharpness or the autosmooth angle from the F6 menu. It is preferred to modify this from the outside in the T panel or the HOPS helper.

The only parameter to go into in the F6 is the Additive mode.

Additive mode is checked by default and basically makes the ssharps not overwrite previous ssharps and their levels.

Unchecked this will remove all ssharps and mark them again which can be useful in some situations. But in the below case you can see at 60 the remarking was not so successful.

![ssharpen](img/ssharpen/s7.gif)

Additive mode being off can also have annoyances which is why this is an alternate behavior. For example to fix shading sometimes certain edges must be marked. Having them recalucated will cause shading issues without manual fixes.

![ssharpen](img/ssharpen/s8.gif)

---

## Inside Out Sharpening

Over the course of using SSharpen on thousands of parts it has become apparent that using the lower left menu that no longer floats to change parameters can sometimes be risky and a one way trip to the desktop in some cases. Because of this we put the ssharpening parameters outside in various panels to experiment with adjusting the behavior in advance to try and maintain stability.

![ssharpen](img/ssharpen/s9.gif)

Working this way can be more risky however with complex meshes so for that reason the ssharpening paramerters are located outside of the operator.

It formerly was like this in 2.79

![ssharpen](img/ssharpen/s10.png)

As of now these options are in the [helper](helper.md) / N panel and hopsMini helper.

![ssharpen](img/ssharpen/s11.png)

The 30 / 45 / 60 buttons are presets for degress. Even this has a purpose. For example if you are cutting a bevelled mesh with 3 segments into another mesh. It will get caught at 30. However at 45 the sharpening is optimized to behave better.

![ssharpen](img/ssharpen/s12.gif)

In the example I had to go back and do edit mode sharpening on those two edges at the top but the interior was sharpened correctly instead of being caught at 30 degrees. I tend to use this option on higher values than 30 past blocking in.

> Seam may not be a good option to have checked when you begin UVing for obvious reasons.

---

## Why Ssharpen

>> Sharpen also is ran in edit mode with Set Sharp if nothing is selected. Otherwise it just marks / unmarks the selection. This can be handy for using ssharpen without exiting edit mode.

If you were to ssharpen manually you would have to click smooth, set autosmooth, go in edit mode select sharps based off of angle then mark as crease / sharp / seam / bevel weight. For simplicity we call that marking ssharp. To do this manually would put unwanted wear on your keyboard not to mention and uncountable amount of additional clicks.

![ssharpen](img/ssharpen/s1.gif)


> SSharpen does not add a bevel modifier or any modifier of any kind. It only smooths the object and marks edges.
As a result we feel it is the softer of the duo ssharpen/scharpen

---

## SSharpen Usage

Ssharpen can be used to update the ssharpening on a mesh after mesh operations like edit mode changes or manually applying modifiers. In the below example the blue marked edges represent the ssharp edges.

![ssharpen](img/ssharpen/s3.gif)

![ssharpen](img/ssharpen/ss15.gif)

Ssharpen can also be used as an updater for [Csharpen](csharpen.md) **in weight**. Once a mesh is in a Csharp state (bevelled) you can use ssharpen to get update bevel weights.
This is the secondary use of ssharpen.

![ssharpen](img/ssharpen/s4.gif)

Ssharpen also can be used in subdivision blocking and for many other things that require marking edges.

>Q: I mean the name. Why the name?

>A: Well it was initially called soft sharpen so we just shortened it. Its must better than replacing it with " click smooth, set autosmooth, go in edit mode select sharps based off of angle then mark as crease / sharp / seam / bevel weight"

---

## Ssharpen Extra Uses

# Subdivision Rebasing
Sometimes the right marking of an edge can be the difference between smoothing a cylinder or turning it into a mess.

![ssharpen](img/ssharpen/s2.gif)

This was something I discovered by accident but found to be quite essential.
If you put a subsurf on the default cylinder you lose the form, but with the creasing in the right area you can prevent the form from collapsing and add roundness to the are a you intend.

# Mark Seams For Quick Selections
When utilized with the seams checkbox in either the helper or the tpanel, you can make face selections in edit mode with L (select linked)

![ssharpen](img/ssharpen/ss14.gif)

This is utilized for material assignment or face extraction.

![ssharpen](img/ssharpen/s5.gif)

---

### sSharpen use cases

- calculating ssharps on meshes
![ssharpen](img/ssharpen/s13.gif)

- recalculating ssharps on meshes
![ssharpen](img/ssharpen/s14.gif)

Recalculation is done via the F6 menu that is available after running the operator.

---

### SSharpen F9 options

![ssharpen](img/ssharpen/s12.png)

1. sharpness
   * edge angle to witch sharpening is applied - default 30

2. auto smooth angle
   * value for autosmoouth angle for selected object - default

3. additive mode
   * ON - apply defined sharpness and keeps other already existing sharp edges
   * OFF - clears all sharp edges before applying its own sharpness

2. global
  * ON - ensures the options set here will be repeated next time
  * OFF - uncheck this to use these setting only once this instance.

  This remains on by default and we rarely turn it off if ever.

---

## Removing Csharp / Ssharp marks / modifiers from meshes

See [Clear s/c Sharps](clearssharps.md)
