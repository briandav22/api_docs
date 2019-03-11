Scrutinizer API
===============

This is a python wrapper for the Scrutinizer API. It is meant to simplimfy the process of getting data back from scrutinizers, and can be used as a 'quick start' when building scripts to work with the API. 

Typically the biggest changes someone will make is by passing arguments into the :ref:`scrut_json` class. To learn more about what types of arugments you can pass to the :ref:`scrut_json` class, take a look at the :ref:`report_json`  tab found within any Scrutinzier report. 

The :ref:`report_json` tab displays all of the JSON that is passed to render and report you have run, learning how to use this tab will be crucial to building meaningful requests with the Scrutinizer API.

.. code-block:: python

    client = scrut_api_client(hostname="some_hostname",
                              authToken="some_authtoken")


    report_object = scrut_json()
    report_format = scrut_data_requested()


    params = scrut_params(
        client=client,
        json_data = report_object.report_json,
        data_requested=report_format.format

    )


    response = scrut_request(params)



.. toctree::
   :maxdepth: 4

   api_client
   scrut_json
   params