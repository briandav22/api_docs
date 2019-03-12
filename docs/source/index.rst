.. Scrutinizer Python API documentation master file, created by
   sphinx-quickstart on Mon Feb 25 11:21:07 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to Scrutinizer Python API's documentation!
.. ==================================================





.. This is a python wrapper for the Scrutinizer API. It is meant to simplify the process of getting data back from the Scrutinizer API, and can be used as a 'quick start' when building scripts. 

.. Typically the biggest changes someone will make is passing arguments into the :ref:`api_json` class. To learn more about what types of arugments you can pass to the :ref:`api_json` class, take a look at the :ref:`api_report`  tab found within any Scrutinzier report. 

.. The :ref:`api_report` tab displays all of the JSON that is passed to render and report you have run, learning how to use this tab will be crucial to building meaningful requests with the Scrutinizer API.

.. .. code-block:: python

..     client = scrut_api_client(hostname="some_hostname",
..                               authToken="some_authtoken")


..     report_object = scrut_json()
..     report_format = scrut_data_requested()


..     params = scrut_params(
..         client=client,
..         json_data = report_object.report_json,
..         data_requested=report_format.format

..     )


..     response = scrut_request(params)


.. toctree::
   :maxdepth: 3

   Scrutinizer Python Wrapper <api_welcome>
   api_json_example
   api_report

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

