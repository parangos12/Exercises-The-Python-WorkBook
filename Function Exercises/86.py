song1={1:"On the first day of Christmas, my true love sent to me A partridge in a pear tree",2:"On the second day of Christmas, my true love sent to me Two turtledoves And a partridge in a pear tree",3:"On the third day of Christmas, my true love sent to me Three French hens Two turtledoves And a partridge in a pear tree",4:"On the fourth day of Christmas, my true love sent to me Four calling birds Three French hens Two turtledoves And a partridge in a pear tree",5:"On the fifth day of Christmas, my true love sent to me Five gold rings (five golden rings) Four calling birds Three French hens Two turtledoves And a partridge in a pear tree",6:"On the sixth day of Christmas, my true love sent to me Six geese a-laying Five gold rings (five golden rings) Four calling birds Three French hens Two turtledoves And a partridge in a pear tree",7:"On the seventh day of Christmas, my true love sent to me Seven swans a-swimming Six geese a-laying Five gold rings (five golden rings) Four calling birds Three French hens Two turtledoves And a partridge in a pear tree"}

def song(verse):
    for i in song1:
        if verse==i:
            print(song1[i])
print(song(7))
