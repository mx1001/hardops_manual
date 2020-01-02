![header](img/banner.gif)

### Sharpen

# Locating Sharpen

Sharpen is able to be found in the main menu(Q) / main pie(shift + Q) / n panel of hopstool.

As the tooltip shows this is a multi-tool intended to handle the entirety of the sharpening workflow. Our goal was to consolidate all sharpening behaviors into a single tool and ensure it is the fastest version possible.

![sharpen](img/sharpen/s1.png) ![sharpen](img/sharpen/s2.png) ![sharpen](img/sharpen/s3.png)

_______

# Customizing Sharpen

Sharpen is customizable in preferences however the tool tip may not reflect those changes. I like to have classic csharp as my fallback for everything and unmark sharps under my alt.

![sharpen](img/sharpen/s4.png)

My defaults are set to the following.

- LMB - [sharpen (ssharp)](ssharpen.md)
- ALT - clear sharp markings (cleansharp)
- CTRL - [sharpen / apply (csharp)](csharpen.md)
- Shift - recalculate sharps (resharp)
- Ctrl + Shift - sharpen / apply + jump to adjust bevel

_______

## Basic Usage

# [Sharpen](ssharpen.md) - LMB

- LMB - sharpen (ssharp)

By default LMB on sharpen will select sharp edges and mark them according to the options specified in the:

- (ctrl + ~) helper
- worflow area of the n panel.

![sharpen](img/sharpen/s5.gif)

After usage the F9 panel can be used to make fine adjustments post operation like adjusting the angle sharpen is looking for.

![sharpen](img/sharpen/s6.png) ![sharpen](img/sharpen/s7.png)

_______

# [Csharpen](csharpen.md) - Ctrl + LMB

- CTRL - sharpen / apply (csharp)

Csharp is the same as sharp except boolean modifiers and others (specified in F9) are being applied before the sharpening process to ensure the new geometry receives markings as well.

There is also an option to add a bevel to the mesh like classic but it must be clicked.

To demonstrate in action let's set up a couple of cuts.

![sharpen](img/sharpen/s8.gif)

Sharp will mark the unaffected cube but the booleans remain live.

![sharpen](img/sharpen/s9.gif)

Ctrl + clicking sharpen will apply the boolean modifiers and perform sharpening.

![sharpen](img/sharpen/s10.gif)

_______

# Clear Sharps - ALT

In the event you want to unsharpen a mesh and remove markings / bevels alt activates clear sharp.

**Alt** clicking sharpen will remove all markings.

![sharpen](img/sharpen/s11.gif)

_______

# Recalculate Sharps - Shift

Occasionally while modelling sharp markings can become inaccurate and could use a recalculation.

**Shift** clicking sharpen will activate re-sharp.

This mode unmarks the model and remarks it with sharp marked edges.

![sharpen](img/sharpen/s12.gif)

_______

# Csharp + Bwidth - Ctrl + shift

Csharp + Bwidth is the process of applying the selected modifiers, marking sharp edges and jumping into bevel width adjustment mode. This workflow was popular in the touch and go workflow of classic csharp so it remains for users who miss working linearly.

![sharpen](img/sharpen/s13.gif)

> This mode jumps you into a modal so the F9 panel is unavailable so the general assumption is if using this you already have the F9 panel in order from a previous operation.
_______
