# Criar um diretório para setar OE-Core
# mkdir home/oe-core
# cd home/oe-core 
# repo init -u https://github.com/HeitorCervantes  -b dunfell -5.x.y -m tdxref/default.xml
# repo sync 
# . export
# cd layers
# cd meta-nxview/
# tree 
# cd conf/
# code layer.conf
BBPATH .= ":${LAYERDIR}"

BBFILES += "${LAYERDIR}/recipes*/*/*.bb \
            ${LAYERDIR}/recipes*/*/*.bbappend"

BBFILE_COLLECTIONS += "meta-nxview"
BBFILE_PATTERN_meta-nxview = "^${LAYERDIR}/"
BBFILE_PRIORITY_meta-nxview = "97"
LAYERVERSION_meta-nxview = "1"
LAYERSERIES_COMPAT_meta-nxview = "dunfell"

include conf/machine/colibri-imx6ull-extra.conf

# code linux-toradex_5.4-2.3.x.bbappend

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}}:"
unset KBUILD_DEFCONFIG

SRC_URI += "\
            file://logo/logo_custom_clut224.ppm \
            file://dts/imx6ull-colibri-novus-ihm.dts \
            file://dts/imx6ull-colibri-novus-ihm.dtsi \
            file://defconfig"

do_patchextra()
{
    install -d ${STAGING_KERNEL_DIR}/drivers/video/logo/
    install im 0644 ${WORKDIR}/logo/logo_custom_clut224.ppm ${STAGING_KERNEL_DIR}/drivers/video/logo/

    install -d ${STAGING_KERNEL_DIR}/arch/arm/boot/dts/
    install im 0644 ${WORKDIR}/dts/imx6ull-colibri-novus-ihm.dts ${STAGING_KERNEL_DIR}/arch/arm/boot/dts/
    install im 0644 ${WORKDIR}/dts/imx6ull-colibri-novus-ihm.dtsi ${STAGING_KERNEL_DIR}/arch/arm/boot/dts/
}

addtask patchextra after dp_patch before do_compile

# code touch-udev-rules_1.0.bb

SUMMARY = "touch udev rules"
DESCRIPTION = "add udev rules to invert touch matrix"

LICENSE = "CLOSED"

SRC_URI = "file://libinput.rules"

do_install()
{
    install -d ${D}/etc/udev/rules.d/
    install -m 0666 ${WORKDIR}/libinput.rules ${D}/etc/udev/rules.d/
}

FILES_${PN} += "/ect/udev/rules.d/libinput.rules"

