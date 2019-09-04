![header](img/banner.gif)

### tThick

## What is tThick?

Tthick is one of the modal operators in Hard Ops intended to use a solidify modifier in a modal manner. This tool is intended to behave as an object level extrude.

---

## tThick use case

If the mesh is undefined:

Q >> tThick

If the mesh is [csharp](csharpen.md) / [cstep](step.md):

Q >> [Operations](operations.md) >> tThick

![tthick](img/tthick/t1.gif)

In the above example I reset the [sstatus](sstatus.md) to undefined and used tthick to thicken the mesh. From there I was able to use the [boolean](boolean.md) hotkey to cut into the main mesh.

---

## tThick Detailed Usage

> When pressing H during a modal the help will be displayed.

![tthick](img/tthick/t2.png)

When using tThick the following hotkeys apply:

  - R - turns on rim for solidify (useful for cases where the mesh needs to only look thick)
  - 1 - sets offset to 1. Makes mesh sit on top of itself.
  - 2 - sets offset to 0. This pushes the mesh in and out at the same time.
  - 3 - opposite of 1. Pushes mesh down itself.
  - Ctrl - changes offset manually. Rare usage.

Rim

![tthick](img/tthick/t3.gif)  

Offset Example

![tthick](img/tthick/t4.gif)

---

## tThick tips

# tThick to panel cut

Having a pending boolean sets your mesh into what is called a [boolshape](sstatus.md). The icon in the corner will be green. ![tthick](img/tthick/t6.png)

This means the Q menu will have the boolshape menu of:

- bWidth
- tThick
- qArray

tThick has the interesting effect of turning a boolean into a panel cut.

![tthick](img/tthick/t7.gif)

![tthick](img/tthick/t8.gif)
