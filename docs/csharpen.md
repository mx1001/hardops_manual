![header](img/banner.gif)

### Csharpen

Csharpen does the following things.

- set shading to smooth from flat
- enables autosmooth / sets angle to 60
- marks edges as crease / sharp / seam / bevel weight based off of sharp parameter.
- applies boolean modifiers and other non hard surface modifiers
- adds a bevel modifier (segements: 3 / profile 0.7 / weight not angle)
- sets menu behavior to be for objects that are bevelled via changing [sstaus](sstaus.md)

If this sounds like the ssharpen that is because this is the complex version of that tool. Created at the same time for a more specific reason. Applying modifiers and setting up bevels.

This may sound strange but it allows for a very itterative forward workflow with boolean based workflows.

Below is an example of it in action.

![csharpen](img/csharpen/c1.gif)

In the above example I used simple cubes to boolean into the main shape. Then using cSharpen I was able to both bevel the form and apply the boolean modifier. After that I used another cube to boolean and when cSharpening it was able to ignore the bevel modifier and apply the boolean.


There is also a video on this topic specifically.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5lzfHQBel0o" frameborder="0" allowfullscreen></iframe>

---

## F6 Menu

The F6 menu has options that are similar to Ssharpen with a few additions.

![csharpen](img/csharpen/c2.png)

- Modifiers (hold shift to select / deselect) defaults generally are fine with the exception of sometimes ignoring solidify as well
- general parameters (antiquainted - these options aren't changed normally)
- sharpness - same reason as [ssharpen](ssharpen.md)

---

## Csharpen In Action

This is the basic usage of cSharpen in a boolean workflow.

![csharpen](img/csharpen/c3.gif)

By default it ignores the bevel modifier. Under no circumstances do we apply the bevels via the cSharpen.

With solidify it can be useful to keep the solidify live for non destructive workflows.

![csharpen](img/csharpen/c4.gif)

---

## Why Csharpen?

Csharpen became a needed tool after we began using boolean based workflows and needed a way to procedurally work forward with less steps. The tool was initially called complex sharpen but in the end we decided on cSharp.



<iframe width="560" height="315" src="https://www.youtube.com/embed/N-ihUA3VmtA" frameborder="0" allowfullscreen></iframe>

---

## Removing Csharp / Ssharp marks / modifiers from meshes

See [Clear s/c Sharps](clearssharps.md)
