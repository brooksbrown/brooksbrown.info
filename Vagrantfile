# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
 config.vm.box = "precise32"

 config.vm.forward_port 80, 8080
 config.vm.forward_port 8000, 8000
 
 config.vm.provision :chef_solo do |chef|
     chef.cookbooks_path = "vagrant/cookbooks"
     chef.add_recipe "apt"
     chef.add_recipe "apache2"
     chef.add_recipe "apache2::mod_php5"
     chef.add_recipe "apache2::mod_wsgi"
     chef.add_recipe "django"
     chef.log_level = :debug 
  #   # You may also specify custom JSON attributes:
  #   chef.json = { :mysql_password => "foo" }
   end

end
