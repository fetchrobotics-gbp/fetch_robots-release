%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-freight-bringup
Version:        0.9.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS freight_bringup package

License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-diagnostic-aggregator
Requires:       ros-noetic-fetch-description
Requires:       ros-noetic-fetch-drivers
Requires:       ros-noetic-fetch-navigation
Requires:       ros-noetic-fetch-open-auto-dock
Requires:       ros-noetic-fetch-teleop
Requires:       ros-noetic-graft
Requires:       ros-noetic-joy
Requires:       ros-noetic-robot-state-publisher
Requires:       ros-noetic-sick-tim >= 0.0.4
Requires:       ros-noetic-sound-play
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Bringup for freight

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
* Sun Apr 25 2021 Eric Relson <erelson@fetchrobotics.com> - 0.9.3-1
- Autogenerated by Bloom

* Fri Mar 12 2021 Eric Relson <erelson@fetchrobotics.com> - 0.9.2-1
- Autogenerated by Bloom

* Fri Mar 05 2021 Eric Relson <erelson@fetchrobotics.com> - 0.9.1-1
- Autogenerated by Bloom

