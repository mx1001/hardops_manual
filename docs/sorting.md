![header](img/banner.gif)

### Sorting workflows in hardOps

# hopsSort

The sort tickbox in hardOps and boxcutter is there for users to specify what modifiers are supposed to be where in the stack post boolean operation. Unchecked modifiers do nothing and remain where there are in the stack.

**clicking them does nothing until the next boolean operation**

[**This only affects boolean operations**](boolean.md)

![mir](img/faq/f2.png)

Sort can be turned off an on overall and the buttons next to it do the following:

- last bevel to bottom of stack (ahead of booleans)
- sort bevel modifiers - move bevel mods to bottom of stack
  - non vgroup / weight models
- sort array - ensures array is last so it shows booleans in all subparts
- sort mirror - using modifier mirror at the end of the stack will mirror all cuts
- sort solidify - keeps solidify later in the stack. Off by defaults. Only used in certain situations.
- sort weighted normal - keeps weighted normal at the end of the stack (maintains shading)
- sort simple deform - keeps simple deform at the end of the stack before the rest.
- sort triangulate - keeps triangulate after boolean to allow for iterative working on an exportable mesh
- sort decimate - moves decimate at the end of the stack (useful for rare situations)
  - recommended off for smart shapes and situations where the mod order is crucial.

To show sort bevel in action.

![mir](img/faq/f3.gif)

In this example I turned on only bevel sorting. Notice that when I used the boolean operation, the modifier for mirror was put last.

![mir](img/faq/f5.gif)

The down pointing arrow is for latest bevel sort. If you have more than one bevel more than likely you only want to deal with the highest level in order to cut with an independent bevel level.

## <kbd>Ctrl</kbd> + <kbd>~</kbd> helper

![mir](img/faq/f4.png)

This is how I am able to cut on the final level of a bevel without affecting previous levels.
In this example the bevel angles are as follows.

- 30 degrees
- 60 degrees
- 60 degrees

If I use another 30 degree bevel it will detect the previous levels and cause mesh issues and possibly a crash. So this can be a delicate dance.

With mirror sorting the mirror will also be added to the end of the stack ensuring that the modifiers are always ordered in a way to keep working with booleans non destructively.

![mir](img/faq/f6.gif)

At the end of the last gif I added a Weighted normal modifier. This mod will always need to be at the end or else shading issues will occur. Turning it on will ensure the mod remains at the end when boolean operations are performed. It is best to turn that on when working with weighted normal.

![mir](img/faq/f7.gif)

> Multi- Bevel Sorting video

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZnyMUIilp6g" frameborder="0" allowfullscreen></iframe>


## Sort Gotcha w/ hShapes

Some of the new smart shapes will require certain mods be off in order to maintain stack order.
Lets look at the current smart bbox and scroll through its mods to see how it is made.

![mir](img/faq/f8.gif)

The mods on this box are as follows.

![mir](img/faq/f9.png)

If we move / toggle the decimate mod this shape will be fundamentally changed. The decimate is needed for simplification and will cause issues.

To show that in action.

![mir](img/faq/f10.gif)

This is just to show that all situations can't be handled with sorting and at this time turning off sorting can also be of benefit to users.

Boxcutter also has a sort that must be taken into account. It can be found in either the topbar, n panel or D menu.

![mir](img/faq/f11.gif)

We aspire to expand sorting into something more expansive down the road but for now it will have to suffice for boolean operation.

___
