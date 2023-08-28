# Maintainer: clq9920 <clq9920@163.com>
pkgname=lonenote
pkgver=1.0
pkgrel=1
url='https://github.com/clq9920/lonenote'
pkgdesc="Infinite Canvas Handwriting Note Software Based on Pyside6"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
license=('GPL2')
depends=('pyside6')
source=("git+https://github.com/clq9920/lonenote.git")
md5sums=('SKIP')


build() {
echo "1"
}
package() {
	echo "$srcdir/$pkgname"
	cd "$srcdir/$pkgname"
	install -Dm755 "lonenote.py" "$pkgdir/usr/bin/lonenote"
	install -Dm644 $pkgname.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
	install -Dm644 application-lonenote.png "$pkgdir/usr/share/icons/application-lonenote.png"
	install -Dm644 lonenote.xml "$pkgdir/usr/share/mime/packages/lonenote.xml"
}
