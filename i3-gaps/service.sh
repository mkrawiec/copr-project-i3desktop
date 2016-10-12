PKG_VERSION=4.12

pkg_service_hook()
{
    git clone -b $PKG_VERSION --depth 1 --recursive \
		https://github.com/Airblader/i3 \
		i3-gaps-$PKG_VERSION

    tar -cvzf i3-gaps-${PKG_VERSION}.tar.gz i3-gaps-$PKG_VERSION
    rm -fr i3-gaps-$PKG_VERSION
}
