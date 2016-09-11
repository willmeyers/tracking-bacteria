# Tracking Protozoa
Interested in computer vision and inspired by an article on [using protozoa swimming patterns](https://www.whoi.edu/mr/pr/viewArticle.do?id=133689) to detect toxins in water, I decided to develop a small program that tracks protozoa movement. The program implements two possible ways of tracking movement.

To limit the scope of this program, I did not implement a meaningful way to indentify swimming patterns of a selected protozoa in 2D or 3D space; however the position (X, Y) of the points (retrieved from the moving protozoa) can surely by measured and interacted with in some meaningful way.

## Method
There are currently two different methods that I implemented in tracking protozoa that are built into the application.

1. Background subtraction

2. Lucas-Kanade and Feature Detection

### Background Subtraction
![Background-sub image](background-sub.gif)

An inital frame is captured from the device and is set as the background, which is then blurred using Gaussian blur. As frames are read by the capture device, each frame is blurred and then a threshold is created which tracks the differences between the initial frame and the current frame. Changes are highlighted with a pink bounding box, and the movement is tracked.

### Feature Detection and Lucas-Kanade
![Lucas-Kanade image](lucas-kanade.gif)

A user defines a region of interest, in this case a protozoa, where using feature detection gives an array of points that highlights the object. The points are averaged out which returns a single, averaged point used for tracking. The points are average due to the feature detection returning points selecting the outline of the protozoa. To get a more accurate tracking path, the points are averaged and the returned point is usually always in the center of the organism.
