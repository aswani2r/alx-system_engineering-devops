# executes a killprocess

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
}
