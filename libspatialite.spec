#define	beta	RC2

Name:		libspatialite
Version:	5.0.1
Release:	%{?beta:0.%{beta}.}1
Summary:	SpatiaLite extension enables SQLite to support spatial data 
Group:		System/Libraries
License:	MPL
URL:		http://www.gaia-gis.it
Source0:	http://www.gaia-gis.it/gaia-sins/libspatialite-sources/libspatialite-%{version}%{?beta:-%{beta}}.tar.gz
BuildRequires:	sqlite3-devel
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	proj-devel
BuildRequires:	pkgconfig(rttopo)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(minizip)

%description
Core package.

#-------------------------------------------------------------------------------------

%define major 7
%define libname %mklibname spatialite

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
%{_libdir}/mod_spatialite.so.%{major}*
%{_libdir}/libspatialite.so
%{_libdir}/mod_spatialite.so

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
%{_libdir}/pkgconfig/*.pc

#-------------------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
autoreconf -fi
if echo %{optflags} |grep -E -- '-O[sz] '; then
	# _Float32 doesn't like -Os
	export CFLAGS="%{optflags} -O3"
	export CXXFLAGS="%{optflags} -O3"
fi
%configure

%build
%make_build

%install
%make_install
