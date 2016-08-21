queue()
    .defer(d3.csv, "/compare.csv")
    .await(makeGraphs);

function makeGraphs(error, data) {
	


	//Create a Crossfilter instance
	var ndx = crossfilter(data);

	//Define Dimensions
	var areaDim = ndx.dimension(function(d) { return d["area"]; });
	var investmentDim = ndx.dimension(function(d) { return d["investment"]; });
	var rentDifficultyGroupDim = ndx.dimension(function(d) { return d["rent_difficulty_group"]; });
	var saleDifficultyGroupDim = ndx.dimension(function(d) { return d["sale_difficulty_group"]; });
	var salePriceGroupDim = ndx.dimension(function(d) { return d["sale_price_group"]; });
	var rentPriceGroupDim  = ndx.dimension(function(d) { return d["rent_price_group"]; });


	//Calculate metrics
	var numArea = areaDim.group(); 
	var numInvestment = investmentDim.group(); 
	var numRentDifficultyGroup = rentDifficultyGroupDim.group();
	var numSaleDifficultyGroup = saleDifficultyGroupDim.group();
	var numSalePriceGroup = salePriceGroupDim.group();
	var numRentPriceGroup = rentPriceGroupDim.group();
	});

	var all = ndx.groupAll();

    //Charts
	var areaChart = dc.rowChart("#area-chart");
	var investmentChart = dc.rowChart("#investment-chart");
	var rentDifChart = dc.rowChart("#rent-dif-chart");
	var saleDifChart = dc.rowChart("#sale-dif-chart");
	var rentPriceChart = dc.rowChart("#rent-price-chart");
	var salePriceChart = dc.rowChart("#sale-price-chart");


	areaChart
	    .width(300)
	    .height(150)
        	.dimension(areaDim)
	        .group(numArea)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);

	investmentChart
	    .width(300)
	    .height(150)
        	.dimension(investmentDim)
	        .group(numInvestment)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);

	rentDifChart
	    .width(300)
	    .height(150)
        	.dimension(rentDifficultyGroupDim)
	        .group(numRentDifficultyGroup)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);

	saleDifChart
	    .width(300)
	    .height(150)
        	.dimension(saleDifficultyGroupDim)
	        .group(numSaleDifficultyGroup)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);

	rentPriceChart
	    .width(300)
	    .height(150)
        	.dimension(rentPriceGroupDim)
	        .group(numRentPriceGroup)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);

	salePriceChart
	    .width(300)
	    .height(150)
        	.dimension(salePriceGroupDim)
	        .group(numSalePriceGroup)
        	.colors(['#6baed6'])
	        .elasticX(true)
        	.labelOffsetY(10)
	        .xAxis().ticks(4);



		})

    dc.renderAll();

};