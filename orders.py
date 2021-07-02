orders = {
	'samsung,OEM Samsung Washing Machine Pulsator Washplate Cap Shipped With WA48J7700AW, WA48J7700AW/A,WA48J7700AW/AA':20916,
	'samsung,OEM Samsung Chromen Washing Machine  Washplate Pulsator Cap Shipped with WA52M7750AW/A4,WA25M7750AW/A4':91995,
        'samsung,SAMSUNG Washing Machine Spring Hanger, DC61-01257M':22970,
        'samsung,Samsung DC97-17022B Assy Detergent':32959,
	'samsung,Samsung DC66-00470A DAMPER SHOCK':29981,
        'samsung,Samsung DC64-00519D Samsung Washing Machine Door Lock Washer Dryer Dishwashe -MPGH4498 349Y49HBRG9109150':52000,
        'samsung,Samsung DC97-16991A Assembly Filter':13000

}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=False)

for i in sort_orders:
	print((i[0], i[1]))
