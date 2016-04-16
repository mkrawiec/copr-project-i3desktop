PKG_VERSION=4.12.$(date +%Y%m%d)git660d09
PKG_BRANCH=gaps

pkg_service_hook()
{
    git clone -b $PKG_BRANCH https://github.com/Airblader/i3 i3-gaps-$PKG_VERSION
    tar -cvzf i3-gaps-${PKG_VERSION}.tar.gz i3-gaps-$PKG_VERSION
    rm -fr i3-gaps-$PKG_VERSION
}
