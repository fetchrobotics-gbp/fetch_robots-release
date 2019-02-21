Name:           ros-melodic-fetch-drivers
Version:        0.8.4
Release:        0%{?dist}
Summary:        ROS fetch_drivers package

Group:          Development/Libraries
License:        Proprietary
URL:            https://wiki.ros.org/fetch_drivers
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       curl
Requires:       libcurl-devel
Requires:       python-devel
Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-fetch-auto-dock-msgs
Requires:       ros-melodic-fetch-driver-msgs
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-power-msgs
Requires:       ros-melodic-robot-calibration-msgs
Requires:       ros-melodic-robot-controllers
Requires:       ros-melodic-robot-controllers-interface
Requires:       ros-melodic-rosconsole
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-rostime
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-urdf
Requires:       urdfdom-devel
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  python-devel
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-fetch-auto-dock-msgs
BuildRequires:  ros-melodic-fetch-driver-msgs
BuildRequires:  ros-melodic-mk
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-power-msgs
BuildRequires:  ros-melodic-robot-calibration-msgs
BuildRequires:  ros-melodic-robot-controllers
BuildRequires:  ros-melodic-robot-controllers-interface
BuildRequires:  ros-melodic-rosconsole
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-rospack
BuildRequires:  ros-melodic-rostime
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  yaml-cpp-devel

%description
The public fetch_drivers package is a binary only release. fetch_drivers
contains both the drivers and firmware for the fetch and freight research
robots. There should be no reason to use these drivers unless you're running on
a fetch or a freight research robot. This package, is a cmake/make only package
which installs the binaries for the drivers and firmware.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Feb 21 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.4-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.3-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.2-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.1-0
- Autogenerated by Bloom

* Wed Feb 13 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.0-1
- Autogenerated by Bloom

* Wed Feb 13 2019 Alexander Moriarty <amoriarty@fetchrobotics.com> - 0.8.0-0
- Autogenerated by Bloom

