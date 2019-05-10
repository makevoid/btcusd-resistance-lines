require 'bundler'
Bundler.require :default

DOCKER = File.exists? "/.dockerenv"

host = "localhost"
host = "ipfs" if DOCKER
FS = IPFS::Client.new host: "http://#{host}", port: 5001
