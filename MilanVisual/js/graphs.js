queue()
    .defer(d3.csv, "compare.csv")
    .await(makeGraphs);

function makeGraphs(error, data) {

	//Create a Crossfilter instance
	var ndx = crossfilter(data);

	//Define Dimensions
	var areaDim = ndx.dimension(function(d) { return d["area"]+':  '+(d.gross_yield* 100).toFixed(2) + '%'; });
	var investmentDim = ndx.dimension(function(d) { return d["investment"]; });
	var rentDifficultyGroupDim = ndx.dimension(function(d) { return d["rent_difficulty_group"]; });
	var saleDifficultyGroupDim = ndx.dimension(function(d) { return d["sale_difficulty_group"]; });
	var salePriceGroupDim = ndx.dimension(function(d) { return d["sale_price_group"]; });
	var rentPriceGroupDim  = ndx.dimension(function(d) { return d["rent_price_group"]; });
  var grossYieldDim  = ndx.dimension(function(d) { return +d["gross_yield"]; });


	//Calculate metrics
	var numArea = areaDim.group().reduceSum(function (d) {return d.gross_yield;});
	var numInvestment = investmentDim.group();
	var numRentDifficultyGroup = rentDifficultyGroupDim.group();
	var numSaleDifficultyGroup = saleDifficultyGroupDim.group();
	var numSalePriceGroup = salePriceGroupDim.group();
	var numRentPriceGroup = rentPriceGroupDim.group();
  var numGrossYield = grossYieldDim.group().reduceSum(function (d) {return d.gross_yield;});

	var all = ndx.groupAll();

  //Charts
	areaChart = dc.rowChart("#area-chart");
	investmentChart = dc.rowChart("#investment-chart");
	rentDifChart = dc.rowChart("#rent-dif-chart");
	rentDifPieChart = dc.pieChart("#rent-dif-pie-chart");
	saleDifChart = dc.rowChart("#sale-dif-chart");
	saleDifPieChart = dc.pieChart("#sale-dif-pie-chart");
	rentPriceChart = dc.rowChart("#rent-price-chart");
	salePriceChart = dc.rowChart("#sale-price-chart");

	areaChart
	    .width(600)
	    .height(1000)
        	.dimension(areaDim)
	        .group(numArea)
            .ordering(function(d) { return -d.value })
            .colors(['#6baed6'])
	        .elasticX(true)
			.labelOffsetY(10)
			.turnOnControls(true)
	        .xAxis().ticks(4).tickFormat(function (v) {
            return (v* 100).toFixed(2) + '%';
			});

	investmentChart
	    .width(300)
	    .height(150)
        	.dimension(investmentDim)
	        .group(numInvestment)
        	.colors(['#6baed6'])
			.ordering(function(d) { return d.value })
			.elasticX(true)
	        .xAxis().ticks(4);

	rentDifChart
	    .width(300)
	    .height(150)
        	.dimension(rentDifficultyGroupDim)
	        .group(numRentDifficultyGroup)
        	.colors(['#6baed6'])
			.ordering(function(d) { return d.value })
	        .elasticX(true)
	        .xAxis().ticks(4);

	rentDifPieChart
		.width(150)
		.height(150)
		.dimension(rentDifficultyGroupDim)
		.group(numRentDifficultyGroup)
		.ordering(function(d) { return d.value })
		.slicesCap(17)
		.innerRadius(30)


	saleDifChart
	    .width(300)
	    .height(150)
        	.dimension(saleDifficultyGroupDim)
	        .group(numSaleDifficultyGroup)
        	.colors(['#6baed6'])
			.ordering(function(d) { return d.value })
	        .elasticX(true)
	        .xAxis().ticks(4);

	saleDifPieChart
		.width(150)
		.height(150)
		.dimension(saleDifficultyGroupDim)
		.group(numSaleDifficultyGroup)
		.ordering(function(d) { return d.value })
		.slicesCap(17)
		.innerRadius(30)

	rentPriceChart
	    .width(300)
	    .height(150)
        	.dimension(rentPriceGroupDim)
	        .group(numRentPriceGroup)
        	.colors(['#6baed6'])
			.ordering(function(d) { return d.value })
	        .elasticX(true)
	        .xAxis().ticks(4);

	salePriceChart
	    .width(300)
	    .height(150)
        	.dimension(salePriceGroupDim)
	        .group(numSalePriceGroup)
        	.colors(['#6baed6'])
			.ordering(function(d) { return d.value })
	        .elasticX(true)
	        .xAxis().ticks(4);

    dc.renderAll();

};
