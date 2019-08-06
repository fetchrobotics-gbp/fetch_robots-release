Name:           ros-melodic-freight-bringup
Version:        0.8.7
Release:        1%{?dist}
Summary:        ROS freight_bringup package

Group:          Development/Libraries
License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-diagnostic-aggregator
Requires:       ros-melodic-fetch-description
Requires:       ros-melodic-fetch-drivers
Requires:       ros-melodic-fetch-navigation
Requires:       ros-melodic-fetch-open-auto-dock
Requires:       ros-melodic-fetch-teleop
Requires:       ros-melodic-graft
Requires:       ros-melodic-joy
Requires:       ros-melodic-ps3joy
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-sick-tim
BuildRequires:  ros-melodic-catkin

%description
Bringup for freight

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
* Tue Aug 06 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.7-1
- Autogenerated by Bloom

* Thu Feb 28 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.6-0
- Autogenerated by Bloom

* Tue Feb 26 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.5-0
- Autogenerated by Bloom

* Thu Feb 21 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.4-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.3-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.2-0
- Autogenerated by Bloom

* Fri Feb 15 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.1-0
- Autogenerated by Bloom

* Wed Feb 13 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.0-1
- Autogenerated by Bloom

* Wed Feb 13 2019 Eric Relson <erelson@fetchrobotics.com> - 0.8.0-0
- Autogenerated by Bloom

