Name: libspatialite
Version: 2.3.1
Release: %mkrel 2
Summary: SpatiaLite extension enables SQLite to support spatial data 
Group: System/Libraries
License: MPL
URL: http://www.gaia-gis.it
Source0: %{name}-%{version}.tar.gz
BuildRequires: sqlite3-devel
BuildRequires: geos-devel
BuildRequires: proj-devel >= 4.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Core package.

#-------------------------------------------------------------------------------------

%define major 1
%define libname %mklibname spatialite %{major}

%package -n	%{libname}
Summary: SpatiaLite extension enables SQLite to support spatial data
Group: System/Libraries

%description -n	%{libname}
The SpatiaLite extension enables SQLite to support spatial data too [aka
GEOMETRY], in a way conformant to OpenGis specifications supports standard 
WKT and WKB formats: 
- implements SQL spatial functions such as AsText(), GeomFromText(), Area(),
PointN() and alike
- the complete set of OpenGis functions is supported via GEOS, this comprehending
sophisticated spatial analysis functions such as Overlaps(), Touches(), Union(),
Buffer() ..
- supports full Spatial metadata along the OpenGis specifications
- supports importing and exporting from / to shapefiles
- supports coordinate reprojection via PROJ.4 and EPSG geodetic parameters dataset
- supports locale charsets via GNU libiconv
- implements a true Spatial Index based on the SQLite's RTree extension

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libspatialite.so.%{major}*

#-------------------------------------------------------------------------------------

%define develname %mklibname -d spatialite

%package -n	%{develname}
Summary: Devel files for spatialite library
Group: Development/C
Provides: %{name}-devel = %{version}
Provides: spatialite-devel =  %{version}
Requires: %{libname} = %{version}

%description -n	%{develname}
Devel files for spatialite library

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

#-------------------------------------------------------------------------------------

%define develname_static %mklibname -d -s spatialite

%package -n	%{develname_static}
Summary: Devel files for spatialite library
Group: Development/C
Provides: %{name}-static-devel = %{version}
Provides: spatialite-static-devel =  %{version}
Requires: %{develname} = %{version}

%description -n	%{develname_static}
Devel files for spatialite library

%files -n %{develname_static}
%{_libdir}/*.a

#-------------------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}

%build
# Create amalgamation 
make

cd amalgamation
%configure2_5x \
	--with-proj-include=%_includedir \
	--with-proj-lib=%_libdir \
	--with-geos-include=%_includedir \
	--with-geos-lib=%_libdir


%make

%install
rm -rf %{buildroot}

cd amalgamation
%makeinstall_std

%clean
rm -rf %{buildroot}

