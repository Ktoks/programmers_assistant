#!/bin/bash
cd ~ || exit 1
apt install sudo
err=$?
if [ $err != 0 ] ; then
    echo "error installing sudo: $err"
    exit 1
fi
apt update
apt upgrade -y
err=$?
if [ $err != 0 ] ; then
    echo "error upgrading: $err"
    exit 1
fi
git --version
err=$?
if [ $err = 127 ] ; then
    apt install git -y
    err=0
fi
git config --global core.autocrlf false
cd ~ || exit 1
mkdir .ssh
chmod 700 .ssh
apt install python3 python3-pip ipython3 -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing python 3, pip 3, or ipython 3: $err"
    exit 1
fi
python3 -m pip install jupyter
err=$?
if [ $err != 0 ] ; then
    echo "error installing jupyter: $err"
    exit 1
fi
apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing g++, glut, glut, mesa, valgrind, or libgtest: $err"
    exit 1
fi
apt install gcc-multilib g++-multilib -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing gcc or g++ $err"
    exit 1
fi
apt install build-essential -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing build-essential: $err"
    exit 1
fi
#########################################################
sudo apt-get install python-pyaudio python3-pyaudio sox
err=$?
if [ $err != 0 ] ; then
    echo "error installing pyaudio: $err"
    exit 1
fi
apt update && apt upgrade -y
cd ~ || exit 1
# wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
# bash Anaconda3-2019.10-Linux-x86_64.sh
# jupyter notebook

# apt update && apt upgrade -y
# source .bashrc

apt install zsh -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing zsh: $err"
    exit 1
fi
echo "if [ -t 1 ] ; then
exec zsh
fi" >> ~/.bashrc
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" -y
err=$?
if [ $err != 0 ] ; then
    echo "error installing oh my zsh: $err"
    exit 1
fi

echo "---------------------
It is suggested you run these commands with your
username once this script has finished:
cd .ssh || exit 1
cp /mnt/c/Users/{insert your username here}/.ssh/id_rsa* .
chmod 600 id_rsa
chmod 644 id_rsa.pub
---------------------"
echo "After running the above suggested commands,
Please copy your rsa key and paste it to
your github's authorized keys using this command:
cat ~/.ssh/id_rsa.pub
---------------------"
