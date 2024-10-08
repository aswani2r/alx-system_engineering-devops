#increase the amount of traffic nginx sever can handle

#increase the ULIMIT of the default file
exec { 'fix--for--nginx':
	command => 'sed -i "s/15/4096/" /etc/default/nginx',
	path	=> '/usr/local/bin/:/bin/'
}
#restart nginx
exec { 'nginx-restart':
	command => 'nginx restart',
	path	=> '/etc/init.d/'
}
