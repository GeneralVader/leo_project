# LEO PROJECT :-->

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
  
  
  
 

  
  
  
