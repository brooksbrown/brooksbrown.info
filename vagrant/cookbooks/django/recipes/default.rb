#Install python

execute "Install Python" do
  command "sudo apt-get -q -y install python"
  action :run
end

execute "Install Python PIP" do
  command "sudo apt-get -q -y install python-pip"
  action :run
end

execute "Install Python Virtualenv" do
  command "sudo apt-get -q -y install python-virtualenv"
  action :run
end


execute "Create Vagrant Venv" do
  command "virtualenv #{node[:django][:venv_dir]}"
  user "vagrant"
  group "vagrant"
  action :run
end

execute "install python requirements" do
  command "pip install --environment='#{node[:django][:venv_dir]}' -q -r #{node[:django][:requirements_file]}" 
  user "vagrant"
  group "vagrant"
  returns [0,1]
  action :run
end

