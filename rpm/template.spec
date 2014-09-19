Name:           ros-hydro-sr-gui-muscle-driver-bootloader
Version:        1.3.4
Release:        0%{?dist}
Summary:        ROS sr_gui_muscle_driver_bootloader package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_gui_muscle_driver_bootloader
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-sr-robot-msgs
Requires:       ros-hydro-sr-visualization-icons
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rqt-gui
BuildRequires:  ros-hydro-rqt-gui-py
BuildRequires:  ros-hydro-sr-robot-msgs
BuildRequires:  ros-hydro-sr-visualization-icons
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs

%description
A GUI plugin for bootloading the muscle drivers on the etherCAT muscle shadow
hand.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Sep 19 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.4-0
- Autogenerated by Bloom

