![header](img/banner.gif)

### Booleans

## Hard Ops and Booleans

**[Booltool](https://blenderartists.org/forum/showthread.php?336498-BoolTool-0-2&p=2659836&viewfull=1#post2659836) is no longer required** The hotkeys I once used booltool for have been added into the core of hard ops and supports the drawing and interconnecting systems as a result. The hotkeys are as follows:

- ctrl + numpad minus (difference boolean)
- ctrl + numpad plus (union boolean)
- ctrl + numpad slash (slash boolean)

To demonstrate union and difference.

![bool](img\boolean\ll3.gif)

To demonstrate slash.

![bool](img\boolean\ll4.gif)

> Slash is also in the Q menu when 2 objects are selected.

So while we support booltool and will respect it if enabled, the HOPS boolean system will also set up [drawing](hud.md) and use our [systems](sstatus.md).

---

## Using Booleans in Hard Ops

# hotkeys

With 2 or more objects the following hotkeys apply.

- ctrl + numpad minus (difference boolean)
- ctrl + numpad plus (union boolean)
- ctrl + numpad slash (slash boolean)

![bool](img\boolean\ll3.gif)

# Q menu

With 2 or more objects the Q menu will show an option for booleans.

![bool](img\boolean\ll5.png)

> I generally use the hotkeys but this is added for additional conveninece.

# Shift + Q Pie menu

With 2 or more objects the shift + Q menu will show options for booleans.

![bool](img\boolean\ll6.png)

---

## boolshape

When an object is used as a boolean the following things happen:
  - object is converted into a wire
  - object receives the sstatus: boolshape which affects the Q menu

This means the object has a special Q menu with options for bevel, solidify and array.
To demonstrate them all at once.

![bool](img\boolean\ll7.gif)

When the logo is red the object is a boolshape. To reset a boolshape just reset the sstatus and convert back into solid in the [settings](settings.md) submenu.

![bool](img\boolean\ll8.gif)


---

# Backstory: [Booltool](https://blenderartists.org/forum/showthread.php?336498-BoolTool-0-2&p=2659836&viewfull=1#post2659836)

Before [booltool](https://github.com/vitorbalbio/code/tree/master/BoolTool) existed, adding a boolean to a mesh was similar to the below example.

![bool](img\boolean\ll1.gif)

When [Booltool](https://blenderartists.org/forum/showthread.php?336498-BoolTool-0-2&p=2659836&viewfull=1#post2659836) first came out it caused an explosion of booleans onto the scene. They always existed but there never was an approach to make them so applicable.

> I mention the 0.2 version because it was the last update by original creator vitorbalbio. 0.3 and beyond is now handled by a different person so therefore the tool is different now.

In my personal workflow it introduced the ability use the hotkeys:

- ctrl + numpad minus (difference boolean)
- ctrl + numpad plus (union boolean)

![bool](img\boolean\ll2.gif)

I used booltool for the longest time in this state without expansion or advancement. I especially used this in conjunction with edge split which made animation a nightmare. However this was the workflow at the time.

It goes without saying booltool had many other features worth checking out but the subtractive behavior was my main focus. I still loved what this tool brought to the table and it also opened my eyes to having mirroring and other tools have the same simplistic behavior.

---
