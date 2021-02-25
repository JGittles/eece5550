# Install script for directory: /home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ubuntu/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/turtlebot3_autorace_level_crossing_detect" TYPE FILE FILES "/home/ubuntu/catkin_ws/devel/include/turtlebot3_autorace_level_crossing_detect/DetectLaneParamsConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/turtlebot3_autorace_level_crossing_detect" TYPE FILE FILES "/home/ubuntu/catkin_ws/devel/include/turtlebot3_autorace_level_crossing_detect/DetectLevelParamsConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/ubuntu/catkin_ws/devel/lib/python2.7/dist-packages/turtlebot3_autorace_level_crossing_detect/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/turtlebot3_autorace_level_crossing_detect" TYPE DIRECTORY FILES "/home/ubuntu/catkin_ws/devel/lib/python2.7/dist-packages/turtlebot3_autorace_level_crossing_detect/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/turtlebot3_autorace_level_crossing_detect.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_level_crossing_detect/cmake" TYPE FILE FILES
    "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/turtlebot3_autorace_level_crossing_detectConfig.cmake"
    "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/turtlebot3_autorace_level_crossing_detectConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_level_crossing_detect" TYPE FILE FILES "/home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_level_crossing_detect" TYPE PROGRAM FILES "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/detect_lane")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_level_crossing_detect" TYPE PROGRAM FILES "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/detect_level")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_autorace_level_crossing_detect" TYPE PROGRAM FILES "/home/ubuntu/catkin_ws/build/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/catkin_generated/installspace/detect_sign")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_autorace_level_crossing_detect" TYPE DIRECTORY FILES
    "/home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/cfg"
    "/home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/file"
    "/home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/launch"
    "/home/ubuntu/catkin_ws/src/turtlebot3_autorace_2020/turtlebot3_autorace_level_crossing/turtlebot3_autorace_level_crossing_detect/param"
    )
endif()

