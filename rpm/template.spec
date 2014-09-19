Name:           ros-hydro-sr-visualization
Version:        1.3.4
Release:        0%{?dist}
Summary:        ROS sr_visualization package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_visualization
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-sr-gui-bootloader
Requires:       ros-hydro-sr-gui-change-controllers
Requires:       ros-hydro-sr-gui-change-muscle-controllers
Requires:       ros-hydro-sr-gui-controller-tuner
Requires:       ros-hydro-sr-gui-grasp-controller
Requires:       ros-hydro-sr-gui-hand-calibration
Requires:       ros-hydro-sr-gui-joint-slider
Requires:       ros-hydro-sr-gui-motor-resetter
Requires:       ros-hydro-sr-gui-movement-recorder
Requires:       ros-hydro-sr-gui-muscle-driver-bootloader
Requires:       ros-hydro-sr-gui-self-test
Requires:       ros-hydro-sr-visualization-icons
BuildRequires:  ros-hydro-catkin

%description
This stack contains the different gui plugins used with the shadow robot stacks.

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

