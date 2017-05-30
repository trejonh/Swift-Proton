sudo deb http://www.deb-multimedia.org jessie main non-free deb-src http://www.deb-multimedia.org jessie main non-free
sudo apt-get update
sudo apt-get install deb-multimedia-keyring
sudo apt-get update
sudo apt-get remove ffmpeg
sudo apt-get install build-essential libmp3lame-dev libvorbis-dev libtheora-dev libspeex-dev yasm pkg-config libfaac-dev libopenjpeg-dev libx264-dev
mkdir software
cd software
wget http://ffmpeg.org/releases/ffmpeg-2.7.2.tar.bz2
cd ..
mkdir src
cd src
tar xvjf ../software/ffmpeg-2.7.2.tar.bz2
cd ffmpeg-2.7.2
./configure --enable-gpl --enable-postproc --enable-swscale --enable-avfilter --enable-libmp3lame 
--enable-libvorbis --enable-libtheora --enable-libx264 --enable-libspeex --enable-shared 
--enable-pthreads --enable-libopenjpeg --enable-libfaac --enable-nonfree
make
sudo make install
sudo ldconfig