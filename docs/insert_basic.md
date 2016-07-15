## Insert System

Hard Ops has an insert system for using premade meshes for quick greebling and detail work. It's intended to be used in a pinch when detail is needed quickly.

![](insert\ins_preview.png)

The insert system can be brought up via the Q menu via inserts and also has a top option for an asset scroller which allows you to cycle through assets.

![](insert\ins_1.gif)

![](insert\ins_2.gif)

___

![](img\faq\faq21.png) Orange Inserts are just basic inserts. These are just meshes you place.

> Orange inserts can be inserted on a series of faces and can be scaled immediately after selection via a modal operation. This allows for scaling to perfection. It even sets the pivot points to individual origins so they retain their position. These work in both object and edit mode.

![](img\faq\faq24.gif)

![](img\faq\faq22.png) Red Inserts are inserts made to be boolean cut into surfaces.

![](img\faq\faq23.png) Adjustable inserts are red inserts that can be adjusted prior to being applied.

>Red inserts also do not get inserted on faces. They always are inserted at the 0,0,0 of the 3d view. This is because they dont behave well being placed automatically due to the hook modifiers that the adjustable ones have. These inserts also have an AP that allows for surface snapping while also seeing the outside perimeter. This allows for precise placement.

![](img\faq\faq25.gif)

> Red inserts are built up out of these 3 pieces.
  - AP or alignment plane (used for aligning the whole insert)
  - BB of BoolBox (used for the boolean to make room for the OB)
  - OB or Object (the object being inserted)

![](img\faq\faq26.png)

[Update Log Explaining Red Inserts ](https://masterxeon1001.com/2016/01/05/hops0065update/)

___

# Inserts In Action
