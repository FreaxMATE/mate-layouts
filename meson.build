project(
    'mate-layouts',
    version: '0.0.0',
    license: 'GPL3',
    meson_version: '>=0.50.0'
)

dependency('pygobject-3.0')
dependency('gtk+-3.0')
dependency('libnotify')

prefix = get_option('prefix')
datadir = get_option('datadir')
bindir = get_option('bindir')
libdir = get_option('libdir')
policydir = join_paths(datadir, 'polkit-1/actions')
genericdir = join_paths(datadir, 'mate-layouts/')
icondir = join_paths(datadir, 'icons/hicolor/')
schemadir = join_paths(datadir, 'glib-2.0/schemas')

conf_data = configuration_data()
conf_data.set('HELPER_DIR', join_paths(prefix, libdir, 'mate-layouts/'))
conf_data.set('GLADE_DIR', join_paths(prefix, datadir, 'mate-layouts/'))

# Python scripts
configure_file(input: 'src/mate-layouts', output: 'mate-layouts', install_dir: bindir, install: true, configuration: conf_data)
configure_file(input: 'src/mate-layouts-helper', output: 'mate-layouts-helper', install_dir: join_paths(libdir,'mate-layouts/'), install: true, configuration: conf_data)

# Metadata
configure_file(input: 'data/org.github.FreaxMATE.mate-layouts.appdata.xml',output: 'org.github.FreaxMATE.mate-layouts.appdata.xml',install_dir: join_paths(datadir, 'metainfo'),install: true,configuration: conf_data)
configure_file(input: 'data/org.github.FreaxMATE.mate-layouts.desktop',output: 'org.github.FreaxMATE.mate-layouts.desktop',install_dir: join_paths(datadir, 'applications'),install: true,configuration: conf_data)
configure_file(input: 'data/org.github.FreaxMATE.mate-layouts.policy',output: 'org.github.FreaxMATE.mate-layouts.policy',install_dir: policydir,install: true,configuration: conf_data)
configure_file(input: 'data/org.github.FreaxMATE.mate-layouts.ui',output: 'org.github.FreaxMATE.mate-layouts.ui',install_dir: genericdir,install: true,configuration: conf_data)
install_data(['data/org.github.FreaxMATE.mate-layouts.gschema.xml',], install_dir: schemadir)

# Icons
install_data(['data/icons/hicolor/16x16/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'16x16/apps/'))
install_data(['data/icons/hicolor/22x22/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'22x22/apps/'))
install_data(['data/icons/hicolor/24x24/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'24x24/apps/'))
install_data(['data/icons/hicolor/32x32/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'32x32/apps/'))
install_data(['data/icons/hicolor/36x36/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'36x36/apps/'))
install_data(['data/icons/hicolor/48x48/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'48x48/apps/'))
install_data(['data/icons/hicolor/64x64/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'64x64/apps/'))
install_data(['data/icons/hicolor/72x72/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'72x72/apps/'))
install_data(['data/icons/hicolor/96x96/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'96x96/apps/'))
install_data(['data/icons/hicolor/128x128/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'128x128/apps/'))
install_data(['data/icons/hicolor/256x256/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'256x256/apps/'))
install_data(['data/icons/hicolor/512x512/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'512x512/apps/'))
install_data(['data/icons/hicolor/1024x1024/apps/org.github.FreaxMATE.mate-layouts.png',], install_dir: join_paths(icondir,'1024x1024/apps/'))
install_data(['data/icons/hicolor/scalable/apps/org.github.FreaxMATE.mate-layouts.svg',], install_dir: join_paths(icondir,'scalable/apps/'))

# Layouts previews
install_subdir('data/layout-previews/', install_dir : genericdir)

meson.add_install_script('meson-post-install.py')

