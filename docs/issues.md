![header](img/banner.gif)

### Helping us help you

# Capturing Issues w/ ShareX windows

When it comes to Blender crashes occur however being able to replicate it and provide steps for what causes it goes much farther for assistance with diagnosis.

For windows a small freeware app called [ShareX](https://getsharex.com/) is essential.

![hotkey](img/issue/i1.png)

In ShareX I set my workflow to the above image.

Thanks to this I am able to quicky record gifs and screencasts of issues.

For example theres an issue where if the decimate mod is moved up the smartBox modstack it will cause shading and geometrical issues.

![hotkey](img/issue/i2.gif)

By providing this instead of a vague description it can better inform us of what the issue.

Another thing that could be of use is showing us the modifier stack.

It is part of the N panel and ctrl + ~ systems so showing us what is present also gives us insight.
Also keeping an eye on the stack can better give the users insight on what is going on behind the scenes.

![hotkey](img/issue/i3.gif)

> In this example I turned off decimate sort and booled again which resolved the issue. The decimate mod needed to be where it was and not moved. So this wasn't a bug. But still an issue nonetheless.

# Mac Help

The stuff it says in crash reports is not of use to us. I don't think non apple engineers can read that.

Getting the terminal output to remain after a crash is more essential.

![hotkey](img/issue/i4.png)

![hotkey](img/issue/i5.gif)


# PC Help

When Blender crashes the console goes with it. By running Blender via the cmd you can get additional information that can help us fix issues.

Right clicking Blender while open to access the properties will get you the shortcut.

![hotkey](img/issue/i6.png)

![hotkey](img/issue/i8.png)

Windows + R >> Run Window >> cmd

> Brings up command prompt.

![hotkey](img/issue/i7.png)

In the cmd paste the shortcut from the properties window.

Running blender this way will make the cmd be a terminal output. Providing us information on why crashes occur.

![hotkey](img/issue/i9.gif)
