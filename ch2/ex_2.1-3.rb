a = [1, 2, 3]
v = 3

r = nil
a.each_with_index do |e, i|
	if e == v 
		r = i
		break
	end
end

puts r

