# Tracking Protozoa
Interested in computer vision and inspired by an article on [using protozoa swimming patterns](https://www.whoi.edu/mr/pr/viewArticle.do?id=133689) to detect toxins in water, I decided to develop a small program that tracks protozoa movement. The program opens a window, showing the video stream of a capture device, where regions of interests can be defined and then tracked.

To limit the scope of the program, I did not implement a meaningful way to indentify swimming patterns of a selected protozoa in 2D or 3D space; however the position of the points (retreived from the moving protozoa) can surely by measured and interacted with in some meaningful way.

## Method
There are currently two different methods that I implemented in tracking protozoa built into the application.

1. Background subtraction

2. Lucas-Kanade and Feature Detection

### Background Subtraction


### Feature Detection and Lucas-Kanade
