.. _api_data_requested:

Data Requested
==============

The ``scrut_data_requested()`` class is used to modify if you want graphing data back, table data back, or both. It is also used to modify the number of rows you want returned in the JSON. 

The default arugments for this class return the top 10 results, and only concern themselves with the data in the table. If you wanted to expand this to include graph data and more rows, a sample arguments would look like this. 

.. code-block:: python    

    data_requested = scrut_data_requested(
        data_requested={
                "inbound" : { 
                    "graph" : "timeseries", #request graphing data
                    "table" : {
                       "query_limit" : {
                               "offset" : 0,
                               "max_num_rows" : 100 #increase max rows
                       }
               }
           }
        )
