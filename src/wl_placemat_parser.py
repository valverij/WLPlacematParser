# -*- coding: utf-8 -*-

import beer_list_parser

# location = "Avon"

draft_string = """
A’Ch ouffe Handle    245. McCh ouffe Belgian Str ong Dar k Ale    8% glass -$8.00
Dark brown, McChouffe has aromas of fruit, bubble gum and earth. Big caramel flavor, earthy hop character, spicy pepper
notes and slightly sour.
Aver y handle 162. White Ras cal Witbier    5.6% $4.50 $5.75
Unfiltered, cloudy with suspended yeast and brewed with coriander and Curacao orange peels. Slightly dry, with
fruity flavors and a zesty spiciness.
ayinger handle    163. Bra u-Weisse    Hefewei zen    5.1% 1/2 Liter $5.00
Cloudy pale yellow color with champagne-like carbonation giving this beer a noticeable crispness. It smells of bananas,
cloves and hints of citrus which all carry over into the flavor. True to style, hop bitterness is scarcely found and it finishes
spicy and dry.
BEERMEISTER HANDLE 226. Kent ucky Bourb on Barrel Ale Str ong Ale    8.2% glass -$4.00
Full of vanilla, wood and bourbon aromas. Moderately carbonated and golden colored. A little bitterness to help
balance this beer, it is full of bourbon, vanilla and wood flavors with a hint of smokiness.
bells HANDLE 167. Two Hearted Ale    ipa    7% $4.50 $5.75
Sweet and bready malt character, big lemon & grapefruit hops notes. Semi dry finish.
boulder HANDLE 174. Sha ke Ch ocolate Porter    Porter    5.9% $4.25 $5.50
Milk chocolatey, along with coffee and big vanilla aromas and flavors. Medium bodied, deep brown color and a
moderate carbonation, Shake has a silky mouthfeel while drinking.
DOGFISH HEAD Handle    190. 90 Min ute IPA Imperial IPA 9% $5.75
Wonderful herbal and pine hops aromas with sweet malt overtones. Big bodied with a big hoppy character, pine,
citrus and earth. Resiny feel with a warming finish.
founders Handle    196. Reds Rye PA Rye Beer    6.6% $4.50 $5.75
Almost startling crimson color brewed with four types of Belgian caramel malts which impart a rich sweetness to this
beer. The smell of grapefruit comes from a vigorous dry-hopping with Amarillo hops. Generous amount of malted rye
leads to a spicy, crisp finish.
glass of the month    227. Kent ucky Bourb on Barrel st out    Stout 6% Glass -$4.00
It smells of roasted malts- bitter coffee and espresso with bourbon, vanilla and wood. Light bourbon and vanilla
notes blend well with the bold coffee flavors.
Goose island handle 201. Ten Hills Pale Ale    Pale Ale    6.2% $4.25 $5.50
Herbal and citrus hop character with toast, caramel, granola malt flavors. Clear amber colored. Light to medium
body. Tastes toasty and bready with a slightly fruity finish.
Great la kes handle    207. Edm und Fit zgerald    Porter    5.8% $4.25 $5.50
Nearly black, Edmund Fitzgerald smells of dark chocolate, caramelized sugar and coffee. Hops character is leafy,
herbal and slightly citrus with malty caramel, coffee and dark chocolate flavors. Medium bodied.
green flash handle    215. Hop Head Red    Red Ale    7% $5.00 $6.25
Hop Head Red has a solid malty base with caramel, candy and brown sugar notes that stand up against a major
hop bill of Amarillo, Nugget and Columbus and then dry-hopped with more Amarillo.
hopp y hopp y handle    220. Heav y Seas Loose Cann on IPA IPA 7.25% $4.25 $5.50
Aroma is heavily floral and nutty. Toffee and subtle citrus tartness bring some complexity. Most notable are grapefruit, nuts
and toasted caramel flavors. It has a resiny and bitter finish.
le ft hand handle 240. Mil k Stout Nitr o sweet st out    6% $4.50 $5.75
Black, brown color. Chocolate & coffee aroma. Light, creamy body. Smooth, sweet to bittersweet finish.
New Belgi um HANDLE 248. New Belgi um Fat Tire Amber Ale    5.2% $4.25 $5.50
Light amber colored, smells biscuity and grainy with green apple and pear sweetness. Mild, balanced overall flavor mostly
biscuit, bread crust, some fruit and almost no hoppiness other than to balance the beer.
ommegang handle    250. Ommegang Adorati on Belgian Str ong Ale    10% Glass -$7.50
This dark brown ale is brewed with five spices: cardamom, coriander, cumin, grains of paradise and mace. Rich
malt sweetness lends to dark fruit and brown sugar flavors.
SIERRA NEVADA Handle    266. Torped o IPA IPA 7.2% $4.50 $5.75
Torpedo is brewed with Two Row Pale and Crystal malts and Magnum and Crystal hops, then dry hopped with more
Magnum, Crystal and Citra hops. This gives Torpedo a bready, maltiness with bold hops flavors of citrus, pine and a
hint of tropical fruit.
Southern tier handle    267. 2XIPA Imperial IPA 11% $5.25
2XIPA is medium bodied, lighter than many double IPAís with a big pine resin aromas along with tropical fruits. These carry
into the flavor and mix with a solid biscuit and caramel maltiness, that are quickly taken over with a bitter hoppy finish..
STONE Handle    275. Sublimel y Sel f Righte ous Ale Bla ck IPA 8.7% $5.75
Sublimely Self-Righteous Ale looks solid black. Chinook, Simcoe and Amarillo hops are used to brew and then dryhopped
again with Amarillo. Bold pine and citrus hops meld well with the smoky, bitter coffee and chocolate flavor.
THIRSTY DOG handle    281. Rail Dog Smoked Porter    Schwar zbier    6.7% $4.25 $5.50
Dark brown to black color. Rail Dog smells smokey with milk chocolate and coffee beans. It has a big chocolate
flavor with iced coffee some toffee, fruit and smoke.
tr oegs Handle    286. Hopba ck Amber    Amber Ale    6% $4.25 $5.50
Reddish copper colored, Hopback Amber has aromas of honey, biscuit, caramel, orange, apricot and pine. Well
balanced with flavors of toasted grain, nuts, apricots and a bit of pine.
Victory handle 294. Ran ch Double IPA Imperial IPA 9% $4.75
Citrus, floral hops and caramel aromas. Tastes sweet with strong flavors of citrus and caramel followed by an earthy
bitter character. Good balance, crisp with a medium body and medium carbonation.
"""

exclusives = """
300 Anchor Steam Beer Ca lifornia Common 4.9 $4.00
301 N orth Coast Old Stock Ale O ld Ale 11.9 $6.75
302 Great Divide Yeti I mp. Stout    9.5 $6.50
303 Bells Kalamazoo Stout    Stout    6 $4.25
304 Weyerbacher Blithering Idiot    Barleywine 11.1 $5.75
"""

# seasonals = """
# 83 De Dolle dulle teve belgian strong ale 10 $7.25
# 87 Heavy Seas Black Cannon B lack IPA    7.25 $4.00
# 91 O vila Quad with Plums Quadrupel 10.2 $6.50
# 94 Ep ic Pfiefferhorn Lager Premium Lager 5.3 $7.00
# 100 B ig Eddy Russian Imp Stout I mperial Stout 9.5 $6.00
# 106 B rewDog Dogma S cotch Ale 7.8 $9.00
# """
location = "Washington Square"
draft_string = """
243. Lindemans Fram boise Fruit Lambic 4% Glass-$5.75
318. Nort h Coast Scr ims haw pilsner 4.7% $4.25 $5.50
290. Vedett Extra White WITBIER 4.7% Glass-$4.75 $6.00
264. SIE RRA NEVADA PALE american pale ale 5% $4.50 $5.7
"""

beer_list_parser.parse_draft_list(draft_string, location)
# print "\n"
# beer_list_parser.parse_exclusives_list(exclusives, location)
# print "\n"
# beer_list_parser.parse_seasonal_list(seasonals, location)

# def main():
#     beer_list_parser.parse_draft_list(draft_string, location)
#     print "\n\n"
#     beer_list_parser.parse_exclusives_list(exclusives, location)
#     print "\n\n"
#     beer_list_parser.parse_seasonal_list(seasonals, location)
# 
# if __name__ == "__main__":
#     main()