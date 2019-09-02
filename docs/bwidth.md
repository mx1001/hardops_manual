![header](img/banner.gif)

### bWidth

## What is bWidth?

bWidth is the name of the modal used for adjusting the bevel width of a modifier interactively in the 3d view.

There are additional uses

---

## bWidth use cases

If the mesh is undefined:

Q >> [Operations](operations.md) >> bWidth

![bevelwidth](img/bwidth/b3.gif)

- weight means this will only work on marked edges
- no clamp overlap means this will be capable of exceeding geometric limits
- adding bweight without csharpen will result in an angle bevel being added

As of 2.8 the goal is to try to be more non destructive so the default is now angle which ignores edge weights.

> [Csharp](csharp.md) : In the event you desire classic behavior set workflow to weight in the ctrl + ~ helper.

![bevelwidth](img/bwidth/b8.gif)

If the mesh is [csharp](csharp.md) / [cstep](step.md):

Q >> bWidth (after csharp)

![bevelwidth](img/bwidth/b4.gif)

- angle means this is not connected to the hops systems and is a default bevel mod
- clamp overlap means this mesh is limited by its geo to ranges unable to exceed understanding.

This is important because the behaviors will be different. While there is a time and place for bWidth on undefined meshes we typically use it on csharp meshes for refinement.

In addition, it can be used to adjust the bevel width of one or more objects.

![bevelwidth](img/bwidth/b5.gif)

When used on multiple objects it is capable of respecting differing offsets and even more.

---

## bWidth detailed usage

> When pressing H during a modal the help will be displayed.

![bwidth](img/bwidth/b6.png)

- scroll - raises and lowers segments. When it comes to segments the following applies:
  - 3 is default becuase the geometric hit isn't too hard.
  - even numbers work best with material indexes
  - 6 will make it capable of not being rebevelled by ssharp/csharp at 30 degrees

- ctrl - changes profile. We generally stick with .7 by default
- W - changes offset type / never used
- V - shows / hides bevel modifiers. Can be useful as a toggle for multiple objects
- Z - shows wire in viewport. has uses extending past just seeing bevels. Also can be used to quickly show wires.
- 1 - toggles autosmooth / for times where you need to toggle autosmooth within the bevel operation
- 2 - use bevel verts (makes bevel use only verts)
- A - Adaptive Mode (added by [machin3](https://twitter.com/machineio)) makes bevel segments adjust according to scale.
- C - Loop slide / See mod tooltip
- S - Modal segments
- E / Shift + Wheel up - allows user to move mod up the stack
- Q / Shift + Wheel down move mod down stack
- P - Change profile
- N - Flip Normal - used for reverse bevelling.
- M - Harden Normals

Usage of the N - flip normal in action.
![bevelwidth](img/bwidth/b9.gif)

> In this example I used a boolean which set the shape as a boolshape which triggers face normal flipping for edit mode bevelling built in by default. Alternatively users would have to press N during modal.

---

## bWidth advanced

# Modifier Differences For Undefined / Csharp meshes

The option is intended to be generally used in the Q menu following the [csharp](csharp.md) operation.

The bevel default modifier created is like this:

![bevelwidth](img/bwidth/b1.png)

For Csharp the setting specified in workflow determine the bevel added.
![bevelwidth](img/bwidth/b10.gif)

If used on undefined meshes the modifier created looks like this:

![bevelwidth](img/bwidth/b2.png)


# bWidth for disabling modifiers temporarily / viewing wires

![bevelwidth](img/bwidth/b7.gif)

**V** during modal will make the bevel modifier hidden.

**Z** during modal will show wires on all selected models

# bWidth will not work on non objects

![bevelwidth](img/bwidth/b11.gif)

At the beginning of this gif the options are greyed out due to my all selection including curves. This is due to the context sensetive nature of the of the operator.

# bWidth to bevel cut

![tthick](img/tthick/t7.gif)

This options is in the boolshape menu for a reason. By beveling shapes before committing you can round out areas being cut for a machined surface.

Modifier order matters here as well so it's important to keep in mind what is on top and how that can affect behavior and cause undesired overlaps.
