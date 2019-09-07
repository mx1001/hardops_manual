![header](img/banner.gif)

### Circular Array

Circular array can be found in the modifiers section of hard ops Q menu.

![cs1](img/circ1/c1.png)

After adding additional segments can be added with array and distance adjusted with displace.

![cs1](img/circ1/c1.gif)

There is a ctrl + click 3d cursor circular array which was intended for assistance with things like Boxcutter.

![cs1](img/circ1/c2.gif)

The 3rd state will not use the 3d cursor and will launch the user into displace allowing for quick positioning.

![cs1](img/circ1/c3.gif)

At this time adjustment is done via array and displace modifier modals. This will be streamlined in the future but for now our next feature will have to do.

# Circular Array w/ hopsTool

When using hopsTool you can add circular array to any object and adjust it using dots.

![cs1](img/circ1/c4.gif)

# How Circular Array works.

- array with count driving rotation of empty using a driver
- empty is parented to the main object

This is due to a change in cyclic dependency issues thanks to the new depsgraph update.

Below is a video about circular array before the tool was added. Our goal was to have boxcutter shift to live with this type of circular array. Now it is a reality.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-THNLxaP_D4" frameborder="0" allowfullscreen></iframe>
