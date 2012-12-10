%define	beta	RC2

Name:		libspatialite
Version:	3.1.0
Release:	0.%{beta}.1
Summary:	SpatiaLite extension enables SQLite to support spatial data 
Group:		System/Libraries
License:	MPL
URL:		http://www.gaia-gis.it
Source0:	%{name}-%{version}-%{beta}.tar.gz
Patch0:		libspatialite-3.1.0-RC2-linkage.patch
BuildRequires:	sqlite3-devel
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	proj-devel

%description
Core package.

#-------------------------------------------------------------------------------------

%define major 3
%define libname %mklibname spatialite %{major}

%package -n	%{libname}
Summary:	SpatiaLite extension enables SQLite to support spatial data
Group:		System/Libraries

%description -n	%{libname}
The SpatiaLite extension enables SQLite to support spatial data too [aka
GEOMETRY], in a way conformant to OpenGis specifications supports standard
WKT and WKB formats:
- implements SQL spatial functions such as AsText(), GeomFromText(), Area(),
PointN() and alike
- the complete set of OpenGis functions is supported via GEOS, this
comprehending sophisticated spatial analysis functions such as Overlaps(),
Touches(), Union(), Buffer() ..
- supports full Spatial metadata along the OpenGis specifications
- supports importing and exporting from / to shapefiles
- supports coordinate reprojection via PROJ.4 and EPSG geodetic parameters
 dataset
- supports locale charsets via GNU libiconv
- implements a true Spatial Index based on the SQLite's RTree extension

%files -n %{libname}
%{_libdir}/libspatialite.so.%{major}*

#-------------------------------------------------------------------------------------

%define develname %mklibname -d spatialite

%package -n	%{develname}
Summary:	Devel files for spatialite library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	spatialite-devel =  %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
Devel files for spatialite library

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#-------------------------------------------------------------------------------------

%define develname_static %mklibname -d -s spatialite

%package -n	%{develname_static}
Summary:	Devel files for spatialite library
Group:		Development/C
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	spatialite-static-devel =  %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}

%description -n	%{develname_static}
Devel files for spatialite library

%files -n %{develname_static}
%{_libdir}/*.a

#-------------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-%{beta}
%patch0 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

