cd quickstart/
ls
ls -l
exit
ls
cd quickstart/
ls
cd ls
cd ..
ls
sls -l
ls
pwd
cd quickstart/
ls
cd server1/
ls
cd pickup-dir/
lc
ls
mount
exit
ls
cd quickstart/
ls
cd ..
ls
cd quickstart/
ls
cd ..
rm -rf quickstart/
umount
mount
umount  home_vagrant_quickstart_server1_pickup-dir
umount  /home/vagrant/quickstart/server1/pickup-dir
mount
exit
cd /vagrant
ls
ls -l
cd /
cd ..
ls
cd ~
ls
 zato quickstart create ~ sqlite localhost 6379  --verbose
ls
cd ..
exit
. ~/.bash_profile
echo 'export PATH=$PATH:/opt/zato/current/bin' >>~/.bash_profile
. ~/.bash_profile
zato --version
echo $PATH
sudo apt-get install zato
curl -s https://zato.io/repo/zato-0CBD7F72.pgp.asc | sudo apt-key add -
sudo apt-add-repository https://zato.io/repo/stable/2.0/ubuntu
sudo apt-get update
sudo apt-get install -y zato
mkdir q    mkdir ~/quickstart
ls
rm q
rmdir q
ls
zato quickstart create ~/quickstart sqlite localhost 6379  --verbose
zato update password /home/vagrant/quickstart/web-admin/ admin
cd /vagrant
ls
mount
exit
