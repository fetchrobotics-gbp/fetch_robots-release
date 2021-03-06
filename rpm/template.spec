%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-fetch-drivers
Version:        0.9.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS fetch_drivers package

License:        Proprietary
URL:            https://wiki.ros.org/fetch_drivers
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       curl
Requires:       libcurl-devel
Requires:       python3-devel
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-actionlib-msgs
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-fetch-auto-dock-msgs
Requires:       ros-noetic-fetch-driver-msgs
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-power-msgs
Requires:       ros-noetic-robot-calibration-msgs
Requires:       ros-noetic-robot-controllers
Requires:       ros-noetic-robot-controllers-interface
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roscpp-serialization
Requires:       ros-noetic-rostime
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-urdf
Requires:       urdfdom-devel
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  python3-devel
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-actionlib-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-fetch-auto-dock-msgs
BuildRequires:  ros-noetic-fetch-driver-msgs
BuildRequires:  ros-noetic-mk
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-power-msgs
BuildRequires:  ros-noetic-robot-calibration-msgs
BuildRequires:  ros-noetic-robot-controllers
BuildRequires:  ros-noetic-robot-controllers-interface
BuildRequires:  ros-noetic-rosconsole
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roscpp-serialization
BuildRequires:  ros-noetic-rospack
BuildRequires:  ros-noetic-rostime
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The public fetch_drivers package is a binary only release. fetch_drivers
contains both the drivers and firmware for the fetch and freight research
robots. There should be no reason to use these drivers unless you're running on
a fetch or a freight research robot. This package, is a cmake/make only package
which installs the binaries for the drivers and firmware.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Mar 05 2021 Carl Saldanha <csaldanha@fetchrobotics.com> - 0.9.1-1
- Autogenerated by Bloom

