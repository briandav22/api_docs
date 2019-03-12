.. _api_params:

Request Parameters
==================

This class is used to bind together the :ref:`api_client` with :ref:`api_json`.

There are three arguments this class takes. 

``client`` : This is generated from the :ref:`api_client`. 

``json_data`` : This is generated from the :ref:`api_json` class. For the most part you are going to be sending in the ``report_json`` property. However, if you review the :ref:`api_json` documentation you will see that you can also pass in other properties if desired. 

``data_requested`` : This is generated from the :ref:`api_data_requested` class, you want to send it in with the ``format`` property. 

Here is an example snipper of passing arguments into the scrut_params class. 

.. code-block:: python

    params = scrut_params(
        client=client, # generated from scrut_api_client
        json_data = report_object.report_json, # generated from scrut_json, 
                                               # make sure you specicy a property
        data_requested=report_format.format # generated from scrut_data_requested, 
                                            # make sure you specify the format property.

    )