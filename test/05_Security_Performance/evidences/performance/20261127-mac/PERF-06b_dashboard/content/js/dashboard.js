/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 37.99926199261993, "KoPercent": 62.00073800738007};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.37738745387453876, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.3403892715262923, 500, 1500, "GET /api/tasks"], "isController": false}, {"data": [0.9979746151768836, 500, 1500, "PUT /api/tasks/[id]"], "isController": false}, {"data": [0.34796947140299633, 500, 1500, "POST /api/tasks"], "isController": false}, {"data": [1.0, 500, 1500, "POST /api/login"], "isController": false}, {"data": [0.34286379872651035, 500, 1500, "GET /api/dashboard"], "isController": false}, {"data": [0.9966243586281394, 500, 1500, "DELETE /api/tasks/[id]"], "isController": false}, {"data": [0.33866400519914586, 500, 1500, "GET /api/tasks?q="], "isController": false}, {"data": [0.3400226918167636, 500, 1500, "GET / (HTML)"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 135500, 84011, 62.00073800738007, 35.76104059040609, 0, 37901, 7.0, 29.0, 82.0, 297.9900000000016, 1093.959406436195, 4375.379501859933, 112.60274476332532], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["GET /api/tasks", 42541, 27998, 65.81415575562399, 30.279777156155234, 0, 6142, 8.0, 79.0, 124.0, 244.0, 426.5103968238054, 1063.0649145106875, 37.782987921337046], "isController": false}, {"data": ["PUT /api/tasks/[id]", 3703, 6, 0.16203078584931138, 15.812314339724571, 0, 689, 6.0, 38.0, 65.0, 154.0, 37.17274333440411, 16.118192688047102, 11.028942937755984], "isController": false}, {"data": ["POST /api/tasks", 10613, 6909, 65.0994063883916, 17.735795722227415, 0, 4708, 8.0, 30.0, 51.0, 130.0, 106.43973964235927, 171.24459129190944, 12.962251401578593], "isController": false}, {"data": ["POST /api/login", 50, 0, 0.0, 57.54, 43, 142, 51.0, 79.69999999999999, 112.89999999999999, 142.0, 5.073051948051948, 1.735439548244724, 1.1665046989143668], "isController": false}, {"data": ["GET /api/dashboard", 32195, 21128, 65.6250970647616, 16.634570585494785, 0, 4704, 8.0, 34.0, 56.0, 115.0, 322.86046651557393, 504.9627449407329, 29.193810921799475], "isController": false}, {"data": ["DELETE /api/tasks/[id]", 3703, 10, 0.2700513097488523, 9.716176073453969, 0, 1408, 3.0, 16.0, 37.0, 109.96000000000004, 37.17162388700951, 7.46574919192122, 10.582271579718729], "isController": false}, {"data": ["GET /api/tasks?q=", 21542, 14217, 65.9966576919506, 26.128864543682045, 0, 4842, 9.0, 63.0, 106.0, 202.9900000000016, 215.98804856773313, 486.9347203457594, 19.605879870308915], "isController": false}, {"data": ["GET / (HTML)", 21153, 13743, 64.96950787122394, 102.74816810854243, 0, 37901, 10.0, 304.0, 388.9500000000007, 662.0, 171.23498364796166, 2570.59434119297, 15.018502290904381], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 84011, 100.0, 62.00073800738007], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 135500, 84011, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 84011, "", "", "", "", "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": ["GET /api/tasks", 42541, 27998, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 27998, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["PUT /api/tasks/[id]", 3703, 6, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 6, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["POST /api/tasks", 10613, 6909, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 6909, "", "", "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": ["GET /api/dashboard", 32195, 21128, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 21128, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["DELETE /api/tasks/[id]", 3703, 10, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 10, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["GET /api/tasks?q=", 21542, 14217, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 14217, "", "", "", "", "", "", "", ""], "isController": false}, {"data": ["GET / (HTML)", 21153, 13743, "Non HTTP response code: java.net.BindException/Non HTTP response message: Can't assign requested address", 13743, "", "", "", "", "", "", "", ""], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
