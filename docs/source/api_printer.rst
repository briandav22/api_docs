Scrutinizer Printer
===================

The scrutinzier printer can be used both for when you are building your requests, perhaps to troubleshoot that they are appearing as you thing, and also to print the data returned from Scrutinizer in a nicely formatted way. 


The most common use case for ``scrut_print()`` is to take a look at the data returned by Scrutinizer. This can be done simply by passings the data property into the class.  Is will come back nicley formatted, similar to :ref:`api_json_example`

.. code-block:: python    


    response = scrut_request(params)

    scrut_print(response.data)  #print data returned by Scrutinizer.. 


Another use case may be to take a look at some of the variables you have constructed in your script. Say you have built out a complex :ref:`api_json` and you wanted to see what it looks like. You could utilize the printer class by passing in the other class as an arugment. 

For Example:

.. code-block:: python    

    params = scrut_params(
        client=client,
        json_data = report_object.report_json,
        data_requested=report_format.format

    )

    scrut_print(params)

Returns :

.. code-block:: python   

    data_for_req : {'rm': 'report_api', 'action': 'get', 'rpt_json': '{"reportTypeLang": "applications", "reportDirections": {"selected": "inbound"}, "dataGranularity": {"selected": "auto"}, "orderBy": "sum_octetdeltacount", "times": {"dateRange": "LastTenMinutes"}, "filters": {"sdfDips_0": "in_10.1.1.252_ALL"}, "rateTotal": {"selected": "rate"}, "dataFormat": {"selected": "normal"}, "bbp": {"selected": "percent"}}', 'data_requested': '{"inbound": {"table": {"query_limit": {"offset": 0, "max_num_rows": 10}}}}', 'authToken': 'BI5NGMrqd3ZsAvWPHekHmPUT'}

    url : https://scrutinizer.plxr.local/fcgi/scrut_fcgi.fcgi

    verify : False


