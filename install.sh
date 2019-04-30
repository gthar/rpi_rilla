#!/bin/bash

lib_dir="/usr/local/lib/python3.4/dist-packages/rpi_rilla"
bin_dir="/usr/local/bin"

cp gpio_light.py $bin_dir
cp ir_screensaver.py $bin_dir
cp light $bin_dir
cp screen $bin_dir
cp alarm $bin_dir
cp alarmctl $bin_dir

chmod +x ${bin_dir}/gpio_light.py
chmod +x ${bin_dir}/ir_screensaver.py
chmod +x ${bin_dir}/light
chmod +x ${bin_dir}/screen

mkdir -p ${lib_dir}
cp rpi_rilla/*.py ${lib_dir}

touch ${lib_dir}/__init__.py
