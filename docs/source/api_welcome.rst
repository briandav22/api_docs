Welcome to Scrutinizer Python API's documentation!
==================================================


This is a python wrapper for the Scrutinizer API. It is meant to simplify the process of getting data back from the Scrutinizer API, and can be used as a 'quick start' when building scripts. 

You can clone the code from github:
https://github.com/briandav22/ScrutinizerPythonAPI

There are five steps you will need in order, they are detailed in the Table of Contents on the left, there is a sample code block below that walks through each step as well. 

Typically the biggest changes someone will make is passing arguments into the :ref:`api_json` class. To learn more about what types of arugments you can pass to the :ref:`api_json` class, take a look at the :ref:`api_report`  tab found within any Scrutinzier report. 

The :ref:`api_report` tab displays all of the JSON that is passed to render and report you have run, learning how to use this tab will be crucial to building meaningful requests with the Scrutinizer API.

.. code-block:: python

    from scrut_api import *

    # step 1 : Initiate Scrutinizer client. 
    client = scrut_api_client(
            hostname="some_scrutinizer_ip", 
            authToken="some_auth_token")

    #step 2 : Set up Report JSON. 

    report_object = scrut_json()

    #step 3: Specifcy what type of data you want
    report_format = scrut_data_requested()

    #step 4: Load your client, json, and format into parameters.
    params = scrut_params(
        client=client,
        json_data = report_object.report_json,
        data_requested=report_format.format

    )

    #step 5: make request to Scrutinizer and store results in a variable.

    response = scrut_request(params)


    #step 6 (options) Print out the data in a nicely formatted way. 
    scrut_print(response.data)


.. toctree::
   :maxdepth: 3
   :hidden:
       
   scrut_api_client() <api_client>
   scrut_json() <api_json>
   scrut_data_requested() <api_data_requested>
   scrut_params() <api_params>   
   scrut_request() <api_request>
   scrut_print() <api_printer>
