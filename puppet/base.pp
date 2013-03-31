Exec {
	path=> ["/usr/bin", "/bin", "/usr/sbin", "/sbin", "/usr/local/bin", "/usr/local/sbin"]
}

class { 'python':
    virtualenv => true,
}

python::virtualenv { '/vagrant/venv':
	ensure => present,
	requirements => '/vagrant/requirements.txt',
}
