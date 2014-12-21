Name:           ros-indigo-sr-gui-joint-slider
Version:        1.3.1
Release:        0%{?dist}
Summary:        ROS sr_gui_joint_slider package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_gui_joint_slider
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-sr-hand
Requires:       ros-indigo-sr-robot-lib
Requires:       ros-indigo-sr-robot-msgs
Requires:       ros-indigo-sr-visualization-icons
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-manager-msgs
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rqt-gui
BuildRequires:  ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-sr-hand
BuildRequires:  ros-indigo-sr-robot-lib
BuildRequires:  ros-indigo-sr-robot-msgs
BuildRequires:  ros-indigo-sr-visualization-icons
BuildRequires:  ros-indigo-std-msgs

%description
A GUI plugin for changing the position of the different joints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.1-0
- Autogenerated by Bloom

