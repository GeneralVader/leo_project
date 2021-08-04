# LEO PROJECT :-->

# <h3>BRIEF INTRODUCTION :<h3>
  This project is based of autonomous path planning and motion of Leo rover. We have taken help of openCV to get the structure of our path ahead and 
  our leo itself decides whether to straight, left or right !
  
  A glimpse of leo Rover.
  
  <img src = "https://github.com/AYUSH-ISHAN/leo_project/blob/main/leo.jpg" height = "480" width = "480"/>
  


# <h3>INSTALLATION :<h3>
  This installation procedure assumes that you have installed ROS Version-1 and Gazebo (preferably version 9).
  1. The first step is the installation of the leo_simulator. You have to go to this link and clone the <a href = "https://github.com/LeoRover/leo_simulator">leo simulator</a> github repo. You can also go to <a href = "http://wiki.ros.org/leo_gazebo">official ROS</a> website of leo gazebo.
  
  2. After completing the step 1 of installation of, repeat the customary step of compiling the catkin package and sourcing its devel file by:-<br>
  
                        ~/catkin_ws $ catkin build or catkin_make>
                        ~/catkin_ws $ source devel/setup.bash

  3. In the third step you will clone our repo and place it in your package and again repeat the customary step of compiling the catkin package and sourcing its devel file as stated above.
  
  4. Now, we will move towards installing Differential Drive plugins. If you are using Melodic distro, then you should have this package inbuilt. But if you are
  on some other distro or somehow not having it, then you may clone this <a href = "https://github.com/ros-controls/ros_controllers">repo</a> and move ahead.
  
 4. Open a fresh terminal and launch the following code in it.<br>
  
                  ~/catkin_ws/src $ roslaunch leo_drive spawn_leo.launch
 
  After firing this command the folling should appear on your gazebo.
  
  <img src = "https://github.com/AYUSH-ISHAN/leo_project/blob/main/leo_road.png"/>
  
  You got it right ?? If yes then you have successfully completed the installation.
  And now it is : - > 
  
  <img src = "https://github.com/AYUSH-ISHAN/leo_project/blob/main/tenor.gif"/>
  
  # <h3>SHOWTIME :<h3>
  
  Since we are fully ready with our installation, lets us make our rover work. Follow the following steps to proceed.
  
  1. Open a fresh terminal with the gazebo simulation running on the other one. Fire Up the following command.
  
              ~/catkin_ws/src $ rosrun leo_drive capture_image.py
  
  
  If it runned succssfully it shouyld present the following images.
  
  <img src = "https://github.com/AYUSH-ISHAN/leo_project/blob/main/mask.png"/>
  
  
  <img src = "https://github.com/AYUSH-ISHAN/leo_project/blob/main/warp_image.png"/>
  
  The first image is the simple masking of the road while the second one is the bird-view type perspective of the camera.

  
  
  
 

  
  
  
