.. _api_data_requested:

Data Requested
==============

The ``scrut_data_requested()`` class is used to modify if you want graphing data back, table data back, or both. It is also used to modify the number of rows you want returned in the JSON. 

The default arugments for this class return the top 10 results, and only concern themselves with the data in the table. If you wanted to expand this to include graph data and more rows, a sample arguments would look like this. 

In the below example the ``data_requested`` variable would have a ``format`` property applied to it. 

.. code-block:: python    

    data_requested = scrut_data_requested(
        data_requested={
                'inbound' : { 
                    'graph' : 'timeseries', #request graphing data
                    'table' : {
                       'query_limit' : {
                               'offset' : 0,
                               'max_num_rows' : 100 #increase max rows
                       }
               }
           }
        )

When passing this variable into params, you want to be sure you specifcy the ``format`` property. 


.. code-block:: python    

    params = scrut_params(
        client=client,
        json_data = report_object.report_json,
        data_requested=report_format.format #make sure to specify the correct property

    )
