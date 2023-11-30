#!/usr/bin/env ruby
input = ARGV[0]
pattern = /School/
if pattern.match(input)
 puts "Match found"
else
 puts "No match found"
end
