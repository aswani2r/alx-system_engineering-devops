# Install a specific version of flask (2.1.0)
package {'flask==2.1.0':
  ensure   => 'installed',
  provider => 'pip'
}
