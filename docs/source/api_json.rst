.. _api_json:

Scrutinizer JSON 
================

This is the class used to build the JSON data you will be sending to the Scrutinizer backend. 

This class can be iniated without providing any arugments. 

.. code-block:: python    

    scrutinizer_json = scrut_json()

This would store a object into the ``scrutinizer_json`` variable that is accepted as a value to the ``json_data`` arugment in the :ref:`api_params` class.

.. code-block:: python    

    params = scrut_params(
        client=client,
        json_data = scrutinizer_json.report_json, #sending report_json in.
        data_requested=report_format.format

    )

However, you will often find that you want to modify what type of data is returned by the API. In this case you will want to change the arguments passed in this class. 

.. code-block:: python    

    scrutinizer_json = scrut_json(reportTypeLang ="srcHosts")

The are two properties that are availble to objects created from this class. 

``report_json`` : This is what the Python Wrapper is mostly designed for, getting quick access to the report data. This is what we used in the example above. There are many arguments that can be passed in to modify this property. For a full understanding of which values can be used to populate each argument take a look at the :ref:`api_report` while in scrutinizer. At the bottom of this page there is a list of the arguments supported by the ``scrut_json()`` class. 

``status_json``: Instead of passing the ``report_json`` property into :ref:`api_params` you could send the ``status_json`` property. This would return all of the JSON that makes up the status tab. Although this is more of a niche use case, it's meant to display that anything done in the web interface can be accesses via the API. Adding new properties into the ``scrut_json()`` class is simple, you just need to be aware of what you are asking for. 

.. code-block:: python    

    params = scrut_params(
        client=client,
        json_data = scrutinizer_json.status_json, #sending status_json in.
        data_requested=report_format.format

    )




Arguments
----------
reportTypeLang = "conversationsApp"
    The default value will return data for a Pair Reports -> Conversations App report. The value can be set to any valid reportTypeLang, for example  ``reportTypeLang ="srcHosts"`` would return the JSON for a Source Hosts report. 
reportDirections = {"selected": "inbound"}
    The default value for this is inbound. Alternatively you could select ‘outbound’ or ‘both’
dataGranularity = {"selected": "auto"}
    Data Granularity is defaulted to Auto. What this means is that the granularity level is selected based on the time range of the report. For example a report spanning 24 hours will have a auto granularity of 30m, you could force this down by setting it with ``dataGranularity = {"selected": "1m"}``
orderBy = "sum_octetdeltacount"
    Typically a user would leave this as the defaul value. However you could change it to trend by something else, for example ``orderBy = "sum_packetdeltacount"``
times = {"dateRange": "LastTenMinutes"}
    Used to select which time range you want to run the report in. Other samples are ``"Last24Hours"`` or ``"LastHour"`` further examples can be examing by changing timeframs in a scrutinizer report and examining the :ref:`api_report` tab.
filters = {"sdfDips_0": "in_GROUP_ALL"}
    Used to select what devices you want to pull data from. The best best for finding the values is by looking at the :ref:`api_report`. In that tab you may see hex values such as ``"sdfDips_0": "in_0A010104_0A010104-11"``. The API does support sending in the IP information, so you could rewrite that as ``"sdfDips_0": "in_10.1.1.4_10.1.1.4-11"`` and yield the same results. 
    
    Things become a little more complex when you want to filter on specific information. For adding a filter for a port and IP adress would look like this :
    
    .. code-block:: python    

        scrutinizer_json = scrut_json(filters = {
            "sdfDips_0": "in_10.1.1.4_10.1.1.4-11",
            "sdfIps_0": "in_10.1.5.2_Both",
            "sdfPorts_0": "in_445-6"})

rateTotal= {"selected": "rate"}
    This is used to select whether or not you want the returned JSON to show values for rate of traffic, or total amount of traffic. For example I might want to know what the average transfer rate a user had over the course of 24 hours, or I may want to see that total amount of traffic my nightly backups use.
dataFormat= {"selected": "normal"}
    Setting this value to the alternative, which is ``{"selected": "raw"}`` would return raw bit values instead of formatted bit values. For example you would see ``1200000`` instead of ``1.2 Mb/s`` 