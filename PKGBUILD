# Maintainer: Semyon5700
pkgname=password-generator
pkgver=1.0.0
pkgrel=1
pkgdesc="Simple password generator with GUI"
arch=('any')
url="https://github.com/Semyon5700/password-generator"
license=('GPL3')
depends=('python' 'tk' 'xclip')
source=("password_generator.py"
        "password-generator.desktop")
md5sums=('SKIP' 'SKIP')

package() {
    # Create directories
    install -d "$pkgdir/opt/password-generator"
    install -d "$pkgdir/usr/bin"
    install -d "$pkgdir/usr/share/applications"

    # Install main script
    install -Dm755 password_generator.py "$pkgdir/opt/password-generator/"

    # Create launcher script
    cat > "$pkgdir/usr/bin/password-generator" << EOF
#!/bin/bash
cd /opt/password-generator
exec python3 password_generator.py
EOF
    chmod +x "$pkgdir/usr/bin/password-generator"

    # Install desktop file
    install -Dm644 password-generator.desktop "$pkgdir/usr/share/applications/"
}
